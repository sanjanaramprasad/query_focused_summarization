import openai
from nltk import word_tokenize, sent_tokenize
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff
import tiktoken

from transformers import GPT2Tokenizer
class GPTInference():
    def __init__(self):
        openai.api_key = "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"
        self.tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo-16k-0613")

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def get_chatgpt_response(self, prompt):
        # print(openai.api_key)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k-0613",
                                       messages=[
                        {"role": "user", "content": prompt},
                        ], 
                        )
        return response['choices'][0]['message']['content']
    
    