# Exersice 1

def pyCalculator(x,y,a):
    print("""Wellcome to swami's calculator.
    Enter operation below like add, sub, multiply, divide, power calculation. """)
    

    if (a == "add"):
        print("\nLet's Calculate !!!")
        print("\nAddition Of",x,"and",y,"is",float(x)+float(y))

    elif (a == "sub" ):
        print("\nLet's Calculate !!!")
        print("\nSubtraction Of",x,"and",y,"is",float(x)-float(y))

    elif (a == "multiply"):
        print("\nLet's Calculate !!!")
        print("\nMultiplication Of",x,"and",y,"is",float(x)*float(y))

    elif (a== "divide"):
        print("\nLet's Calculate !!!")
        print("\nDivision Of",x,"and",y,"is",float(x)/float(y))

    elif (a=="power calculation"):
        print("\nSolution = ",float(x)**float(y)) 

    else :
        print("Error : Invalid Operation.")
        print("Enter operation like add, sub, multiply, divide, power calculation.")


    print("Thank You.....")

pyCalculator(2, 3, '' )






'''
In Below Code We Use 'Float' before Variable For convert string output of input
function into float number.


print("\nSolutions :-")
print("1.Addition Of",x,"and",y,"is",float(x)+float(y))
print("2.Subtraction Of",x,"and",y,"is",float(x)-float(y))
print("3.Multiplication Of",x,"and",y,"is",float(x)*float(y))
print("4.Division Of",x,"and",y,"is",float(x)/float(y))
print("5.Modulus Of",x,"and",y,"is",float(x)%float(y))
print("6.Floor Division  Of",x,"and",y,"is",float(x)//float(y))
print("7.Square of ",x,"is the",float(x)*float(x))
print("7.Cube of ",x,"is the",float(x)*float(x)*float(x))
print("9.Square of ",y,"is the",float(y)*float(y))
print("10.Cube of ",y,"is the",float(y)*float(y)*float(y))

print("\nNow, Get Exponential Operator of any a number(means Power of number) ")
a = input("Enter Number here = ")
b = input("Enter Power or degree here = ")

print("\nSolution = ",float(a)**float(b)) 

'''






