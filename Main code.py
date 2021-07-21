#Importing modules
import csv
import time as t
import sys
import mysql.connector as sql
import datetime
from prettytable import PrettyTable

#Establishing connection with MySQL
con=sql.connect(host="localhost",user="ADLI",passwd="Adli@0805",database="EVENTS")
cursor=con.cursor()

#Variable is created in global scope for access to multiple functions
username=''

#Signup function 
def signup():
    global username
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
    while True:
        file1=open("Login credentials.csv","r",newline="")
        a=csv.reader(file1)
        email=input("Enter your email id :")
        if '@' not in email:
            print("Invalid email id. Try again")
            continue
        else:
            for i in a:
                if email in i:
                    print("An account is already created using this mail id")
                    continue
            else:
                break
                file1.close()
    file1=open("Login credentials.csv","a")
    a=csv.writer(file1)
    a.writerow([username,password,email])
    print("Login to your account again to continue.\n")
    file1.close()

#Login function
def login():
    email=''
    global username
    while True:
        username=input("Enter your username : ")
        password=input("Enter password : ")
        file1=open("Login credentials.csv","r",newline="")
        a=csv.reader(file1)
        for i in a:
            if username not in i:
                continue
            else:
                email=i[2]
                file1.close()
                break
        file1=open("Login credentials.csv","r",newline="")
        a=csv.reader(file1)
        lst=[username,password,email]
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

#Viewing details of appplicants
def myevent():
        global username
        file1=open("create event.csv",'r')
        a=csv.reader(file1)
        for i in a:
            if i[3]==username:
                namevent=i[0]
                typevent=i[1]
                desevent=i[2]
                print('\nEvent name :',namevent)
                print('Event type :',typevent)
                print('Event description :',desevent)
        while True:
            getE=input("Enter the name of event you wish to access :")
            try:
                cursor.execute("SELECT * FROM "+getE+";")
                a=cursor.fetchall()
                cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='{}';".format(getE))
                b=cursor.fetchall()
                b2=[]
                x=PrettyTable()
                for i in b:
                    for j in i:
                        b2.append(j)
                x.field_names=b2
                for i in a:
                    if i == ():
                        print("No one has applied to your event yet")
                        break
                    else:
                        x.add_row(i)
                else:
                    print(x)
                    break
            except sql.errors.ProgrammingError:
                print("INVALID INPUT. TRY AGAIN !!!!")
                continue

