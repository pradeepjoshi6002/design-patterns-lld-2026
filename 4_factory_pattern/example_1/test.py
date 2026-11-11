from NotificationFactory import NotificationFactory

notification=NotificationFactory.create_notification(notificationType="Email")

notification.send()