import os
from mistralai import Mistral
from huggingface_hub import InferenceClient
import openai

class DeepSeek:
    def __init__(self):
        api_key = os.environ["DEEPSEEK_API_KEY"]
        self.provider = 'together'

    def call(self, content):        

        client = InferenceClient(
            model="together",
            token=self.api_key
        )


        messages = [
            {
                "role": "user",
                "content": content
            }
        ]

        completion = client.chat_completion(
            model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", 
            messages=messages,            
        )

        print(content)
        return completion.choices[0].message.content

class SambaNovaCloud:
    def __init__(self):
        api_key = os.environ["SAMBA_CLOUD_KEY"]
        self.model = 'Meta-Llama-3.1-8B-Instruct'
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.sambanova.ai/v1",
        )

    
    def call(self, content):
        print("Samba")
        messages = [{
            "role": "system",
            "content": content
        }]

        temperature = 0.1
        top_p = 0.1

        response = self.client.chat.completions.create(
            model = self.model,
            messages = messages,
            temperature = temperature,
            top_p = top_p
        )

        print(response)
        return response.choices[0].message.content




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
            ],
            max_tokens=4096
        )
        response = chat_response.choices[0].message.content
        response = response.replace('```tex', '')
        response = response.replace('```','')
        return response

