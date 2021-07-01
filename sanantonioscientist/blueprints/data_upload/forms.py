from flask_wtf import Form
from wtforms import FileField, TextAreaField
from wtforms.validators import DataRequired, Length


class UploadForm(Form):
    """Upload form class for storing file upload objects """
    dataset = FileField(
        u'Dataset File',
        [DataRequired()]
    )
    description = TextAreaField(
        "Can you provide a brief problem description?",
        [DataRequired(), Length(1, 8192)]
    )
