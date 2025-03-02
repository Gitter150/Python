# AUTOCORRECT SOFTWARE WITH PYTHON #
import requests
import json
import os
os.system('cls')
prompt = input("Enter the sentence to be corrected!\n")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
headers = {"Content-Type": "application/json"}
data =  {
            "contents": 
                    [{
                        "parts":[{"text": f'Correct the typo: "{prompt}", return a single straightforward autocorrected string without any filler statements'}]
                    }]
        }
response = requests.post(url, headers=headers, json = data).json()
#print(json.dumps(response, indent=4))
response_text = response["candidates"][0]["content"]["parts"][0]["text"]
promptTokenCount = response["usageMetadata"]["promptTokenCount"]
candidatesTokenCount = response["usageMetadata"]["candidatesTokenCount"]
totalTokenCount = response["usageMetadata"]["totalTokenCount"]
print(f"Corrected sentence is\n{response_text.replace("\n","")}")
print(f"Candidate tokens used: {candidatesTokenCount}\nPrompt tokens used: {promptTokenCount}")
print(f"Total tokens used: {totalTokenCount}")





