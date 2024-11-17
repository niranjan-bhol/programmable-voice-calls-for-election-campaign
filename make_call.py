import os
from twilio.rest import Client

# Twilio credentials
account_sid = "AC63780e42e4f538b86e6281d00f6ec38e"
auth_token = "3b14fd99dd0a12f57c7cb9da1d5b7cc7"
client = Client(account_sid, auth_token)

# Read numbers from numbers.txt
with open("numbers.txt", "r") as file:
    numbers = file.read().splitlines()

# Iterate through numbers and make calls
for number in numbers:
    try:
        call = client.calls.create(
            from_="+13479605682",
            to=number.strip(),  # Remove any extra spaces
            url="https://handler.twilio.com/twiml/EH7a4345c1f4b2402da4f3de813d4b9037"  # TwiML URL for the call
        )
        print(f"Call initiated to {number}: SID {call.sid}")
    except Exception as e:
        print(f"Failed to call {number}: {e}")