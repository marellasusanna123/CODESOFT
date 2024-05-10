code={
    "hi":"hi.how may i assist you..",
    "your name please!":"chatbot3.45",
    "what Ai means":"AI stands for Artificial Intelligence, which refers to machines performing tasks that typically require human intelligence.",
    "how does Ai work":"AI systems use algorithms and data to learn and make decisions, mimicking human cognitive functions.",
    "history of ai":"The history of AI traces back to the mid-20th century when researchers began exploring the concept of machines simulating human intelligence through algorithms and computing power.",
    "What are the benefits of AI":"AI can improve efficiency, automate tasks, make predictions, and enhance decision-making processes.",
    "What are the concerns about AI":"Concerns include job displacement, privacy issues, biased algorithms, and ethical considerations in AI decision-making.",
}
def get_response(user_input):
    for pattern,response in code.items():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't understand that.Can you please rephrase your sentence?"
print("Chatbot: Hi! I'm a simple chatbot,I'm here to assist you!")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
       print("Chatbot: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Chatbot:",response)
