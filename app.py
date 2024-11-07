from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]
        print(f"First Name: {first_name} \nLast Name: {last_name} \nEmail: {email} \nDate: {date} \nOccupation: {occupation}")

    return render_template('index.html')


app.run(debug=True, port=5001)