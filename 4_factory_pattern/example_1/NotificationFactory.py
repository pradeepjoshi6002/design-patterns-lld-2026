from Notification import Email, SMS, WhatsApp

class NotificationFactory:

    @staticmethod
    def create_notification(notificationType):

        match notificationType:
            case "Email":
                return Email()
            case "SMS":
                return SMS()
            case "WhatsApp":
                return WhatsApp()
            case _:
                return ValueError("Invalid notification type")