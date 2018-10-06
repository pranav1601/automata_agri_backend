from flask import Flask, jsonify, Response, request
import sys, os
sys.path.insert(0, './addon')
sys.path.insert(0, './config')
import getCondition
app = Flask(__name__)

@app.route('/',methods=['post','get'])
def index():
    return jsonify(getCondition.exec(12.975358300000002,79.1604862))

# print(getCondition.exec(12.975358300000002,79.1604862))

debug=False
if('HEROKU' not in os.environ):
    debug=True

if __name__ == '__main__':
    app.run(debug=debug)
