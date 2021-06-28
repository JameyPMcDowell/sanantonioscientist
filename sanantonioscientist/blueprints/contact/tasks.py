from lib.flask_mailplus import send_template_message
from sanantonioscientist.app import create_celery_app

celery = create_celery_app()


@celery.task()
def deliver_contact_email(email, message):
    """
    Send a contact e-mail.

    Parameters
    ----------
    email : str
        E-mail address of the visitor
    message : str
        E-mail message

    Returns
    -------
    None
    """
    ctx = {'email': email, 'message': message}

    send_template_message(subject='[San Antonio Scientist] Contact',
                          sender=email,
                          recipients=[celery.conf.get('MAIL_USERNAME')],
                          reply_to=email,
                          template='contact/mail/index',
                          ctx=ctx)

    return None
