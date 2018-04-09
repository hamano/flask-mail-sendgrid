#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Flask-Mail-SendGrid
===================

Installation
````````````

.. code:: bash
    $ pip install flask-mail-sendgrid

"""

from setuptools import setup

setup(
    name='Flask-Mail-SendGrid',
    version='0.1',
    description="Flask extension for sendgrid. It has same interface with Flask-Mail.",
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
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
