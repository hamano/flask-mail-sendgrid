# -*- coding: utf-8 -*-

"""
    flask_mail_sendgrid
    ~~~~~~~~~~~~~
    Flask extension for sendgrid. It has same interface with Flask-Mail.
    :copyright: (c) 2018 by HAMANO Tsukasa.
    :license: MIT, see LICENSE for more details.
"""

import sendgrid
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import Email
from sendgrid.helpers.mail import Content
from sendgrid.helpers.mail import Personalization
from flask_mail import Message

class MailSendGrid():
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.state = self.init_app(app)
        else:
            self.state = None

    def init_app(self, app):
        state = {}
        self.api_key = app.config['MAIL_SENDGRID_API_KEY']
        self.default_sender = app.config.get('MAIL_DEFAULT_SENDER', 'no-reply@localhost')
        self.sg = sendgrid.SendGridAPIClient(apikey=self.api_key)
        # register extension with app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['mail'] = self
        return state

    def _make_sendgrid_mail(self, message):
        mail = Mail()
        if message.sender:
            mail.from_email = Email(message.sender)
        else:
            mail.from_email = Email(self.default_sender)

        template_id = getattr(message, 'template_id', None)
        if template_id:
            mail.template_id = template_id

        if message.subject:
            mail.subject = message.subject

        if message.recipients:
            if type(message.recipients) == list:
                personalization = Personalization()
                for recipient in message.recipients:
                    personalization.add_to(Email(recipient))

                dynamic_template_data = getattr(message, 'dynamic_template_data', None)
                if dynamic_template_data:
                    personalization.dynamic_template_data = dynamic_template_data
                
                mail.add_personalization(personalization)
            else:
                raise Exception("unsupported type yet")
        if message.body:
            mail.add_content(Content("text/plain", message.body))

        if message.html:
            mail.add_content(Content("text/html", message.html))

        if message.reply_to:
            mail.reply_to = Email(message.reply_to)

        return mail

    def send(self, message):
        mail = self._make_sendgrid_mail(message)
        res = self.sg.client.mail.send.post(request_body=mail.get())
        if int(res.status_code / 100) != 2:
            raise Exception("error response from sendgrid {}".format(res.status_code))

    def __getattr__(self, name):
        return getattr(self.state, name, None)
