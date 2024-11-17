#curl -X POST "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Calls.json" \
#--data-urlencode "From=+15558675310" \
#--data-urlencode "To=+15017122661" \
#--data-urlencode "Url=http://demo.twilio.com/docs/voice.xml" \
#-u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN

#curl -X POST https://api.twilio.com/2010-04-01/Accounts/AC63780e42e4f538b86e6281d00f6ec38e/Calls.json \
#  --data-urlencode "Url=http://demo.twilio.com/docs/voice.xml" \
#  --data-urlencode "To=+917066002804" \
#  --data-urlencode "From=+13479605682" \
#  -u AC63780e42e4f538b86e6281d00f6ec38e:$TWILIO_AUTH_TOKEN

curl -X POST https://api.twilio.com/2010-04-01/Accounts/AC63780e42e4f538b86e6281d00f6ec38e/Calls.json \
  --data-urlencode "Url=http://demo.twilio.com/docs/voice.xml" \
  --data-urlencode "To=+917066002804" \
  --data-urlencode "From=+13479605682" \
  -u AC63780e42e4f538b86e6281d00f6ec38e:3b14fd99dd0a12f57c7cb9da1d5b7cc7