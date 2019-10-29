import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAFoxiKo7R8BAEzmTgEiN48dMGaYOTmHaILBoZCoCA4GlQ9z3hTLEo7yXH6tXIACQliF3KHtzDu7523M1ZBVH3XO4t9xFx5iUM0DpIqdS4ZA5LvwSdQNAmSoXrnpKTVhGYVZCmSm7v2TOZAYZADiTc2SRsIlSMm5sJqKHl80ZA6dGoslPYLXK7g'
VERIFY_TOKEN = 'AGUACLARA'
bot = Bot(ACCESS_TOKEN)

# Receive messages that Facebook sends our bot at this endpoint
@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        print("method is GET")
        """Before allowing people to message the bot, Facebook has implemented a
        verify token that confirms all requests that the bot receieves came
        from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not GET, it must be POST and we can send a message back
    else:
        output = request.get_json()
        print("hi")
        for event in output['entry']:
            print("event")
            messaging = event['messaging']
            for message in messaging:
                print("messaging")
                if message.get('message'):
                    print("getting ID")
                    #FB Messenger ID of the recipient
                    recipient_id = message['sender']['id']
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# chooses a random message to send to the user
def get_message():
    sample_responses = ["Water is a fundamental human right", "I'm thirsty",
                        "Please upload your data", "No puedo hablar español",
                        "Monroe's favorite food is rice and beans"]
    return random.choice(sample_responses)

# uses PyMessenger to send response
    bot.send_text_message(recipient_id, response)
    return "success"

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
