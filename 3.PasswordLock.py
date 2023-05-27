print("\nSet Your Profile.")
ID = input("Enter Your ID 👉 : ")
password = input("Set The Password 👉 : ")

print("✔ Account Setup is complete ✔")

print("\nLog In Now,")
x = input("Enter ID Here 👉 : ")
y = input("Enter Passcode Here 👉 : ")

if (x == ID):
    print("Wellcome",ID,'👋,')

else:
    print("❌Invalid ID❌")

if(y==password):
    print("✔Correct password. Access Allowed✔")

else:
    print("❌Invalid Password❌")



