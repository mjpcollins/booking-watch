from twilio.rest import Client


class Alert:

    def __init__(self, auth_token, account_sid, phone_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(self.account_sid, auth_token)
        self.number = phone_number

    def send_alert(self, message, messaging_service_sid):
        message = self.client.messages.create(
            messaging_service_sid=messaging_service_sid,
            body=message,
            to=self.number
        )
        return message
