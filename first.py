from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Wellcome to API!'

@app.route('/Prime/<string:n>')
def prime(n):
    num = int(n)
    if num <= 1:
        return f"{num} is not a prime number."

    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return f"{num} is not a prime number."

    return f"{num} is a prime number."

    

app.run(debug=True)