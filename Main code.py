#Importing modules
import csv

#Signup function 
def signup():
    username=input("Your username : ")
    file1=open("Login credentials.csv","r")
    while True:
        a=csv.reader(file1)
        for i in a:
            if username in i:
                print("User name already taken")
                username=input("Your username : ")
        break
    file1.close()
    password=input("Enter your password : ")
    re_enter=input("Enter password again : ")
    while True:
        if password != re_enter:
            print("Passwords do not match, Try again!")
            password=input("Enter your password : ")
            re_enter=input("Enter password : ")
        if password == re_enter:
            break
    file1=open("Login credentials.csv","a")
    a=csv.writer(file1)
    a.writerow([username,password])
    print("Login to your account again to continue.\n")
    file1.close()

#Login function
def login():
    username=input("Enter your username : ")
    password=input("Enter password : ")
    lst=[username,password]
    file1=open("Login credentials.csv","r")
    a=csv.reader(file1)
    while True:
        if lst not in a:
            print("Username or password is incorrect")
            username=input("Enter your username : ")
            password=input("Enter password : ")
            lst=[username,password]
        else:
            print("Welcome",username)
            break
    file1.close()

#Home page function
def homepage():
    sel=input('If you want to create an event type ''c'' \nIf you want to view existing events type ''v''>>>>>>>>>>::')
    if sel=='c':
        create_event=open('create event.csv','a')
        name=input('Enter event name :')
        Etype=input('\nWhat type of event is this (art/science/sports) :')
        des=input('Please give a short description of your event :')
        Ewrite=csv.writer(create_event)
        Ewrite.writerow([name,Etype,des])
        create_event.close()
        print('  EVENT UPDATED! ')
        Q=input('Do you wish to go back to the home page(Y/N) ? :')
        if Q=='Y':
           homepage()
        elif Q=='N':
            quit()
        create_event.close()
    elif sel=='v':
        view_event=open('create event.csv','r')
        Eread=csv.reader(view_event)
        for i in Eread:
            for j in i:
                namevent=i[0]
                typevent=i[1]
                desevent=i[2]
            if len(i) !=0: 
                  print('\nEvent name :',namevent)
                  print('Event type :',typevent)
                  print('Event description :',desevent)
            
           
        Q=input('Do you wish to go back to the home page(Y/N) ? :')
        if Q=='Y':
           homepage()
        elif Q=='N':
            quit()

#Title screen 
print("\t\t\t\t EVENT SHARE \t\t\t\t")
print("\t\t A place where organizers meet participants\n\n\n")

#Login/Signup page
print("Press 1 to create a new account \nPress 2 to use an exisitng account")
choice=input()
while True:
    if choice=="1":
        signup()
        login()
        break
    elif choice=="2":
        login()
        break
    else:
        choice=input("Invalid input. Try again !\n")

#Homepage
homepage()

    
        

