from pypdf import PdfReader
import os
from bardapi import Bard
from dotenv import load_dotenv, find_dotenv
import time

load_dotenv(find_dotenv())
BARD_API = os.environ.get("BARD_API")
os.environ['_BARD_API_KEY']=BARD_API

pdfFileobject=open("./files/THE_CONSTITUTION_OF_INDIA.pdf", 'rb')
PdfReader = PdfReader(pdfFileobject)
text=[]
summary=' '
# Storing The Pages in  a list
for i in range(0, len(PdfReader.pages)):
    # creating a page object
    pageObj = PdfReader.pages[i].extract_text()
    pageObj = pageObj.replace('\t\r','')
    pageObj = pageObj.replace('\xa0','')
    text.append(pageObj)

# Merge multiple page - to reduce API Call
def join_elements(list, chars_per_element):
    new_list=[]
    for i in range(0, len(list), chars_per_element): 
        new_list.append(''.join(list[i:i+chars_per_element]))
    return new_list
new_text = join_elements(text,5)

print(f"Original Pages = {len(text)}")
print(f"Compressed Pages = {len(new_text)}")

def get_completion(prompt):
    response = Bard().get_answer(prompt)['content']
    return response

for i in range(len(new_text)):
    prompt =f"""
        your task is to act a Text Summariser.
        I'll give you text from pages of a book from beginning to end.
        And your job is to summarise text from these pages in less than 100 words.
        Don't be conversational. I need a plain 100 word answare.
        Text is shared below, delimited with triple backticks:
        ```{text[i]}```
        """
    
    try:
        response = get_completion(prompt)
    except:
        response = get_completion(prompt)

    print(response)

