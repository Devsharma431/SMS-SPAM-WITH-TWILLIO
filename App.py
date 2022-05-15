from twilio.rest import Client
message = input('Enter your spamming SMS : ')
yo = input("Enter your target number with country code : ")
account_sid = 'YOUR ACC SID'
auth_token = 'YOUR AUTH TOKEN'
client = Client(account_sid, auth_token)
while True:
   message = client.messages \
                  .create(
                       body=message,
                       from_='+YOUR TWILLIO NUMBER',
                       to= yo,
                   )
  
print(message.sid)
