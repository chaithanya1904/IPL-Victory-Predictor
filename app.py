from flask import Flask, render_template, request
import pickle
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
#pipe = pickle.load(open('pipe.pkl', 'rb'))
pipe = joblib.load('model.joblib')

# Teams and cities data
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        city = request.form['city']
        target = int(request.form['target'])
        score = int(request.form['score'])
        overs = float(request.form['overs'])
        wickets = int(request.form['wickets'])

        # Calculate remaining values
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left

        # Create input DataFrame for prediction
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_left],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Predict win probability
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        return render_template('index.html', teams=teams, cities=cities, 
                               win_prob=round(win * 100), loss_prob=round(loss * 100), 
                               batting_team=batting_team, bowling_team=bowling_team)
    return render_template('index.html', teams=teams, cities=cities)

if __name__ == '__main__':
    app.run(debug=True)
