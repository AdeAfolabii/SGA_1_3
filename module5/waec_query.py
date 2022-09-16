import sqlite3
import csv

# connect a connection
conn=sqlite3.connect('results.db')

#check
print('success')

#create cursor
c=conn.cursor()

#check
print('success')

#query
query="""
SELECT * FROM waec_results
"""

c.execute(query)

#check
print('success')

#fetch items
items= c.fetchall()
print(f" {'-' * 70}\nid\t name\tmaths\tenglish\tphysics\tchemistry\tbiology\tgeography\tyoruba\tagriculture\teconomics\n{'-' * 70}")
for item in items:
     id, name, maths, english, physics, chemistry, biology, geography, yoruba, agriculture, economics = item
     print(f"{id}\t{name}\t{maths}\t{english}\t{physics}\t{chemistry}\t{biology}\t{geography}\t\t{yoruba}\t{agriculture}\t{economics}")

# person with highest in maths
def highest_math_scorer(query = "SELECT id, name, MAX(maths) FROM waec_results"):
    c.execute(query)
    items =c.fetchall()
    print(f"{'-' * 50} \n ID\t NAME\t SCORE\n {'-' * 50} \n")
    for item in items:
        id, name, score =items
    print(f"{id} \t {name} \t {score}")
    print(item)

highest_math_scorer()

#commit changes
conn.commit
#close
conn.close

#lowest in english
def lowest_in_english(query = "SELECT id, name, MIN(english) FROM waec_results"):
    c.execute(query)
    items =c.fetchall()
    print(f"{'-' * 50} \n ID\t NAME\t SCORE\n {'-' * 50} \n")
    for item in items:
        id, name, score =items
    print(f"{id} \t {name} \t {score}")
    print(item)

lowest_in_english()

#commit changes
conn.commit
#close
conn.close

#Avg score of student in maths
def avr_math_score(query = "SELECT AVG(maths) FROM waec_results"):
    c.execute(query)
    items =c.fetchall()
    print(f"{'-' * 50} \n ID\t NAME\t SCORE\n {'-' * 50} \n")
    for item in items:
        id, name, score =items
    print(f"{id} \t {name} \t {score}")
    print(item)

avr_math_score()

#commit changes
conn.commit
#close
conn.close

#Avg score of student in english
def avr_english_score(query = "SELECT AVG(english) FROM waec_results"):
    c.execute(query)
    items =c.fetchall()
    print(f"{'-' * 50} \n ID\t NAME\t SCORE\n {'-' * 50} \n")
    for item in items:
        id, name, score =items
    print(f"{id} \t {name} \t {score}")
    print(item)

avr_english_score()

#commit changes
conn.commit
#close
conn.close

#best performing student across all nine subjects in terms of overall scores
def best_student_in_all(query = "SELECT id, name, MAX(maths + english+ physics+ chemistry + biology+ geography + yoruba+ agriculture+ economics FROM waec_results"):
    c.execute(query)
    items =c.fetchall()
    print(f"{'-' * 50} \n ID\t NAME\t SCORE\n {'-' * 50} \n")
    for item in items:
        id, name, score =items
    print(f"{id} \t {name} \t {score}")
    print(item)

best_student_in_all()

#best performing student across all nine subjects in terms of average scores
def best_avr_student_in_all(query = "SELECT id, name, AVG(maths + english+ physics+ chemistry + biology+ geography + yoruba+ agriculture+ economics FROM waec_results"):
    c.execute(query)
    items =c.fetchall()
    print(f"{'-' * 50} \n ID\t NAME\t SCORE\n {'-' * 50} \n")
    for item in items:
        id, name, score =items
    print(f"{id} \t {name} \t {score}")
    print(item)

best_avr_student_in_all()

