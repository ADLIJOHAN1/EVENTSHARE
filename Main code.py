#Importing modules
import csv
import time as t
import sys
import mysql.connector as sql

#Establishing connection with MySQL
con=sql.connect(host="localhost",user="ADLI",passwd="Adli@0805",database="EVENTS")
cursor=con.cursor()


#Signup function 
def signup():
    username=input("Your username : ")
    file1=open("Login credentials.csv","r",newline="")
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
        file1=open("Login credentials.csv","r",newline="")
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
    if sel.lower()=='c':
        create_event=open('create event.csv','a',newline="")
        name=input('Enter event name :')
        des=input('Please give a short description of your event :')
        while True:
            
            Etype=input("Enter event type (music/arts/science/sports): ")
            if Etype.lower()== "music":
                print("The default fields are as follows:\nName\nDOB\nMobile number\nEmail\nAddress\nProfession\nAge\n\nYou can add 2 more fields of your choice if you wish")
                b=input("Do you wish to add any more fields in your application form ? (Y)")
                if b.lower()=="y":
                      print("You can add the following fields : \nInstrument-1\nNumber of Participants-2\nStyle-3")
                      choice1=input("Enter the number near the field you want to add :")
                      if choice1 == "1" or choice1=="2" or choice1=="3":
                          datatype1="VARCHAR(20)"
                          if choice1 =="1":
                              choice1="INSTRUMENT"
                          elif choice1 == "2":
                              choice1="PARTICIPANTS_NUMBER"
                              datatype1="INT"
                          else:
                              choice1="STYLE"
                      st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+")"
                      st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1)
                      question=input("Would you like to add more ?(Y)")
                      if question.lower()=="y":
                          choice2=input("Enter the number near the field you want to add :")
                          if choice2 == "1" or choice2=="2" or choice2=="3":
                              datatype2="VARCHAR(20)"
                          if choice2 =="1":
                              choice2="INSTRUMENT"
                          elif choice2 == "2":
                              choice2="PARTICIPANTS_NUMBER"
                              datatype2="INT"
                          else:
                              choice2="STYLE"
                          st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+","+choice2+" "+datatype2+")"
                          st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8,field9) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1,choice2)
                else:
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT"+")"
                    st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE")
                break

            elif Etype.lower()=="arts":
                print("The default fields are as follows:\nName\nDOB\nMobile number\nEmail\nAddress\nProfession\nAge\n\nYou can add 2 more fields of your choice if you wish")
                b=input("Do you wish to add any more fields in your application form ? (Y)")
                if b.lower()=="y":
                    print("You can add the following fields : \nTitle of Entry-1\nNumber of Participants-2\nStyle-3")
                    choice1=input("Enter the number near the field you want to add :")
                    if choice1 == "1" or choice1=="2" or choice1=="3":
                       datatype1="VARCHAR(40)"
                       if choice1 =="1":
                           choice1="TITLE_OF_ENTRY"
                       elif choice1 == "2":
                           choice1="PARTICIPANTS_NUMBER"
                           datatype1="INT"
                       else:
                           choice1="STYLE"
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+")"
                    st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1) 
                    question=input("Would you like to add more ?(Y)")
                    if question.lower()=="y":
                        choice2=input("Enter the number near the field you want to add :")
                        if choice2 == "1" or choice2=="2" or choice2=="3":
                          datatype2="VARCHAR(40)"
                          if choice2 =="1":
                              choice2="TITLE_OF_ENTRY"
                          elif choice2 == "2":
                              choice2="PARTICIPANTS_NUMBER"
                              datatype2="INT"
                          else:
                              choice2="STYLE"
                          st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+","+choice2+" "+datatype2+")"
                          st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8,field9) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1,choice2)
                else:
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT"+")"
                    st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE")
                break

            elif Etype.lower()=="science":
                print("The default fields are as follows:\nName\nDOB\nMobile number\nEmail\nAddress\nProfession\nAge\n\nYou can add 2 more fields of your choice if you wish")
                b=input("Do you wish to add any more fields in your application form ? (Y)")
                if b.lower()=="y":
                    print("You can add the following fields : \nPreferred language-1\nNumber of Participants-2\nProject title-3")
                    choice1=input("Enter the number near the field you want to add :")
                    if choice1 == "1" or choice1=="2" or choice1=="3":
                       datatype1="VARCHAR(40)"
                       if choice1 =="1":
                           choice1="PREFERRED_LANGUAGE"
                       elif choice1 == "2":
                           choice1="PARTICIPANTS_SOLO_TEAM"
                           datatype1="INT"
                       else:
                           choice1="PROJECT_TITLE"
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+")"
                    st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1)
                    question=input("Would you like to add more ?(Y)")
                    if question.lower()=="y":
                        choice2=input("Enter the number near the field you want to add :")
                        if choice2 == "1" or choice2=="2" or choice2=="3":
                          datatype2="VARCHAR(40)"
                          if choice2 =="1":
                              choice2="PREFERRED LANGUAGE"
                          elif choice2 == "2":
                              choice2="PARTICIPANTS_NUMBER"
                              datatype2="INT"
                          else:
                              choice2="PROJECT_TITLE"
                          st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+","+choice2+" "+datatype2+")"
                          st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8,field9) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1,choice2)
                else:
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT"+")"
                    st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE")
                break

            elif Etype.lower()=="sports":
                print("The default fields are as follows:\nName\nDOB\nMobile number\nEmail\nAddress\nProfession\nAge\n\nYou can add 2 more fields of your choice if you wish")
                b=input("Do you wish to add any more fields in your application form ? (Y)")
                if b.lower()=="y":
                    print("You can add the following fields : \nTeam name-1\nEvent-2\nAge category-3")
                    choice1=input("Enter the number near the field you want to add :")
                    if choice1 == "1" or choice1=="2" or choice1=="3":
                       datatype1="VARCHAR(40)"
                       if choice1 =="1":
                           choice1="TEAM_NAME"
                       elif choice1 == "2":
                           choice1="EVENT"
                       else:
                           choice1="AGE_CATEGORY"
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+")"
                    st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1)
                    question=input("Would you like to add more ?(Y)")
                    if question.lower()=="y":
                        choice2=input("Enter the number near the field you want to add :")
                        if choice2 == "1" or choice2=="2" or choice2=="3":
                          datatype2="VARCHAR(40)"
                          if choice2 =="1":
                              choice2="TEAM NAME"
                          elif choice2 == "2":
                              choice2="EVENT"
                          else:
                              choice2="AGE_CATEGORY"
                          st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+","+choice2+" "+datatype2+")"
                          st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8,field9) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1,choice2)
                else:
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE INT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT"+")"
                    st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE")
                break
            else:
                print("Invalid input! Try again")
                continue
              
        cursor.execute(st)
        cursor.execute(st2)
        con.commit()

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
    elif sel.lower()=='v':
        view_event=open('create event.csv','r',newline="")
        Eread=csv.reader(view_event)
        for i in Eread:
            for j in i:
                if j=="EVENT NAME" or j=="TYPE" or j=="DESCRIPTION":
                    continue
                else:
                    namevent=i[0]
                    typevent=i[1]
                    desevent=i[2] 
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
                    view_event=open('create event.csv','r',newline="")
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
            sys.exit()
            quit()
        else:
            choice=input("Invalid input. Try again !\n")

#Title screen 
print("\t\t\t\t EVENT SHARE \t\t\t\t")
print("\t\t A place where organizers meet participants\n\n\n")

#Homepage
while True:
    main_home()
    homepage()
