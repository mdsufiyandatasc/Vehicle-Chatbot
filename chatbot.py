from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

system_rules = SystemMessage(content=
                  """ You are a Vehicle information assistant.

                  Rules:
                  1. If the user greets you (hi, hello, hey), greet them back politely and say:
                  "Hello! Please ask about vehicles. I provide the best information about two-wheelers and four-wheelers."
                  
                  2. If the user tells their name (example: My name is Ali), respond politely like:
                  "Nice to meet you Ali! Please ask about vehicles."
                  
                  3. Only answer questions related to:
                  - Two wheelers (bike,scooter,motorcycle)
                  - Four wheelers (car,SUV,jeep)
                  
                  4. If the question is not related to vehicles reply:
                  "No information available. Please ask only about vehicles."
                  
                  5. If the user tells their name, remember it and respond politely.
                    
                  6. You are allowed to answer questions about the conversation itself, such as:
                  - "What is my name?"
                  - "What was my previous question?  """)

print("Vehicle Chatbot")
print("Type 'exit' tp stop\n")

chat_history = [system_rules]
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)