import tkinter as tk
import mysql.connector
#^^^^Imports
root=tk.Tk()
root.geometry("300x200")
#^^^Window Creation
l1=tk.Label(root,text="Name:")
l1.grid(row=0, column=0)
t1=tk.Entry(root)
t1.grid(row=0,column=1)

l2=tk.Label(root,text="ID:")
l2.grid(row=1, column=0)
t2=tk.Entry(root,show="*")
t2.grid(row=1,column=1)

l3=tk.Label(root,text="Age:")
l3.grid(row=2, column=0)
t3=tk.Entry(root)
t3.grid(row=2,column=1)
#^^^^^Creation Of Form
def f1():
    mydb=mysql.connector.connect(
    host="localhost",
    database="connection",
    user="root",
    password="password",

    )
    #connection of database
    cursor=mydb.cursor()
    print("Connection Successful")
    name=t1.get()
    id=t2.get()
    age = t3.get()
    sql=("insert into a (NAME,ID, AGE) values (%s, %s, %s) ")
    val=(name,id,age)
    cursor.execute(sql,val)
    mydb.commit()
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)
    mydb.close()
    #Inserts data into databbase
b1=tk.Button(root,text="Enter Values",command=f1)
b1.grid(row=3,column=0)
#creates button

root.mainloop()
