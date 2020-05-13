from flaskr import create_celery_app
from flaskr.extensions import mail

celery = create_celery_app()


@celery.task
def add(x, y):
    return x + y


@celery.task
def mul(x, y):
    return x * y


@celery.task
def xsum(numbers):
    return sum(numbers)

@celery.task
def send_some_mail():
    mail.send_message("hello friend",
                #   subject="New form submission",
                #   body="Hi",
                  sender="form@flaskr.com",
                  recipients=['sean.connery543@gmail.com'])
    print('sent mail')

# @celery.task
# def deliver_contact_email(email, message):
#     """
#     Send a contact e-mail.

#     :param email: E-mail address of the visitor
#     :type user_id: str
#     :param message: E-mail message
#     :type user_id: str
#     :return: None
#     """
#     ctx = {'email': email, 'message': message}

#     send_template_message(subject='[Snake Eyes] Contact',
#                           sender=email,
#                           recipients=[celery.conf.get('MAIL_USERNAME')],
#                           reply_to=email,
#                           template='contact/mail/index', ctx=ctx)

#     return None
