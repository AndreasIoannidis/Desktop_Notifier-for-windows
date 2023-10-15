from plyer import notification


notification_title="AMD SECURITY NOTIFICATION"
notification_message = "Your AMD GPU has been detected as compromised. Please contact your IT"
icon_path = "amd.ico"

notification.notify(
    title = notification_title,
    message =notification_message,
    app_icon = icon_path ,
    timeout = 10,
    toast =False
)