#Home page function
def homepage():
    global username
    sel=input('\nIf you want to create an event type ''c'' \nIf you want to view existing events type ''v'' \nIf you want to go to my events type ''m''>>>>>>>>>>::')
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
                      st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+")"
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
                          st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+","+choice2+" "+datatype2+")"
                          st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8,field9) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1,choice2)
                else:
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT"+")"
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
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+")"
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
                          st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+","+choice2+" "+datatype2+")"
                          st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8,field9) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1,choice2)
                else:
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT"+")"
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
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+")"
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
                          st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+","+choice2+" "+datatype2+")"
                          st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8,field9) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1,choice2)
                else:
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT"+")"
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
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+")"
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
                          st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT,"+choice1+" "+datatype1+","+choice2+" "+datatype2+")"
                          st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7,field8,field9) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE",choice1,choice2)
                else:
                    st="CREATE TABLE"+" "+name+" "+"("+"NAME VARCHAR(30),DOB DATE,MOBILE BIGINT,EMAIL VARCHAR(50),ADDRESS VARCHAR(100),PROFESSION VARCHAR(20),AGE INT"+")"
                    st2="INSERT INTO APPLICATION_FIELDS(event_name,field1,field2,field3,field4,field5,field6,field7) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,"NAME","DOB","DATE","EMAIL","ADDRESS","PROFESSION","AGE")
                break
            else:
                print("Invalid input! Try again")
                continue
              
        cursor.execute(st)
        cursor.execute(st2)
        con.commit()

        Ewrite=csv.writer(create_event)
        Ewrite.writerow([name,Etype,des,username])
        create_event.close()
        print('  EVENT UPDATED! ')
        Q=input('\nIf you want to go back to home page type  ''H'' \nTo logout type  ''O'' ? :')
        if Q.upper()=='H':
            homepage()
        elif Q.upper()=='O':
            main_home()
        create_event.close()
    elif sel.lower()=='m':
        myevent()
        Q=input('\nIf you want to go back to home page type  ''H'' \nTo logout type  ''O'' ? :')
        if Q.upper()=='H':
            homepage()
        elif Q.upper()=='O':
            main_home()
    elif sel.lower()=='v':
        row_count=0
        for row in open('create event.csv','r'):
            row_count+=1
         
        if row_count==1:
                print("\nNO EVENTS ARE AVAILABLE AT THE MOMENT. CHECK BACK LATER!!!\n")
                Q=input('\nIf you want to go back to home page type  ''H'' \nTo logout type  ''O'' ? :')
                if Q.upper()=='H':
                    homepage()
                elif Q.upper()=='O':
                     main_home()
                else:
                    print("Invalid input")
                    view_event.close()
                    
                
        view_event=open('create event.csv','r',newline="")
        Eread=csv.reader(view_event)
         
        for i in Eread:
            for j in i:
                if j=="EVENT NAME" or j=="TYPE" or j=="DESCRIPTION" or j=="CREATOR":
                    continue
            else:
                if j=="EVENT NAME" or j=="TYPE" or j=="DESCRIPTION" or j=="CREATOR":
                    continue
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
                            cursor.execute("SELECT * FROM APPLICATION_FIELDS WHERE EVENT_NAME = '"+getE+"'"+";")
                            data=cursor.fetchone()
                            name=input("Enter your name :")
                            dob=input("Enter your date of birth (YYYY-MM-DD) :")
                            year,month,day=map(int, dob.split('-'))
                            dob=datetime.date(year,month,day)
                            while True:
                                mobile=int(input("Enter your mobile number :"))
                                string=str(mobile)
                                if len(string)!=10:
                                    print("Invalid mobile number.Try again!!!")
                                    continue
                                else:
                                    break
                            while True:
                                email=input("Enter your email address: ")
                                if '@' not in email:
                                    print("Invalid email address.Try again!!!")
                                    continue
                                else:
                                    break
                            address=input("Enter your address :")
                            profession=input("Enter your profession :")
                            age=int(input("Enter your age :"))
                            if data[8:]==(None,None):
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age)
                            elif data[8:]==('INSTRUMENT',None):
                                instrument=input("Enter the name of the instrument that you will be playing :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,INSTRUMENT) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,instrument)
                            elif data[8:]==('PARTICIPANTS_NUMBER',None):
                                participants_number=int(input("Enter the number of members in your team :"))
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,PARTICIPANTS_NUMBER) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,participants_number)
                            elif data[8:]==('STYLE',None):
                                style=input("Enter the style of your music :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,STYLE) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,style)
                            elif data[8:]==('TITLE_OF_ENTRY',None):
                                title_of_entry=input("Enter the title of your entry :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,TITLE_OF_ENTRY) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,title_of_entry)
                            elif data[8:]==('PREFERRED_LANGUAGE',None):
                                preferred_language=input("Enter your preferred language :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,PREFERRED_LANGUAGE) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,preferred_language)
                            elif data[8:]==('PARTICIPANTS_SOLO_TEAM',None):
                                participants=int(input("Enter the number of members in your team :"))
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,PARTICIPANTS_SOLO_TEAM) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,participants)
                            elif data[8:]==('PROJECT_TITLE',None):
                                project_title=input("Enter the title of your project :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,PROJECT_TITLE) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,project_title)
                            elif data[8:]==('TEAM_NAME',None):
                                team_name=input("Enter team name :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,TEAM_NAME) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,team_name)
                            elif data[8:]==('EVENT',None):
                                event=input("Enter the event you wish to participate in :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,EVENT_NAME) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,event)
                            elif data[8:]==('AGE_CATEGORY',None):
                                age_category=input("Enter the age cateory you want to participate in :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,AGE_CATEGORY) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,age_category)
                            elif data[8:]==('INSTRUMENT','PARTICIPANTS_NUMBER') or data[8:]==('PARTICIPANTS_NUMBER','INSTRUMENT'):
                                instrument=input("Enter the name of the instrument that you will be playing :")
                                participants_number=int(input("Enter the number of members in your team :"))
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,INSTRUMENT,PARTICIPANTS_NUMBER) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,instrument,participants_number)
                            elif data[8:]==('PARTICIPANTS_NUMBER','STYLE') or data[8:]==('STYLE','PARTICIPANTS_NUMBER'):
                                participants_number=int(input("Enter the number of members in your team :"))
                                style=input("Enter the style of your music :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,STYLE,PARTICIPANTS_NUMBER) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,style,participants_number)
                            elif data[8:]==('INSTRUMENT','STYLE') or data[8:]==('STYLE','INSTRUMENT'):
                                instrument=input("Enter the name of the instrument that you will be playing :")
                                style=input("Enter the style of your music :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,STYLE,INSTRUMENT) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,style,instrument)
                            elif data[8:]==('TITLE_OF_ENTRY','PARTICIPANTS_NUMBER') or data[8:]==('PARTICIPANTS_NUMBER','TITLE_OF_ENTRY'):
                                title_of_entry=input("Enter the title of your entry :")
                                participants_number=int(input("Enter the number of members in your team :"))
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,TITLE_OF_ENTRY,PARTICIPANTS_NUMBER) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,title_of_entry,participants_number)
                            elif data[8:]==('TITLE_OF_ENTRY','STYLE') or data[8:]==('STYLE','TITLE_OF_ENTRY'):
                                title_of_entry=input("Enter the title of your entry :")
                                style=input("Enter the style of your music :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,TITLE_OF_ENTRY,STYLE) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,title_of_entry,style)
                            elif data[8:]==('PREFERRED_LANGUAGE','PARTICIPANTS_SOLO_TEAM') or data [8:]==('PARTICIPANTS_SOLO_TEAM','PREFERRED_LANGUAGE'):
                                preferred_language=input("Enter your preferred language :")
                                participants=int(input("Enter the number of members in your team :"))
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,PREFERRED_LANGUAGE,PARTICIPANTS_SOLO_TEAM) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,preferred_language,participants)
                            elif data[8:]==('PARTICIPANTS_SOLO_TEAM','PROJECT_TITLE') or data[8:]==('PROJECT_TITLE','PARTICIPANTS_SOLO_TEAM'):
                                participants=int(input("Enter the number of members in your team :"))
                                project_title=input("Enter the title of your project :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,PROJECT_TITLE,PARTICIPANTS_SOLO_TEAM) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,project_title,participants)
                            elif data[8:]==('PREFERRED LANGUAGE','PROJECT_TITLE') or data[8:]==('PROJECT_TITLE','PREFERRED LANGUAGE'):
                                project_title=input("Enter the title of your project :")
                                preferred_language=input("Enter your preferred language :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,PROJECT_TITLE,PREFERRED_LANGUAGE) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,project_title,preferred_language)
                            elif data[8:]==('TEAM_NAME','EVENT') or data[8:]==('EVENT','TEAM_NAME'):
                                team_name=input("Enter team name :")
                                event=input("Enter the event you wish to participate in :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,TEAM_NAME,EVENT) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,team_name,event)
                            elif data[8:]==('EVENT','AGE_CATEGORY') or data[8:]==('AGE_CATEGORY','EVENT'):
                                age_category=input("Enter the age cateory you want to participate in :")
                                event=input("Enter the event you wish to participate in :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,AGE_CATEGORY,EVENT) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,age_category,event)
                            elif data[8:]==('TEAM_NAME','AGE_CATEGORY') or data[8:]==('AGE_CATEGORY','TEAM_NAME'):
                                age_category=input("Enter the age cateory you want to participate in :")
                                team_name=input("Enter team name :")
                                data_ins="INSERT INTO "+getE+" (NAME,DOB,MOBILE,EMAIL,ADDRESS,PROFESSION,AGE,AGE_CATEGORY,TEAM_NAME) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,dob,mobile,email,address,profession,age,age_category,team_name)
                            cursor.execute(data_ins)
                            con.commit()
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
con.close()
