#Importing modules
import csv
import time as t


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
    while True:
        username=input("Enter your username : ")
        password=input("Enter password : ")
        lst=[username,password]
        file1=open("Login credentials.csv","r")
        a=csv.reader(file1)
        if lst not in a:
            print("Username or password is incorrect")
            continue

        else:
            print('\nLogging in',end='')
            for i in range(7):
                t.sleep(0.5)
                print('.',end='')
            print("\n\n          Welcome",username)
            break
    file1.close()

#Home page function
def homepage():
    sel=input('\nIf you want to create an event type ''c'' \nIf you want to view existing events type ''v''>>>>>>>>>>::')
    if sel=='c':
        create_event=open('create event.csv','a')
        name=input('Enter event name :')
        Etype=input('\nWhat type of event is this (art/science/sports) :')
        des=input('Please give a short description of your event :')
        Ewrite=csv.writer(create_event)
        Ewrite.writerow([name,Etype,des])
        create_event.close()
        print('  EVENT UPDATED! ')
        Q=input('\nIf you want to go back to home page type  ''H'' \nTo logout type  ''O'' ? :')
        if Q.upper()=='H':
           homepage()
        elif Q.upper()=='O':
            main_home()
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
        view_event.close()
        while True:
            apply=input('do you wish to apply to any of these events (Y/N)?')
            if apply.upper()=='Y':
                a=True
                while a:
                    getE=input('Type the event name of which you want to apply ..')
                    view_event=open('create event.csv','r')
                    Eread=csv.reader(view_event)
                    for i in Eread:
                        if getE in i:
                            print("Applied")
                            a=False
                            break
                        elif getE not in i:
                            continue
                    if i==[]:
                        print("Event does not exist")
                        continue
                    break
                Q=input('\nIf you want to go back to home page type  ''H'' \nTo logout type  ''O'' ? :')
                if Q.upper()=='H':
                    homepage()
                elif Q.upper()=='O':
                     main_home()
                else:
                    print("Invalid input")
                    continue
                break
                view_event.close()
                    
            elif apply.upper()=='N':
                Q=input('\nIf you want to go back to home page type  ''H'' \nTo logout type  ''O'' ? :')
                if Q.upper()=='H':
                    homepage()
                elif Q.upper()=='O':
                     main_home()
                else:
                    print("Invalid input")
                    continue
                break
            else:
                print("Invalid input")
                continue

#Login/Signup page
def main_home():
    
    print("Press 1 to create a new account \nPress 2 to use an exisitng account \nPress 3 to quit")
    choice=input()
    while True:
        if choice=="1":
            signup()
            login()
            break
        elif choice=="2":
            login()
            homepage()
            break
        elif choice=='3':
            quit()
        else:
            choice=input("Invalid input. Try again !\n")

#Title screen 
print("\t\t\t\t EVENT SHARE \t\t\t\t")
print("\t\t A place where organizers meet participants\n\n\n")

#Homepage
main_home()

homepage()
