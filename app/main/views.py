# -*- coding: utf-8 -*-
from app.main import main
from flask import render_template, redirect, request, url_for, flash
from ..models import Plugin, StuInfo
from .forms import QueryForm


@main.route('/', methods=['GET', 'POST'])
def index():
    plugin = Plugin.query.all()
    form = QueryForm()
    if request.method == 'POST':
        stuinfo = StuInfo.query.filter_by(stu_name=request.form['name'], number=form.number.data).first()
        if stuinfo:
            stuinfo_id = stuinfo.id
            flash(u'查询成功!', 'success')
            return redirect(url_for('admin.show_stuinfo', id=stuinfo_id))
        else:
            flash(u'查询失败，请检查姓名或学号！', 'danger')

    return render_template('index.html', form=form, plugin=plugin)
