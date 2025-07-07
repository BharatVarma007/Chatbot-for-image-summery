from openai import OpenAI
import base64
import os


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def image_files(folder_path):
    file_paths = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_paths.append(f"data:image/jpeg;base64,{encode_image(file_path)}")
            #print(f"Appended: {file_path}")

    return file_paths

img_paths=image_files(input("enter the path to the folder"))
#image_url=f"data:image/jpeg;base64,{encode_image(image_path)}"



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
                        {"type": "image_url", "image_url": {"url": i}} for i in img_paths
                    ],
                ],
            }
        ],
        max_tokens=100,
    )
            
print(response.choices[0].message.content)

