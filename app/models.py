# -*- coding: utf-8 -*-
from flask_login import UserMixin
from app import db, login_manager


# 管理员用户表
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 学生信息表
class StuInfo(db.Model):
    __tablename__ = 'stu_info'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64), unique=True)
    stu_name = db.Column(db.String(64), nullable=True)
    grade = db.Column(db.String(64), nullable=True)
    cla = db.Column(db.String(64), nullable=True)

    def __init__(self, number, stu_name, grade, cla):
        self.number = number
        self.stu_name = stu_name
        self.grade = grade
        self.cla = cla


# 公告表
class Plugin(db.Model):
    __tablename__ = 'plugin'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(64), unique=True)
    content = db.Column(db.Text, default='')

    def __init__(self, user_id, title, content):
        self.user_id = user_id
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Plugin %r>' % self.title


# 评价信息表
class Assess(db.Model):
    __tablename__ = 'assess'
    id = db.Column(db.Integer, primary_key=True)
    stuinfo_id = db.Column(db.Integer, nullable=True)
    term = db.Column(db.String(64), nullable=True)
    duty = db.Column(db.String(64), nullable=True)  # 责任与担当
    study = db.Column(db.String(64), nullable=True)  # 学习与探究
    health = db.Column(db.String(64), nullable=True)  # 健康与生存
    taste = db.Column(db.String(64), nullable=True)  # 审美与人文
    practice = db.Column(db.String(64), nullable=True)  # 实践与创新
    personality = db.Column(db.String(64), nullable=True)  # 个性与发展
    comment = db.Column(db.Text, unique=True)  # 评价

    def __init__(self, stuinfo_id, term, duty, study, health, taste, practice, personality, comment):
        self.stuinfo_id = stuinfo_id
        self.term = term
        self.duty = duty
        self.study = study
        self.health = health
        self.taste = taste
        self.practice = practice
        self.personality = personality
        self.comment = comment



