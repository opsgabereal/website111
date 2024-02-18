from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
