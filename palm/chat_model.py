'''
Using PaLM2 api key Chat bot demo.

Here I using:
    1) prompt
    2) examples
    3) temperature
    4) context

reference {
    https://www.youtube.com/@jiejenn/videos, 
    https://developers.generativeai.google/api/python/google/generativeai/chat_async
    https://github.com/google/generative-ai-python/blob/v0.1.0/google/generativeai/client.py
            }
'''
import os
import google.generativeai as palm
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
PaLM_KEY = os.environ.get("PaLM_KEY")
palm.configure(api_key=PaLM_KEY)

examples=[
    ('Hello', 'Hi there mr. How can I be assistant'),
    ('I want to make a lot of money', 'You should work hard like your parents')
]
prompt ='I need help with a job interview for a data analyst job. Can youhelp me?'
response = palm.chat(messages=prompt, temperature=0.2 ,context='Speak like a CEO', examples=examples)
# msg_print= response.messages
# print(msg_print)
for message in response.messages:
    print(message['author'], message['content'])

while True:
    s = input()
    # response=response.reply('Can you provide me with additional detail')
    response=response.reply(s)
    print(response.last)

