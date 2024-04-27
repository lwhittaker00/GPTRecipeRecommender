import os
from openai import OpenAI
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()

#used to run the api assistant
def GetFoodRec(title, ingredients, tools):
    #create assistant that responds to user input
    assistant = client.beta.assistants.create(
        name="Recipe Generator",
        instructions=f"Given user inputs Title: {title}, Ingredients: {ingredients}, Tools: {tools}. You are a food recommender generator who after taking user input on the title, ingredients, and tools will provide a recipe recommendation with instructions on making the dish.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-3.5-turbo-0125",
    )
    
    #create a thread that represents a conversation with a user
    thread = client.beta.threads.create()   
    
    #create message object that will get contents of the message from users
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=f"Inputs: {title}, {ingredients}, {tools}. recommend a recipe based on the given inputs. Give back a response that starts with a greeting, then explains the ingredients and tools utilized in the recommended recipe, including the quantities of each ingredient used. Next, on new lines provide the estimated preparation and cooking times. Then, provide an ordered list of the instructions of the recipe."
    )
    
    #used to generate a response from thread after it has input
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address user as chef. User is wanting to learn to cook."
    )
    
    #once run complete save it to value
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        ) 
        for msg in messages:
            if isinstance(msg.content[0], dict):
                text_content = msg.content[0]['text']
            else:
                text_content = msg.content[0].text
            if 'recipe' in text_content.value.lower():
                return text_content.value
        else:
            return "No recipe recommendation found."
    else:
        return f"Error: {run.status}"
        

