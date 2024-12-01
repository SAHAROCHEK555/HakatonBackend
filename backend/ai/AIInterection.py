import requests


class AIInterection:
    @staticmethod
    def answer_from_mistral(API_KEY, message):
        print(API_KEY)
        headers = {
            'Authorization': API_KEY,
            'Content-Type': 'application/json'
        }
        
        data = {
            "model": "mistral-nemo-instruct-2407",
            "messages": [{"role": "system", "content": "отвечай на русском языке"}, {"role": "user", "content": message}],
            "max_tokens": 1000,
            "temperature": 0.3
        }
        
        response = requests.post("http://84.201.152.196:8020/v1/completions", headers=headers, json=data)
        
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            return reply
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
        