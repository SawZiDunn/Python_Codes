from flask import Flask, request, render_template

app = Flask(__name__)

REGISTERED = dict()
SPORTS = [
    'Basketball',
    'Soccer',
    'Tennis'
]


@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    sport = request.form.get('sport')

    if not name or sport not in SPORTS:
        return render_template('failure.html')

    REGISTERED[name] = sport
    return render_template('success.html')


@app.route('/registered')
def registered():
    return render_template('registered.html', registered=REGISTERED)