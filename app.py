from flask import Flask, jsonify, Response, request
from preproc_beta import preproc
from TT_SLOT import slot
import os
app = Flask(__name__)
#
#
# a={'a':'b'}
# @app.route('/',methods=['post','get'])
# def index():
#     # resp = Response('{\"a\":"b"}')
#     # resp.headers['content-type'] = 'application/json'
#     # # return ("{\"as\":\"fg\"}", 400)
#     # # return jsonify(a)
#     res=Response("Hey")
#     res.set_cookie("name", value="I am cookie")
#     # return jsonify({'form':request.form,'args':request.args,'cookie':request.cookies})
#     return res
#
# app.run(port=3000)

# proc('C:\\Users\\shubh\\Desktop\\Shubham-IT2.png')
UPLOAD_FOLDER = './tmp/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=['post','get'])
def index():
    return '<form action="/upload" method="post" enctype="multipart/form-data"><input type="file" name="file" /><input type="submit"></form>'


@app.route('/upload',methods=['post','get'])
def upload_file():
    f = request.files['file']
    f.save('./tmp/image.png')
    preproc('./tmp/image.png')
    return(slot())
    return "as"


if __name__ == '__main__':
    app.run(debug=True)
