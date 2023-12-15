print("Welcome to Quiz Game!")

playing = input("Do you want to play? ")
Name = input("Enter your name: ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
print("Rules!!!")
print("For all Correct Answers, you will get 2 marks")
print("For all Incorrect Answers, you will get -1 marks")
score = 0
# 1st
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=  2
else:
    print("Incorrect!")
    score -= 1
#2nd
answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 1
#3rd
answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 1
#4th
answer = input("What does AI stands for? ")
if answer.lower() == "artificial intelligence":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 1

print(f"Hey! {Name} you're quiz score is " + str(score))