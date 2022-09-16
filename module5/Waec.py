import sqlite3
import csv

#check
print("successful")

#create a connection
conn= sqlite3.connect('results.db')

#check
print("connection created successfully")

#create a cursor
c= conn.cursor()

#check
print("cursor created successfully")

#create a table
# table = """CREATE TABLE waec_results (
#     id INTEGER,
#     name TEXT,
#     maths INTEGER,
#     english INTEGER,
#     physics INTEGER,
#     chemistry INTEGER,
#     biology INTEGER,
#     geography INTEGER,
#     yoruba INTEGER, 
#     agriculture INTEGER,
#     economics INTEGER
# )
# """

# c.execute(table)
# #check
# print("Table created successfully")

#opening the csv file
with open("results.csv", "r") as waec:
    waecs= csv.reader(waec)
    #Skipping the header
    next(waecs)
    c.executemany (
        """INSERT INTO waec_results 
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", waecs)

#check
print("this was successful")

#commit changes
conn.commit()

#close connection
conn.close()