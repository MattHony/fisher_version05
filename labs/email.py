# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/12 20:20
# @Author : '红文'
# @File : email.py
# @Software: PyCharm
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message
from app import mail

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='aaa@qq.com', body='Test',
    #               recipients=['user@qq.com'])
    msg = Message('[鱼书]'+''+subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template,**kwargs)
    thr = Thread(target=send_async_email, args=[current_app, msg])
    thr.start()
    # mail.send(msg)
