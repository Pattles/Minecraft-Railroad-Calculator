from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

def run():
    app.run()

if __name__ == '__main__':
    run()