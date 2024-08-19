import requests
import json
import os
from utils.get_keys import load_config

config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "config.yaml")
# config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'configs', 'config.yaml')

load_config(config_path)


class OpenAIModel:
    # This class represents an interface to interact with OpenAI's API

    def __init__(self, model, system_prompt, temperature):
        # Constructor method that initializes the OpenAIModel object
        
        # The endpoint URL for OpenAI's chat completions API
        self.model_endpoint = "https://api.openai.com/v1/chat/completions"
        # The temperature parameter for controlling randomness in the model's output
        self.temperature = temperature
        # The specific OpenAI model to be used (e.g., "gpt-3.5-turbo", "gpt-4")
        self.model = model
        # The system prompt that sets the context or behavior for the AI
        self.system_prompt = system_prompt
        # Retrieves the OpenAI API key from environment variables
        self.api_key = os.getenv("OPENAI_API_KEY")
        # Headers for the HTTP request, including content type and authorization
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def generate_text(self, prompt):
        payload = {
            "model": self.model,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "temperature": self.temperature,
        }

        response = requests.post(self.model_endpoint, headers=self.headers, json=payload)
        response_json = response.json()
        response = json.loads(response_json['choices'][0]['message']['content'])
        
        print(f"\n\nResponse from OpenAI model: {response}")
        
        return response


        