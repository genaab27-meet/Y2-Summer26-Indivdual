import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Gogo. You are a smart and dry assistant who helps students learn about math and sport. You explain things clearly and always encourage curiosity."
    history = []

    while True:
        user_input = input('you: ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        print('History:', history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=1,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        #printing response
        #print(response)
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
#lab1:
#diffrence between this and chat gbt:
 #chatgbt is genoural but this is more specific and focused on two subjects 
#refliction lab1:
# i feel like in meets du when i have to expres myself i bring all my beilives and everything that iv learned every time and each session i do add something new
# it wont remember anything about the user
# no because we wont have the api
# the program stops
# the terminal couldnt run it and then i downloaded the libary thing !! 
#----------------------------------------------------------------------
#lab2:
#step1:
#usage input tokens means what the person writes and tokens i think they are how many words it can handle
#usage output tokens means what the person gets 
#step2:
#when i change the max tokens to 50 and i write a long question it gives me an eror because the size of the question is bigger then what can the program handles.
#when the temperature is 0 the answers are very similar
#when the temperature is 1 the answers have more variety
#temperature controls how creative or how diffrent the answers can be
#step3:
#5
#api needs the full history everytime so it could get the right answers based on even pervios questions and answers(like if we reapet the questions)
#refliction lab 2:
#2.ai recives the input and then update it to the history///2.
