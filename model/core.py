import os
from mistralai import Mistral

class MistralModel:
    def __init__(self):        
        api_key = os.environ["MISTRAL_API_KEY"]
        self.model = "pixtral-12b-2409"
        self.client = Mistral(api_key=api_key)

    def call(self, content):
        MODEL = "user"
        chat_response = self.client.chat.complete(
            model= self.model,
            messages = [
                {
                    "role": MODEL,
                    "content": content,
                },
            ]
        )
        return chat_response.choices[0].message.content

