Flask-Mail-SendGrid
===================

# Installing Flask-Mail-SendGrid

Install with pypi:

~~~
$ pip install flask-mail-sendgrid
~~~

or install latest version:

~~~
$ git clone https://github.com/hamano/flask-mail-sendgrid.git
$ cd flask-mail-sendgrid
$ python setup.py install
~~~

# Configuring Flask-Mail-SendGrid

* SENDGRID_API_KEY: API Key for SendGrid
* MAIL_DEFAULT_SENDER: default sender

# Usage

~~~
from flask_mail_sendgrid import MailSendGrid
mail = MailSendGrid(app)

msg = Message("Subject",
              sender="from@example.com",
              recipients=["to@example.com"])
~~~

The message can contain a body and/or HTML:

~~~
msg.body = "testing"
msg.html = "<b>testing</b>"
~~~

Finally, to send the message, you use the Mail instance configured with your Flask application:

~~~
mail.send(msg)
~~~
