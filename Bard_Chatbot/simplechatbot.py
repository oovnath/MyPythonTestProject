import os
from bardapi import Bard
from dotenv import load_dotenv, find_dotenv
import time

load_dotenv(find_dotenv())
BARD_API = os.environ.get("BARD_API")
os.environ['_BARD_API_KEY']=BARD_API

input_text="How to play football?"
print(Bard().get_answer(input_text)['content'])
