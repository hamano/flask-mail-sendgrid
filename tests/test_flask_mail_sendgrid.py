import unittest

from flask_mail import Message
from sendgrid.helpers.mail import Mail
from flask_mail_sendgrid import MailSendGrid


class TestMailSendGrid(unittest.TestCase):

    def test__make_sendgrid_mail(self):
        msg = Message(
            'hi',
            sender='google@gmail.com',
            recipients=['google@gmail.com'],
            body='hi all!!!',
            mail_options={'from_name': 'Anyone'}
        )
        mail = MailSendGrid()._make_sendgrid_mail(msg)
        self.assertTrue(isinstance(mail, Mail))
        mail_get = mail.get()
        self.assertTrue(isinstance(mail_get, dict))
        self.assertEqual(mail_get['from']['email'], msg.sender)
        self.assertEqual(mail_get['from']['name'], msg.mail_options['from_name'])
        self.assertEqual(mail_get['personalizations'][0]['to'][0]['email'], msg.recipients[0])
        self.assertEqual(mail_get['content'][0]['value'], msg.body)
        self.assertEqual(mail_get['subject'], msg.subject)
