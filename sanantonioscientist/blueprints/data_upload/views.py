from flask import Blueprint, flash, render_template, redirect, request, url_for

from .forms import UploadForm

data_upload = Blueprint(
    'data_upload',
    __name__,
    template_folder='templates'
)


# TODO: use Flask-Uploads package
@data_upload.route('/data_upload', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if form.validate_on_submit():
        flash("Thanks for submitting data")
        if request.files:
            dataset = request.files['dataset']
            print(dataset)
        return redirect(url_for('data_upload.index'))
    return render_template('data_upload/index.html', form=form)
