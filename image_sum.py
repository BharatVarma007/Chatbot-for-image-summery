from openai import OpenAI
import base64
import json
import os

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_url = 'https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/02/19/ML-1955-2.jpg'

image_path="Images\Skynova_Invoice.jpg"

#image_url=f"data:image/jpeg;base64,{encode_image(image_path)}"

client = OpenAI()  


response = client.chat.completions.create(
    model='gpt-4o', 
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Look at this image and summarize it in one sentence"},
                {
                    "type": "image_url",
                    "image_url": {"url": image_url}
                }
            ],
        }
    ],
    max_tokens=50  
)


            
print(response.choices[0].message.content)

