from openai import OpenAI
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


image_url_1 = 'https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/02/19/ML-1955-2.jpg'


image_path="Images\Skynova_Invoice.jpg"

image_url=f"data:image/jpeg;base64,{encode_image(image_path)}"

img_urls=[]
img_urls.append(image_url_1)
img_urls.append(image_url)


client = OpenAI()  

response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "look at these images and summarize them all in a single sentance",
                    },
                    *[
                        {"type": "image_url", "image_url": {"url": i}} for i in img_urls
                    ],
                ],
            }
        ],
        max_tokens=100,
    )
            
print(response.choices[0].message.content)

