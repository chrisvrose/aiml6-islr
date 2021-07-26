from flask import Flask, flash, request, redirect, url_for
import numpy
import cv2
from inference_check import inference
import base64
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000
@app.route("/test")
def hello_world():
    return {
        'test':'Hello world'
    }

@app.route('/uploadpost',methods=['POST'])
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


@app.route('/upload',methods=['POST'])
def upload2():
    file = request.json.get('file')
    if file is None:
        return {'ok':False,'error':False}
    # uploaded_file = request.files['file']
    try:
    #read image file string data
        filestr = base64.b64decode( file)
        print('decoded')
        #convert string data to numpy array
        npimg = numpy.fromstring(filestr, numpy.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        ans = inference(img)
        return {'ok':True,'res':inference(img)}
    except Exception as e:
        print(e);
        return {'ok':False,'error':True}

@app.route('/upload',methods=['GET'])
def form():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post id='a' enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <script>
    function arrayBufferToBase64( buffer ) {
        var binary = '';
        var bytes = new Uint8Array( buffer );
        var len = bytes.byteLength;
        for (var i = 0; i < len; i++) {
            binary += String.fromCharCode( bytes[ i ] );
        }
        return window.btoa( binary );
    }
    document.getElementById('a').addEventListener('submit',(e)=>{
        e.preventDefault();
        console.log(e);
        if(e.target.file.files.length===0) {alert('no files');return;}
        const file = e.target.file.files[0];
        const reader = new FileReader();

        reader.readAsArrayBuffer(file);
        reader.onload=((k)=>{
        console.log('k')
        document.vax = arrayBufferToBase64(reader.result);
            
        })
        reader.onerror = ((k)=>{console.log(k);alert('Error loading file!')})
    })
    </script>
    '''