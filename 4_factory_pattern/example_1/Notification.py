from NotificationInterface import Notification

class Email(Notification):

    def send(self):
        print("Sending email")

class SMS(Notification):

    def send(self):
        print("Sending SMS")

class WhatsApp(Notification):

    def send(self):
        print("Sending WhatsApp")