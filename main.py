import tkinter as tk
import mysql.connector
#^^^^imports
root=tk.Tk()
root.geometry("300x200")
#^^^window creation
l1=tk.Label(root,text="Name:")
l1.grid(row=0, column=0)
t1=tk.Entry(root)
t1.grid(row=0,column=1)

l2=tk.Label(root,text="ID:")
l2.grid(row=1, column=0)
t2=tk.Entry(root,show="*")
t2.grid(row=1,column=1)
#^^^^^creation Of form
def f1():
    mydb=mysql.connector.connect(
    host="localhost",
    database="connection",
    user="root",
    password="tyu@3434",
    

    )
    #connection of database
    cursor=mydb.cursor()
    print("Connection Successful")
    name=t1.get()
    id=t2.get()
    sql=("insert into a (NAME,ID) values (%s, %s) ")
    val=(name,id)
    cursor.execute(sql,val)
    mydb.commit()
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)
    mydb.close()
    #inserts data into databbase
b1=tk.Button(root,text="Enter Values",command=f1)
b1.grid(row=3,column=0)
#creates button

root.mainloop()
