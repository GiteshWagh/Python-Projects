import random

print("Here We create only 8 to 10 digit password")
list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','&','*','1','2','3','4','5','6','7','8','9','0']
X = (random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))
inputFromUser =int(input("Enter How many Digit Password You Have : "))
# for k in range(0,int(X)*int(inputFromUser)): 
#     print(X)
if (inputFromUser == 8):
    print(X)


elif (inputFromUser == 9):
    X1 = (random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))
    print(X1)
    

else:
    X2 = (random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))+(random.choice(list))
    print(X2)



    

