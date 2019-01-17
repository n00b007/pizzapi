from twilio.rest import Client

# setting up the auth
account = "AC3547c4a4a87da54f6998d4a25bda063751" # random token
auth_token = "8a2fbe9744c3das72667e9421d4ff3e0a04" # random auth token

client = Client(account, auth_token)

def send_message(client=client, message=None):
    message = client.messages.create(to="+122241244", from_="+1421341445", body = message)


