import sqlite3
import time

baglanti=sqlite3.connect("veriler.db")
run = baglanti.cursor()
def studentInformation(nname):
   inf= run.execute("SELECT * FROM students where name=?",(nname,))
   if(len(inf.fetchall())==0):
       print("student not found")
       return 0

   for i in inf.fetchall():
       print("Student nummber: ",i[0],"Student name: ",i[1],"Student surname: ",i[2])

def newStudent(name,surname):
    run.execute("INSERT INTO students(name, surname) VALUES (?,?)",(name,surname,))
    print("student enrollment is successful.")

def AddigNote(number,m,h,a):
    run.execute("INSERT INTO Lessons(number,math,history,art) VALUES(?,?,?,?)",(number,m,h,a,))
    print("Added Note")

def absence(number,date):
    run.execute("INSERT INTO Absence(number,absence_date) VALUES(?,?)",(number,date,))
    print("Added Ansence")

def SeeNote(name):
    num= run.execute("SELECT number FROM students WHERE name=? ",(name,))
    num=num.fetchone()[0]

    notes= run.execute("SELECT * FROM Lessons WHERE number=? ",(num,))
    print(notes.fetchall())
    time.sleep(3)

def SeeAbsence(name):
    num = run.execute("SELECT number FROM students WHERE name=? ",(name,))
    num=num.fetchone()[0]
    absen = run.execute("SELECT * FROM Absence WHERE number=? ", (num,))
    print(absen.fetchall())
    time.sleep(3)


print("Welcome!")
print("*"*20)
while True:
    print("Student information -> 1\nNew student -> 2\nAdding a course note->3 \nAdding Absence-> 4")
    select = input()
    if(select == "1"):
        yourName = input("Student name-> ")
        a= studentInformation(yourName)
        if(a!=0):
            com=input("Lessons Note for -> 1\nAbsence for -> 2")
            if(com =="1"):
                SeeNote(yourName)
            elif(com == "2"):
                SeeAbsence(yourName)


    elif(select == "2"):
        newname=input("Student name->")
        newsurname=input("Student Surname->")
        newStudent(newname,newsurname)
    elif(select == "3"):
        num=input("Student number->")
        mat=input("Math note:")
        his = input("History note:")
        ar = input("Art note:")
        AddigNote(num,mat,his,ar)

    elif(select== "4"):
        n=input("Student number:")
        a=input("Student's absence->")
        absence(n,a)

    baglanti.commit() #gönderme
    baglanti.close()