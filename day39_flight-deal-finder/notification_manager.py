from twilio.rest import Client
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        # Twilio account info
        account_sid = os.environ["ACCT_SID"]
        auth_token = os.environ["AUTH_TOKEN"]

        self.client = Client(account_sid, auth_token)

    def send_notification(self, text):
        message = self.client.messages.create(
            body=text,
            from_="+16674010418",  # purchased/trial phone number from Twilio
            to="+1xxxxxxxxxx"
            # verified number with Twilio, in this case it is the phone number used via the registration.
        )
        print(message.status)
