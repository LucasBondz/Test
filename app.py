from flask import Flask, render_template, request
from datetime import datetime, date

def days_to_birthday(dob):
    today = date.today()
    dob = datetime.strptime(dob, "%Y-%m-%d").date()
    next_birthday = date(today.year, dob.month, dob.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)
    return (next_birthday - today).days

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        age = calculate_age(dob)
        zodiac = get_zodiac_sign(dob)
        days_to_bday = days_to_birthday(dob)
        message = f"Welcome, {name}! You are {age} years old. Your zodiac sign is {zodiac}. There are {days_to_bday} days until your next birthday!"
        return render_template('result.html', message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)