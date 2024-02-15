from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            filename = secure_filename(f.filename)
            f.save(filename)
            return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
