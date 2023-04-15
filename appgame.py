from flask import Flask, render_template, request

app = Flask(__name__)

connected_users = set()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    if len(connected_users) < 4:
        username = request.form['username']
        connected_users.add(username)
        return "You are now connected as " + username
    else:
        return "Sorry, maximum number of connections reached."

if __name__ == '__main__':
    app.run(debug=True)
