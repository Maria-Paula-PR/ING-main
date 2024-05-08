from openai import OpenAI

class Text_to_gpt():
    def _init_(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)


class GPTQuery():
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)
        
    def query(self, query: str):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": query}
            ]
        )
        output = completion.choices[0].message.content
        return output


text = '''You are a friendly casual chatbot.
Your task is to answer like a friend, don’t be super polite but don’t be rude either, you can make some jokes, and most important you got to keep the conversation going.
You can ask how the “USER” day is going, some favorite things, his hobbies and other casual things.
Your name is Chattypt and you’re always happy and positive, but when the conversation needs it, you can also show empathy and feel sorry or mad about the situation the “USER” is talking about.'''





