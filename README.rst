Flask-Mail-SendGrid
===================

Flask extension for sendgrid. It has same interface with Flask-Mail.

Flask-Mail-SendGrid is friendly with another extention such as Flask-Security.

Installing Flask-Mail-SendGrid
------------------------------

Install with pypi:

.. code:: bash

    $ pip install flask-mail-sendgrid

or install latest version:

.. code:: bash

    $ git clone https://github.com/hamano/flask-mail-sendgrid.git
    $ cd flask-mail-sendgrid
    $ python setup.py install

Configuring Flask-Mail-SendGrid
-------------------------------

-  SENDGRID\_API\_KEY: API Key for SendGrid
-  MAIL\_DEFAULT\_SENDER: default sender

Usage
-----

.. code:: python

    from flask import Flask
    from flask_mail_sendgrid import MailSendGrid
    from flask_mail import Message

    app = Flask(__name__)
    mail = MailSendGrid(app)
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["to@example.com"])

The message can contain a body and/or HTML:

.. code:: python

    msg.body = "testing"
    msg.html = "<b>testing</b>"

Finally, to send the message, you use the Mail instance configured with
your Flask application:

.. code:: python

    mail.send(msg)


