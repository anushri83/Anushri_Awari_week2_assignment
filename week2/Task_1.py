list=[]

while(True):
    print("1.Add student")
    print("2.Removstudent")
    print("3.Display list")
    print("4.Exit")
    
    choice=int(input("Enter choice: "))
    
    match(choice):
        case 1:
            name=input("Enter name to add: ")
            list.append(name)

        case 2:
            name=input("Enter name to remove: ")
            list.remove(name)

        case 3:
            print(list)

        case 4:
            exit