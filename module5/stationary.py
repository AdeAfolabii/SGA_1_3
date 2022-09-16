import sqlite3
#create a connection
conn = sqlite3.connect('produces.db')
#create a cursor object
c = conn.cursor()
#check
print( 'All successful')

stationaries_list= [
    ("123", "pencil", "1.50", "22"),
    ("321", "pen", "7.50", "20"),
    ("214", "Eraser", "2.00", "10"),
    ("143", "Notebook", "3.00", "12"),
    ("412", "Ruler",    "1.50", "5"),
    ("124", "Crimp",    "0.50", "2"),
    ("121", "Tack",    "1.20", "33"),
    ("221",  "Glue",    "2.50", "1"),
    ("1234", "stamps", "8.50", "15"),
    ("4321", "Drive", "6.50", "27"),
    ("3214", "Cord",    "4.50", "3"),
    ("3412", "Folder", "5.00", "23"),
    ("2135", "Paper",  "10.50", "156"),
    ("1254", "Ipad",  "30.70", "12"),
    ("0407", "Clip", "1.10", "37")
]

c.executemany( """ INSERT INTO stationaries VALUES (?, ?, ?, ?) """, stationaries_list )

c.execute("SELECT * FROM stationaries")
#check
print("successful")

# Calculate the amount the business owner invested in the procurement of the items.
query =""" 
    SELECT item_id, SUM (cost_price)
    FROM stationaries;
    """

c.execute(query)
items=c.fetchall()
print(f"{'-' * 40}\nitem_id \t total_cost\n{'-' * 40}")
for item in items:
     item_id, total_cost = item
     print(f"{item_id}\t{total_cost}")


#the average quantity of items in stock.
query1 = """
SELECT item_id, AVG(quant_in_stock)
FROM stationaries;
"""

c.execute(query1)
items=c.fetchall()
print(f"{'-' * 40}\nitem_id\tquant_in_stock\n{'-' * 40}")
for item in items:
     item_id, quant_in_stock = item
     print(f"{item_id}\t{quant_in_stock}")

# the item with the least quantity in stock
query2= """ 
    SELECT item_id, name, MIN (quant_in_stock)
    FROM stationaries
    """

c.execute(query2)
items=c.fetchall()
print(f"{'-' * 40}\nitem id \tname\tleast item in stock\n{'-' * 40}")
for item in items:
    item_id, name, quant_in_stock = item
    print(f"{item_id}\t  {name} \t {quant_in_stock}")


#the item with the most quantity in stock
query3= """ 
    SELECT item_id, name, MAX (quant_in_stock)
    FROM stationaries
    """

c.execute(query3)
items=c.fetchall()
print(f"{'-' * 40}\nitem id \tname\tmost item in stock\n{'-' * 40}")
for item in items:
    item_id, name, quant_in_stock = item
    print(f"{item_id}\t  {name} \t {quant_in_stock}")

#commit
conn.commit()
#close
conn.close()