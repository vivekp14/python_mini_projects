print("Welcome to the Quiz!")

playing = input("Do you want to play?")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
    print("Your score is " + str(score))
else:
    print("Incorrect. The correct answer is central processing Unit.")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
    print("Your score is " + str(score))
else:
    print("Incorrect. The correct answer is graphics processing unit.")  

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score +=1
    print("Your score is " + str(score))
else:
    print("Incorrect. The correct answer is random access memory.")      

print("You got " + str(score) + " questions correct!")