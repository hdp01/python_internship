import requests
import json

def summarize_text(text, api_key):

    url = "https://api.edenai.run/v2/text/summarize"

    payload = {
        "providers": "microsoft,connexun",
        "language": "en",
        "text": text
    }

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, json=payload, headers=headers)

    summary = json.loads(response.text)['microsoft']['result']

    return summary

text = input("Enter the text to summarize: ")

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiY2Y0N2FmYWUtNTk5NS00NmNmLTkzZTMtMzEwOTMyN2JmZDY2IiwidHlwZSI6ImFwaV90b2tlbiJ9.dlB7UeF-SRhfum7RbNnJl_KrBasVJXzgs0On45zRrf4"

summary = summarize_text(text, api_key)

print(summary)