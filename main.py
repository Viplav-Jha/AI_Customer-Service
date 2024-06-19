from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Load the CSV data
file_path = 'bank-full.csv'
data = pd.read_csv(file_path)

# Convert column names to a set for quick lookup
column_names = set(data.columns)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()
    response = ""

    # Check if user input contains any column names
    if 'age' in user_input:
        response = f"The average age of the customers is {data['age'].mean():.2f} years."
    elif 'job' in user_input:
        unique_jobs = ', '.join(data['job'].unique())
        response = f"The unique job titles are: {unique_jobs}."
    elif 'marital' in user_input:
        unique_marital = ', '.join(data['marital'].unique())
        response = f"The unique marital statuses are: {unique_marital}."
    elif 'education' in user_input:
        unique_education = ', '.join(data['education'].unique())
        response = f"The unique education levels are: {unique_education}."
    elif 'balance' in user_input:
        response = f"The average balance of the customers is {data['balance'].mean():.2f}."
    elif 'housing' in user_input:
        unique_housing = ', '.join(data['housing'].unique())
        response = f"The unique housing statuses are: {unique_housing}."
    elif 'loan' in user_input:
        unique_loans = ', '.join(data['loan'].unique())
        response = f"The unique loan statuses are: {unique_loans}."
    elif 'contact' in user_input:
        unique_contact = ', '.join(data['contact'].unique())
        response = f"The unique contact types are: {unique_contact}."
    elif 'day' in user_input:
        response = f"The unique contact days are: {', '.join(map(str, data['day'].unique()))}."
    elif 'month' in user_input:
        unique_months = ', '.join(data['month'].unique())
        response = f"The unique contact months are: {unique_months}."
    elif 'duration' in user_input:
        response = f"The average duration of the calls is {data['duration'].mean():.2f} seconds."
    elif 'campaign' in user_input:
        response = f"The average number of contacts during the campaign is {data['campaign'].mean():.2f}."
    elif 'pdays' in user_input:
        response = f"The average number of days since the client was last contacted from a previous campaign is {data['pdays'].mean():.2f}."
    elif 'previous' in user_input:
        response = f"The average number of contacts performed before this campaign is {data['previous'].mean():.2f}."
    elif 'poutcome' in user_input:
        unique_poutcome = ', '.join(data['poutcome'].unique())
        response = f"The unique outcomes of the previous marketing campaign are: {unique_poutcome}."
    else:
        response = "I'm not sure how to respond to that. Can you ask about specific columns like age, job, marital status, education, etc.?"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
