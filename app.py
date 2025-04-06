from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask App on Azure!"

@app.route('/xss')
def xss():
    q = request.args.get('q', '')
    return f"XSS Test Received: {q}"

@app.route('/sqli')
def sqli():
    id_val = request.args.get('id', '')
    return f"SQLi Test Received: {id_val}"

if __name__ == '__main__':
    app.run()
