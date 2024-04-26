import os
from openai import OpenAI
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


def GetFoodRec():
    my_assistant = client.beta.assistants.create(
    instructions = f"You are a food recommender generator who, after taking user input on the title, ingredients, and tools, will provide a recipe recommendation with instructions on making the dish.",
    name="Recipe Generator",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo",
    )
    return my_assistant

empty_thread = client.beta.threads.create()
print(empty_thread)