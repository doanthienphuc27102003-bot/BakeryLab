from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)
    return "OK"

app.run(host="0.0.0.0", port=8080)
