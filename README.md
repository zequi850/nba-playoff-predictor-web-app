# NBA Playoff Predictor Web App

## Overview

This project is a Flask-based web application that predicts NBA matchup outcomes using 2024–2025 season performance data and head-to-head records.

Users select two NBA teams through an interactive web interface. The Python backend processes historical performance data and generates probability-based predictions for the selected matchup.

---

## Features

- Interactive web application built with Flask
- NBA team matchup selection
- Head-to-head performance analysis
- Season record comparison
- Probability-based prediction engine
- Dynamic content rendering
- Excel dataset integration using Pandas
- Frontend and backend integration

---

## Technologies Used

- Python
- Flask
- Pandas
- OpenPyXL
- HTML
- CSS

---

## Dataset

The project uses NBA 2024–2025 season head-to-head performance data stored in:

```text
nba_2024_25_head_to_head.xlsx
```

The dataset contains team matchup statistics used to calculate prediction probabilities.

---

## Installation

### Requirements

- Python 3.14+
- pip

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
py -3.14 app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
nba-playoff-predictor-web-app
│
├── app.py
├── requirements.txt
├── README.md
├── nba_2024_25_head_to_head.xlsx
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

---

## Skills Demonstrated

### Programming

- Python Development
- Flask Web Development
- Backend Logic Implementation

### Data Analysis

- Data Processing
- Excel Data Integration
- Statistical Analysis
- Probability Modeling

### Web Development

- HTML
- CSS
- User Interface Design
- Frontend/Backend Integration

### Software Engineering

- Project Documentation
- Version Control with GitHub
- Application Architecture
- Technical Problem Solving

---

## Author

**Ezequiel Soto Piñero**

Graduate Student – Applied Mathematics

GitHub:
https://github.com/zequi850
