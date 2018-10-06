from flask import Flask, jsonify, Response, request
app = Flask(__name__)

@app.route('/',methods=['post','get'])
def index():
    return 'Server is running'

if __name__ == '__main__':
    app.run(debug=True)
