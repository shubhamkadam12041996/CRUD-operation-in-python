import sqlite3 
con = sqlite3.connect("product.db")  
print("Database opened successfully")  
con.execute("create table product (pid INTEGER PRIMARY KEY AUTOINCREMENT, pname TEXT NOT NULL, pdes TEXT NOT NULL,Prise INTEGER ,quantity INTEGER, pimg TEXT NOT NULL)") 
print("Table created successfully")   
con.close()