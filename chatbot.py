from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI(temperature=0, model='gpt-4o')

messages = [
    SystemMessage(content="You are a helpful assistant"),
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit','bye','goodbye']:
        print("Assistant: Goodbye!")
        break
    messages.append(HumanMessage(content=user_input))
    response = chat.invoke(input=messages)
    ai_response = response.content
    print("Assistent: ", ai_response)
    messages.append(AIMessage(content=ai_response))
