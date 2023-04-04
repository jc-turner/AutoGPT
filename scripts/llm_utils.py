from typing import List
import openai
from config import Config
from chat import ChatMessage
cfg = Config()

openai.api_key = cfg.openai_api_key

# Overly simple abstraction until we create something better
def create_chat_completion(messages: List[ChatMessage], model=None, temperature=None, max_tokens=None)->str:
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message["content"]
