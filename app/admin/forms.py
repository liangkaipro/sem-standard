# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import PasswordField, StringField, TextAreaField, \
    SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo


class ChangePasswordForm(Form):
    old_password = PasswordField(u'旧密码', validators=[DataRequired()])
    password = PasswordField(u'新密码', validators=[
        DataRequired(), EqualTo('repassword', message=u'两次密码不一致！')])
    repassword = PasswordField(u'确认新密码！', validators=[DataRequired()])


class PluginForm(Form):
    title = StringField(u'标题', validators=[DataRequired()])
    content = TextAreaField(u'内容', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class StuinfoForm(Form):
    number = StringField(u'学号', validators=[DataRequired()])
    name = StringField(u'姓名', validators=[DataRequired()])
    grade = StringField(u'年级', validators=[DataRequired()])
    cla = StringField(u'班级', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class AssessForm(Form):
    term = SelectField(u'学期', validators=[DataRequired()],
                       choices=[('第一学年上学期', '第一学年上学期'), ('第一学年下学期', '第一学年下学期'),
                                ('第二学年上学期', '第二学年上学期'), ('第二学年下学期', '第二学年下学期'),
                                ('第三学年上学期', '第三学年上学期'), ('第三学年下学期', '第三学年下学期'),
                                ('第四学年上学期', '第四学年上学期'), ('第四学年下学期', '第四学年下学期'),
                                ('第五学年上学期', '第五学年上学期'), ('第五学年下学期', '第五学年下学期'),
                                ('第六学年上学期', '第六学年上学期'), ('第六学年下学期', '第六学年下学期')])
    duty = SelectField(u'责任与担当', validators=[DataRequired()],
                       choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    study = SelectField(u'学习与探究', validators=[DataRequired()],
                        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    health = SelectField(u'健康与生存', validators=[DataRequired()],
                         choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    taste = SelectField(u'审美与人文', validators=[DataRequired()],
                        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    practice = SelectField(u'实践与创新', validators=[DataRequired()],
                           choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    personality = SelectField(u'个性与发展', validators=[DataRequired()],
                              choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    comment = TextAreaField(u'老师评语', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class ManageStuForm(Form):
    grade = StringField(u'年级', validators=[DataRequired()])
    cla = StringField(u'班级', validators=[DataRequired()])
    submit = SubmitField(u'查询')
