# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(Form):
    name = StringField(u'姓名', validators=[DataRequired()])
    number = StringField(u'学号', validators=[DataRequired()])
    submit = SubmitField(u'查询')
