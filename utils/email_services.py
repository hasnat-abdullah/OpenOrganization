from django.conf import settings
from django.core.mail import send_mail

class EMAIL:
    def __init__(self):
        self.from_email = settings.EMAIL_HOST_USER

    def send_email_service(self, name, phn, subject, message, recipient_list):
        try:
            message = f" Sender details:\n Name: {name}\n Mobile: {phn}\n Email: {recipient_list}\n\n Message: {message}"
            send_mail(subject, message, self.from_email, recipient_list)
            return True
        except Exception as ex:
            print("Faild to send sms \n")
            print(ex)

            return False