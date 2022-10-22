import psycopg2

conn = psycopg2.connect(
    database = "Candles",
    user = "postgres",
    password = "Dancer#1999",
    host = "127.0.0.1",
    port = "5432"
)

cursor = conn.cursor() 
  #create table
#cursor.execute('''CREATE TABLE customer(
    #customer_Id INT PRIMARY KEY,
    #customer_name TEXT not null
#);''')
#print("Table Created")

 #insert data
#cursor.execute('''INSERT INTO customer(customer_id, customer_name)
    #VALUES(1, 'Maria');''')
#print("Data Added")

 #get data
#cursor.execute('''SELECT * FROM customer''')
#rows = cursor.fetchall()

 #loop through rows
#for row in rows:
    #print("customer_id: ", row[0])
    #print("customer_name: ", row[1])


cursor.execute('''SELECT * FROM candles''')
rows = cursor.fetchall()

 #loop through rows
for row in rows:
    print("id_num: ", row[0])
    print("candle_name: ", row[1])
    print("candle_color: ", row[2])
    print("quantity: ", row[3])
    print("price: ", row[4])
    print("\n")

print("Done")

conn.commit()
conn.close() 