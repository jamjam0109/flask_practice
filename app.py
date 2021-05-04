import model 
from utils import file_rename
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES


app = Flask(__name__)
 
app.config['SECRET_KEY'] = 'hardsecretkey'

photos = UploadSet('photos', IMAGES)
 
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
 
configure_uploads(app, photos)
 
@app.route('/', methods=['GET', 'POST'])
@app.route('/output', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        
        try:
            filename = photos.save(request.files['photo'])
            filename = app.config['UPLOADED_PHOTOS_DEST'] + '/' + filename
        except: 
            return render_template('index.html')
        
        new_filename = file_rename(filename)
        model_output = model.main(new_filename)
 
        return render_template(
            'output.html',
            title='output', 
            filename=new_filename, 
            model_output=model_output
            )
 
    return render_template('index.html')
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=40001)