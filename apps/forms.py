from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,TextAreaField, validators

class CreateForm(FlaskForm):
    title = StringField('Enter Title: ',[validators.InputRequired()])
    remarks = TextAreaField('Remarks: ',[validators.InputRequired()])
    save = SubmitField('Save')

class UpdateForm(FlaskForm):
    title = StringField('Enter Title: ',[validators.InputRequired()])
    remarks = TextAreaField('Remarks: ',[validators.InputRequired()])
    update = SubmitField('Update')