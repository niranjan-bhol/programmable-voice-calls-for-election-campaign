import os
from twilio.rest import Client

account_sid = "AC63780e42e4f538b86e6281d00f6ec38e"
auth_token = "3b14fd99dd0a12f57c7cb9da1d5b7cc7"
client = Client(account_sid, auth_token)

call = client.calls.create(
  from_="+13479605682",
  to="+917066002804",
  url="https://handler.twilio.com/twiml/EH7a4345c1f4b2402da4f3de813d4b9037"
)

print(call.sid)