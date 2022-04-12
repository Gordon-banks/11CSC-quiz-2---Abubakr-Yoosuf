#This quiz will ask multiple choice question about general knowledge . The quiz will also keep track of the score and it is going to print it at the end.There is one bonus question which is worth 3 points, Good luck!

import time

#Welcome message 
print("Welcome to my quiz about general knowledge!")
time.sleep(1)

#Chances section
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Scoring
score = 0

#my first question
question_1 = print("1) What day is ANZAC Day observed?\n(a) April 25\n(b) July 1\n(c) April 28\n(d) March 15\n\n ")
answer_1 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Noice work.\n")
        score = score + 1
        break
    else:
        print("Incorrect! :( \n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question no.2
question_2 = print("2) What is the capital city of Australia?\n(a) Sydney\n(b) Melbourne\n(c) Canberra\n(d) Perth\n\n ")
answer_2 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question number 3
question_3 = print("3) Who is the longest lasting president of the United States (as of now)?\n(a) Donald Trump\n(b) John F. Kennedy\n(c) James Madison\n(d) Franklin D.Roosevelt\n(e) Edmonton\n(f) Montreal\n\n ")
answer_3 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")
        print("The next question is a bonus point question... \n")

time.sleep(2)

#question number 4
question_4 = print("4) How many regions is New Zealand divided into?\n(a) 9\n(b) 20\n(c) 16\n(d) 17\n\n ")
answer_4 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job. +3 points because this was a bonus question\n")
        score = score + 3
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

#question number 5
question_5 = print("5) What is Canada's national animal?\n(a) Beaver\n(b) Canadian Horse\n(c) Moose\n(d) Goose\n\n ")
answer_5 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(1)

#printing the score near the end.
while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thanks for doing my quiz!")
print("Goodbye!")