import random

print("\nWellcome To Snake-Water-Gun Game !!!\n")


list1 = ["Snake", "Water","Gun"]
Computers_Choice = random.choice(list1)
print("{ Snake-Water-Gun }")
Players_Choice = input("Enter Option : ")
print(f"Computer choose : ",Computers_Choice)

if (Computers_Choice == Players_Choice):
    print("!!!Tie!!!")
   

if (Computers_Choice == "Snake" and Players_Choice == "Water"):
    print("!!!Computer Won!!!") 

if (Computers_Choice == "Snake" and Players_Choice == "Gun"):
    print("!!!You Won!!!")



if (Computers_Choice == "Water" and Players_Choice == "Snake"):
    print("!!!You Won!!!") 

if (Computers_Choice == "Water" and Players_Choice == "Gun"):
    print("!!!Computer Won!!!")


if (Computers_Choice == "Gun" and Players_Choice == "Snake"):
    print("!!!Computer Won!!!") 

if (Computers_Choice == "Gun" and Players_Choice == "Water"):
    print("!!!You Won!!!")










