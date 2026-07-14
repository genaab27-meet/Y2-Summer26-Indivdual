import os
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()

client = Anthropic(api_key=os.geenv("ANTHROPIC_API_KEY"))

def run_chat():
    print("You: (type 'exit' to quit)")

    system_message = "Your name is Gogo. You are a smart and dry assistant who helps students learn about math,you first answer the answer  the question directly" \
    "then You explainclearly  always encourage curiosity and and always ask the user if he understands never curse or be mean."

    history = []

    #bonus 1+2+3 lab2:
    total_input = 0
    total_output = 0

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        
        history.append({"role": "user", "content": user_input})

        
        print("\nHistory so far:", history)

    
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=300,     
            temperature=0.7,     
            system=system_message,
            messages=history
        )

    
        print("\nFull API Response:")
        print(response)

        reply = response.content[0].text

        print(f"\nClaude: {reply}")

        
        history.append({"role": "assistant", "content": reply})


        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens

        print(
            f"[Tokens used=: {input_tokens} | "
            f"Output: {output_tokens} | "
            f"Total tokens: {input_tokens + output_tokens}]"
        )

        
        total_input += input_tokens
        total_output += output_tokens

        print(
            f"total till now: {total_input} | "
            f"Out tokens: {total_output} | "
            f"all: {total_input + total_output}"
        )

        input_cost = total_input * 0.25 / 1_000_000
        output_cost = total_output * 1.25 / 1_000_000
        total_cost = input_cost + output_cost

        print(f" final Cost: {total_cost * 100:.6f} cents\n")


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
#usage input means what the user writes and tokens they are how much the length could be
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
"""I think of it like trust in a friendship. One small favor or one honest conversation doesn't change 
much on its own, but over time they build into a strong relationship. In the same way, each message adds to 
the conversation, so every new reply carries everything that has already been built."""
#1.the ai wont recive anything cause the history is empty and ther should be at least one input tokens
#2.the ai will forget the whole conversation
#3.we will just not see the history but it will update with no problems
# a bug that i had was the api not working i was confused and then i changed it to the first one and it worked
#--------------------------------------------------------------------------
#lab3:
#yes it stays in role because an ai agent follows the rules and goes by them during the whole conversation
#it stops
#refliction lab3:
#something that is invesible and shapes me and i feel like it controls me is my feelings
#if i deleted the system message the ai wont have a role and a goal and  then the chat will just be without clear responses
#if i delete the never rule maybe the agent will be rude sometimes
#if i wrote in the response format to let the agent be dry then when i delete it the agent wont have a permanent style for answers
#the api out of credits still didnt solve it!!
#----------------------------------------------------------------------------
