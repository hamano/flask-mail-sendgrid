#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='Flask-Mail-SendGrid',
    version='0.2',
    description="Flask extension for sendgrid. It has same interface with Flask-Mail.",
    long_description=long_description,
    url="http://github.com/hamano/flask-mail-sendgrid",
    author = "HAMANO Tsukasa",
    author_email = "code@cuspy.org",
    py_modules=['flask_mail_sendgrid'],
    install_requires=[
        'Flask-Mail',
        'SendGrid',
    ],
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
