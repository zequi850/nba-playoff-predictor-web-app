from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = "nba_2024_25_head_to_head.xlsx"

def load_data():
    detail = pd.read_excel(EXCEL_FILE, sheet_name="Detail")
    validation = pd.read_excel(EXCEL_FILE, sheet_name="Validation")
    teams = sorted(validation["Team"].dropna().unique())
    return detail, validation, teams

detail_df, validation_df, teams = load_data()

def get_team_record(team):
    row = validation_df[validation_df["Team"] == team].iloc[0]
    return int(row["Wins"]), int(row["Losses"])

def predict_matchup(team_a, team_b):
    if team_a == team_b:
        return None

    matchup = detail_df[
        (detail_df["Team"] == team_a) &
        (detail_df["Opponent"] == team_b)
    ]

    wins_a, losses_a = get_team_record(team_a)
    wins_b, losses_b = get_team_record(team_b)

    win_pct_a = wins_a / (wins_a + losses_a)
    win_pct_b = wins_b / (wins_b + losses_b)

    if not matchup.empty:
        head_to_head_wins = int(matchup.iloc[0]["Wins"])
        head_to_head_losses = int(matchup.iloc[0]["Losses"])
        total_games = head_to_head_wins + head_to_head_losses

        if total_games > 0:
            h2h_pct_a = head_to_head_wins / total_games
        else:
            h2h_pct_a = 0.5
    else:
        head_to_head_wins = 0
        head_to_head_losses = 0
        h2h_pct_a = 0.5

    h2h_pct_b = 1 - h2h_pct_a

    rating_a = (0.70 * win_pct_a) + (0.30 * h2h_pct_a)
    rating_b = (0.70 * win_pct_b) + (0.30 * h2h_pct_b)

    probability_a = rating_a / (rating_a + rating_b)
    probability_b = rating_b / (rating_a + rating_b)

    return {
        "team_a": team_a,
        "team_b": team_b,
        "probability_a": round(probability_a * 100, 2),
        "probability_b": round(probability_b * 100, 2),
        "team_a_record": f"{wins_a}-{losses_a}",
        "team_b_record": f"{wins_b}-{losses_b}",
        "head_to_head": f"{head_to_head_wins}-{head_to_head_losses}"
    }

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        team_a = request.form.get("team_a")
        team_b = request.form.get("team_b")

        prediction = predict_matchup(team_a, team_b)

        if prediction is None:
            error = "Please select two different teams."

    return render_template(
        "index.html",
        teams=teams,
        prediction=prediction,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)