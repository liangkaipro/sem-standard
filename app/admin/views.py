# -*- coding: utf-8 -*-
from flask import render_template, flash, url_for, redirect, request
from . import admin
from flask_login import login_required, current_user
from .forms import ChangePasswordForm, PluginForm, StuinfoForm, AssessForm, ManageStuForm
from .. import db
from ..models import Plugin, StuInfo, Assess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@admin.route('/')
@login_required
def index():
    form = ChangePasswordForm()
    return render_template('admin/admin.html', form=form)


@admin.route('/add-stuinfo', methods=['GET', 'POST'])
@login_required
def add_stuinfo():
    form = StuinfoForm()
    if request.method == 'GET':
        return render_template('admin/add-stuinfo.html', form=form)
    else:
        if form.validate_on_submit():
            stu_number = form.number.data
            stuinfo = StuInfo.query.filter_by(number=stu_number).first()
            if stuinfo:
                form = StuinfoForm(number=stu_number, name=form.name.data, grade=form.grade.data, cla=form.cla.data)
                flash(u'请检查学号！', 'danger')
                return render_template('admin/add-stuinfo.html', form=form)
            else:
                name = form.name.data
                grade = form.grade.data
                cla = form.cla.data
                stuinfo = StuInfo(number=stu_number, stu_name=name, grade=grade, cla=cla)
                db.session.add(stuinfo)
                db.session.commit()
                flash(u'添加学生成功！', 'success')
                stuinfo_id = StuInfo.query.filter_by(number=form.number.data).first().id
            return redirect(url_for('.show_stuinfo', id=stuinfo_id))
        return redirect(url_for('.add_stuinfo'))


@admin.route('/edit-stuinfo/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_stuinfo(id):
    stuinfo = StuInfo.query.get_or_404(id)
    form = StuinfoForm()
    if form.validate_on_submit():
        stuinfo.number = form.number.data
        stuinfo.stu_name = form.name.data
        stuinfo.grade = form.grade.data
        stuinfo.cla = form.cla.data
        db.session.add(stuinfo)
        db.session.commit()
        flash(u'学生信息更新成功！', 'success')
        return redirect(url_for('.show_stuinfo', id=stuinfo.id))
    form.number.data = stuinfo.number
    form.name.data = stuinfo.stu_name
    form.grade.data = stuinfo.grade
    form.cla.data = stuinfo.cla
    return render_template('admin/add-stuinfo.html', form=form)


@admin.route('/manage-stuinfo', methods=['GET', 'POST'])
@login_required
def manage_stuinfo():
    form = ManageStuForm()
    if form.validate_on_submit():
            stuinfo = StuInfo.query.filter_by(grade=request.form['grade'], cla=form.cla.data).all()
            return render_template('admin/manage-stu.html', form=form, stuinfo=stuinfo)
    return render_template('admin/manage-stu.html', form=form)


@admin.route('/delete-stuinfo/<int:id>')
@login_required
def delete_stuinfo(id):
    stuinfo = StuInfo.query.filter_by(id=id).first()
    db.session.delete(stuinfo)
    db.session.commit()
    flash(u'成功删除此学生信息', 'success')
    return redirect(url_for('.manage_stuinfo'))


@admin.route('/show-stuinfo/<int:id>', methods=['GET', 'POST'])
def show_stuinfo(id):
    form = AssessForm()
    stuinfo_id = id
    if request.method == 'GET':
        stuinfo = StuInfo.query.get_or_404(id)
        plugin = Plugin.query.all()
        assess = Assess.query.filter_by(stuinfo_id=id).all()
        return render_template('show-stuinfo.html', form=form, stuinfo=stuinfo, plugin=plugin, assess=assess)
    else:
        if form.validate_on_submit():
            assess = Assess(stuinfo_id, form.term.data, form.duty.data,
                            form.study.data, form.health.data,
                            form.taste.data, form.practice.data,
                            form.personality.data, form.comment.data)
            db.session.add(assess)
            db.session.commit()
            flash(u'添加评价成功！', 'success')
        else:
            flash(u'添加评价失败！', 'danger')
        return redirect(url_for('.show_stuinfo', id=id))


@admin.route('/delete-assess/<int:id>')
@login_required
def delete_assess(id):
    assess = Assess.query.filter_by(id=id).first_or_404()
    stuinfo_id = Assess.query.filter_by(id=id).first().stuinfo_id
    db.session.delete(assess)
    db.session.commit()
    flash(u'删除已成功！', 'success')
    return redirect(url_for('.show_stuinfo', id=stuinfo_id))


@admin.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        if current_user.password == form.old_password.data:
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash(u'修改密码成功！', 'success')
            return redirect(url_for('admin.index'))
        else:
            flash(u'修改密码失败！旧密码不正确！', 'danger')
    return redirect(url_for('admin.index'))


@admin.route('/plugin', methods=['GET', 'POST'])
@login_required
def show_plugin():
    form = PluginForm()
    if request.method == 'GET':
        plugin = Plugin.query.all()
        return render_template('admin/plugin.html', plugin=plugin, form=form)
    else:
        if form.validate_on_submit():
            plugin = Plugin(current_user.id, form.title.data, form.content.data)
            db.session.add(plugin)
            db.session.commit()
            flash(u'成功添加公告！', 'success')
        else:
            flash(u'添加失败！', 'danger')
        return redirect(url_for('.show_plugin'))


@admin.route('/delete-plugin/<int:id>')
@login_required
def delete_plugin(id):
    plugin = Plugin.query.filter_by(id=id).first_or_404()
    db.session.delete(plugin)
    db.session.commit()
    flash(u'成功删除公告！', 'success')
    return redirect(url_for('.show_plugin'))
