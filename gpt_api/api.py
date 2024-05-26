import json
import os

import requests

config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path) as config_file:
    config = json.load(config_file)

api_key = config['api_key']
api_url = config['api_url']


def chat_once(prompt, system_prompt="You are a helpful assistant.", max_tokens=150, n=1):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        'max_tokens': max_tokens,
        'n': n,
        'stop': None,
        'temperature': 0.7
    }

    response = requests.post(api_url, headers=headers, json=data)
    assert response.status_code == 200, f"Error: {response.status_code} - {response.text}"
    result = response.json()
    return result['choices'][0]['message']['content'].strip()


def chat():
    print("Chat with GPT-3. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat_once(user_input)
        print(f"GPT-3: {response}")


if __name__ == "__main__":
    chat()