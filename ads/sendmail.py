# ads/sendmail1.py

from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message, recipient_list):
    """
    Function to send an email using Django's send_mail function.
    
    Args:
    subject (str): The subject of the email.
    message (str): The message body of the email.
    recipient_list (list): A list of recipient email addresses.
    
    Returns:
    int: The number of successfully delivered messages.
    """
    return send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # Sender's email address
        recipient_list,
        fail_silently=False,
    )