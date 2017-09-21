# -*- coding: utf-8 -*-
from flask import render_template, url_for, flash, request, redirect
from flask_login import login_user, login_required, logout_user
from app.auth import auth
from app.models import User
from app.auth.forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            login_user(user)
            flash(u'登陆成功!', 'success')
            return redirect(url_for('admin.index'))
        else:
            flash(u'登陆失败,请检查用户名或密码！', 'danger')
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已退出登陆！', 'success')
    return redirect(url_for('main.index'))
