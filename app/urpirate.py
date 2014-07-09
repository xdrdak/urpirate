import cv
import os
from flask import Flask, request, g, redirect, url_for, abort, render_template, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './pirates'
ALLOWED_EXTENSIONS = set(['bmp','png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def hello():
 return render_template('helloworld.html')

@app.route("/becomepirate", methods=['POST'])
def becomePirate():
 file = request.files['file']
 if file and allowed_file(file.filename):
  filename = secure_filename(file.filename)
  file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
   #return redirect(url_for('/'))
 return render_template('helloworld.html')
   



if __name__ == "__main__":
 app.run(debug=True)
