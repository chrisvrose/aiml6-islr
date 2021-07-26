from flask import Flask, flash, request, redirect, url_for
import numpy
import cv2
from inference_check import inference
app = Flask(__name__)

@app.route("/test")
def hello_world():
    return {
        'test':'Hello world'
    }

@app.route('/upload',methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect('/form')
    uploaded_file = request.files['file']

    try:
    #read image file string data
        filestr = request.files['file'].read()
        #convert string data to numpy array
        npimg = numpy.fromstring(filestr, numpy.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        ans = inference(img)
        return {'ok':True,'res':inference(img)}
    except Exception:
        return {'ok':False}



@app.route('/upload',methods=['GET'])
def form():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''