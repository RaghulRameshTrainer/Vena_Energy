import sqlite3

dbh=sqlite3.connect('vena.db')
c=dbh.cursor()

def create_table():
    c.execute('CREATE TABLE employee( empname REAL, tech REAL, exp REAL)')

def load_data():
    # c.execute("INSERT INTO employee VALUES('Ashwin','Java','25')")
    # c.execute("INSERT INTO employee VALUES('Malini','Python','15')")
    e_name=input('Enter your name : ')
    e_tech=input("Enter your technology : ")
    e_exp=input("Enter your experience : ")
    c.execute("INSERT INTO employee VALUES(?,?,?)",(e_name,e_tech,e_exp))
    dbh.commit()

def update_data():
    c.execute("UPDATE employee SET tech='Android' WHERE empname='Tharani Priya'")
    dbh.commit()
    c.close()
    dbh.close()

def delete_data():
    c.execute("DELETE FROM employee WHERE empname='Levin'")
    dbh.commit()
    c.close()
    dbh.close()

def fetch_records():
    c.execute("SELECT * FROM employee")
    # fetchone, fetchmany, fetchall
    #print(c.fetchone())
    #print(c.fetchmany(5))
    print(c.fetchall())
    # for row in c.fetchall():
    #     print(f"{row[0]} is working in {row[1]} from past {row[-1]}")
#create_table()
# for x in range(5):
#     load_data()
#update_data()
#delete_data()
fetch_records()