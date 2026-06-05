def chatbot():
    print("basic chatbot")
    while True:
        user=input("user: ")
        if user=="hello":
            print("Bot: Hi!")
        elif user=="how are you":
            print("Bot: I'm fine,thanks!")
        elif user=="bye":
            print("Bot: Goodbye!")
            break
        else:
            print("sorry I can't understand")
chatbot()