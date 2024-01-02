from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/test')
def test():
    return '<html><body><h1>Dies ist ein Test!</h1></body></html>'

if __name__ == '__main__':
    app.run()
