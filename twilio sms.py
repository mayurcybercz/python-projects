from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC05a30a46569806b4adedb737b4ee156b"
# Your Auth Token from twilio.com/console
auth_token  = "65fb010522dd25cbf8edfcee22770d0e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919145262085", 
    from_="+13343709863",
    body="Hello from Python!")

print(message.sid)
