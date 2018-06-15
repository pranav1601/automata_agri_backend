from flask import Flask, jsonify, Response, request
from preproc_beta import preproc
from TT_SLOT import slot
import string
import random
import os
app = Flask(__name__)

UPLOAD_FOLDER = './tmp/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=['post','get'])
def index():
    return '<form action="/upload" method="post" enctype="multipart/form-data"><input type="file" name="file" /><input type="submit"></form>'


@app.route('/upload',methods=['post','get'])
def upload_file():
    try:
        name=''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        f = request.files['file']
        f.save('./tmp/'+name+'.png')
        preproc('./tmp/'+name+'.png')
        value=slot('./tmp/'+name+'.png')
        os.remove('./tmp/'+name+'.png')
        return jsonify(value)
    except:
        return jsonify({'err': 'Bad Request'})



if __name__ == '__main__':
    app.run(debug=True)
