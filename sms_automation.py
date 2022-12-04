from twilio.rest import Client

api = input("Enter your ACCOUNT SID: ")
auth = input("Enter your AUTH TOKEN: ")
from_number = input("Enter your number: ")
Type_message = input("type your message here: ")
to_number = input("Enter multiple recipient number separated by comma: ")
lists = to_number.split(",")
groupnum = []
for i in lists:
    groupnum.append(i)

account_sid = api
auth_token = auth
client = Client(account_sid, auth_token)

for i in range(len(groupnum)):
    client.messages.create(from_=from_number, body=Type_message, to=groupnum[i])
