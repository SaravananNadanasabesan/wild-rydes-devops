# app/main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Company Name: Wild Rydes</h1>
    <p>Developer: Saravanan Nadanasabesan</p>
    <p>Company ID: 101013057</p>
    <p>Joining Date: 2026-01-05</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
