print("\nWellcom to Stone-Paper-Scissor\n")
import random
list1 = ["Stone","Paper","Scissor"]
computers_choice = random.choice(list1)
print("Choose Stone-Paper-Scissor.")
Players_Choice = input("Enter Your Choice : ")
print("computer choice :",computers_choice)

if (computers_choice == Players_Choice):
    print("!!!Tie!!!")

elif (computers_choice == "Stone" and Players_Choice == "Paper"):
    print("!!!You Won!!!")

elif (computers_choice == "Stone" and Players_Choice == "Scissor"):
    print("!!!Computer Won!!!")

elif (computers_choice == "Paper" and Players_Choice == "Stone"):
    print("!!!Computer Won!!!")

elif (computers_choice == "Paper" and Players_Choice == "Scissor"):
    print("!!!You won!!!")

elif (computers_choice == "Scissor" and Players_Choice == "Stone"):
    print("!!!You Won!!!")

elif (computers_choice == "Scissor" and Players_Choice == "Paper"):
    print("!!!Computer Won!!!")
 


