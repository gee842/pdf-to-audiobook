# save_text = 1

import PyPDF2 
import textract
import tts
import sys
from google.cloud import texttospeech
import json


# Source: https://betterprogramming.pub/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f

def pdf_to_text(filepath,save_text=True,save_path='./newconverted.txt'):
    pdfFileObj = open(filepath,'rb')

    print("Using textract instead")
    text = textract.process(filepath, method='tesseract', language='eng')
    decoded = text.decode('utf-8','ignore').replace('\n', ' ')
    list_of_unwanted = ['.','-','+','+','=','©', '©', '¢']
    for i in list_of_unwanted:
        decoded = decoded.replace(i,'')
    if save_text:
        saved_file = open(save_path,'w')
        saved_file.write(decoded)
        saved_file.close()
        
    pdfFileObj.close()
    return decoded

if __name__ == "__main__":
    #'./samples/wagelabor.pdf'
    filepath_of_saved = sys.argv[2]
    text = pdf_to_text(sys.argv[1])

    quota_path = './quota.txt'
    truncated_text = text[1:1000] #CHANGE THIS TO BLOW THROUGH YOUR FREE LIMITS
    tts.comment_to_mp3(truncated_text,quota_path,f'part1',voice="en-GB-Wavenet-B")

