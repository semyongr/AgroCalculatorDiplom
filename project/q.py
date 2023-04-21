from connection import *

cursor = connection.cursor()
cursor.execute("SELECT * FROM fertilizers")
rows = cursor.fetchall()

for row in rows:
   print("{0} {1} {2}".format(row[0], row[1], row[2]))



connection.close()