print("Welcome to my quizz game")
name = input("What is your name? ")
print("Hello", name, "welcome to this quizz")
playing = input("Would you like to play? ")
if playing != "yes":
    quit
else:
    print("Okay lets start")
question = input("What country are you from? ")
if question != "Uganda":
    print("incorrect")
else:
    print("correct")
question = input("What do you like? ")
if question != "yes":
    print("incorrect")
elif question == "Not sure":
    print("incorrect")
else:
    print("correct")
question = input("What is your favourite programming languange? ")
if question != "python":
    print("incorrect")
elif question == "java":
    print("Good try")
elif question == "javacsript":
    print("okay, i get you")
else:
    print("i also dont know which one is your favourite.")
question = input("What is your favourite car? ")
if question == question:
    print("correct")
else: 
    print("incorrect")