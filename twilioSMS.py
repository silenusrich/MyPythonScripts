from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9df997e2a86553d0c7275fc45444d87e"
# Your Auth Token from twilio.com/console
auth_token  = "6c8bf08ba5262029810ce17b049b8abc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19292240566", 
    from_="+12522106826",
    body="Hello from Python!")

print(message.sid)
