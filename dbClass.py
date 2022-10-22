from psycopg2 import pool

conn_pool = pool.SimpleConnectionPool(
    1, 20,
    database = "Candles",
    user = "postgres",
    password = "Dancer#1999",
    host = "127.0.0.1",
    port = "5432"
)

class dbClass:

    def __init__(self, table):
        self.table = table
        self.pool = conn_pool

    def select(self, columns, condition = None):
         conn = self.pool.getconn()
         cursor = conn.cursor()

         query = "SELECT %s FROM %s" % (columns, self.table)

         if(condition):
            query = query + " WHERE " + condition
            
         cursor.execute(query)

         return cursor.fetchall()

    def insert(self, columns, values):
        conn = self.pool.getconn()
        cursor = conn.cursor()

        query = "INSERT INTO %s(%s)VALUES(%s)" % (self.table, columns, values)

        cursor.execute(query)
        conn.commit()
        return


    def update(self, to_update, condition):
        conn = self.pool.getconn()
        cursor = conn.cursor()

        query = "UPDATE candles SET %s WHERE %s" % (to_update, condition)

        cursor.execute(query)
        conn.commit()
        return



candlesTable =dbClass("candles")
customerTable = dbClass("customer")

#candlesTable.insert('id_num, candle_name, candle_color, quantity, price', "23234,'Alma', 'Green', 100, 150")

candlesTable.update("candle_name = 'Calm'","id_num = 12121")

rows = candlesTable.select("*")

for row in rows:
    print("id_num: ", row[0])
    print("candle_name: ", row[1])
    print("candle_color: ", row[2])
    print("quantity: ", row[3])
    print("price: ", row[4])
    print("\n")