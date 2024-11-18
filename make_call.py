import os
from twilio.rest import Client

account_sid = "AC63780e42e4f538b86e6281d00f6ec38e"
auth_token = "3b14fd99dd0a12f57c7cb9da1d5b7cc7"
client = Client(account_sid, auth_token)

with open("numbers.txt", "r") as file:
    numbers = file.read().splitlines()

for number in numbers:
    try:
        call = client.calls.create(
            from_="+13479605682",
            to=number.strip(),
            url="https://handler.twilio.com/twiml/EH7158f3e4b2766aa9af39d4b811e2d67e"
        )
        print(f"Call initiated to {number}: SID {call.sid}")
    except Exception as e:
        print(f"Failed to call {number}: {e}")