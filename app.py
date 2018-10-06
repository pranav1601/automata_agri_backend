from flask import Flask, jsonify, Response, request
import sys, os
sys.path.insert(0, './addon')
import getCondition
app = Flask(__name__)

@app.route('/',methods=['post','get'])
def index():
    return 'Server is running'
print(getCondition.exec(12.975358300000002,79.1604862))

debug=False
if('HEROKU' not in os.environ):
    debug=True

if __name__ == '__main__':
    app.run(debug=debug)
