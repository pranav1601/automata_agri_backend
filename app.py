from flask import Flask, jsonify, Response, request
import sys, os
sys.path.insert(0, './addon')
sys.path.insert(0, './config')
sys.path.insert(0, './prediction')
import getCondition
import devfest_0
app = Flask(__name__)

@app.route('/',methods=['post','get'])
# def index():
#     return jsonify(getCondition.exec(12.975358300000002,79.1604862))

# @app.route('/pos',methods=['post','get'])
def latlng():
    lat=request.args.get('lat')
    lng=request.args.get('lng')
    crop=request.args.get('crop')
    if(crop not in ['rice','bajra','maize']): return ''
    if(not float(lat) or not float(lng)): return ''
    return jsonify(devfest_0.enprd(crop,getCondition.exec(float(lat),float(lng))))
# print(getCondition.exec(12.975358300000002,79.1604862))

debug=False
if('HEROKU' not in os.environ):
    debug=True

if __name__ == '__main__':
    app.run(debug=debug)
