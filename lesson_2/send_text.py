from twilio.rest import TwilioRestClient

# Your Account SID and Auth Token from twilio.com/user/account
account_sid = "ACa05c4d9f994cbebd03c969d2557602b9"
auth_token = "57dafc0da7ec348200ee3cce3f2172ec"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body="Test of Twilio",
                                     to="+13062701879",
                                     from_="+14155992671")
print message.sid
