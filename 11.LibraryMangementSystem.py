def Library_Database():
    print("\nLibrary Database :")
    x= input("Press 0 For Add Book And Press 1 For Checkout Everything : ")
    print("Your Input Is ",x)

    NoOfBook = 2
    Books  = ["Rich Dad Poor Dad", "I Am Mind"]

    class Library():

        def CheckoutLibrary (self):
            if int(NoOfBook) == len(Books):
                print("Everything Is Fine!")

            else:
                print("Something Went Wroung")

    a = Library()


    if (x == '1'):
        a.CheckoutLibrary()
        return

    elif (x == '0') :
        y = input("Enter the book name for adding in the database :")
        NoOfBook = NoOfBook + 1
        Books.append(y)
        print("Book ",y,"is added successfully")
        print("The list is ",Books)
        print(NoOfBook,"Books available in our libary.")
        return
    
    else:
        print("Invalid Input")
        

Library_Database()

            