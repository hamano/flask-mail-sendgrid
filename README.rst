Flask-Mail-SendGrid
===================

Flask extension for sendgrid. It has same interface with Flask-Mail.

Flask-Mail-SendGrid is friendly with another extention such as
Flask-Security.

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

-  MAIL\_SENDGRID\_API\_KEY: API Key for SendGrid
-  MAIL\_DEFAULT\_SENDER: default sender

.. code:: python

    from flask import Flask
    from flask_mail_sendgrid import MailSendGrid

    app = Flask(__name__)
    app.config['MAIL_SENDGRID_API_KEY'] = 'XXXXXXXX'
    mail = MailSendGrid(app)

Sending messages
----------------

To send a message first create a Message instance:

.. code:: python

    from flask_mail import Message

    @app.route("/")
    def index():
        msg = Message("Hello",
                      sender="from@example.com",
                      recipients=["to@example.com"])

The message can contain a body and/or HTML:

.. code:: python

    msg.body = "testing"
    msg.html = "<b>testing</b>"

Or, if you are using Templates in Sendgrid, you may specify a Template ID and Data:

.. code:: python
    msg.template_id = 'my-template-id'
    msg.dynamic_template_data = {'first_name': 'John', 'last_name': 'Doe'}

Finally, to send the message, you use the Mail instance configured with
your Flask application:

.. code:: python

    mail.send(msg)
