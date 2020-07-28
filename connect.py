import sqlite3


def connect(dbname):
    conn=sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS OLX_BIKE (PRICES TEXT, YEAR TEXT, TITLE TEXT, ADDRESS TEXT)")
    print("Table successfully created!:")
    conn.close()

def insert_into_table(dbname,values):
    conn=sqlite3.connect(dbname)
    print("inserted into tables:"+str(values))
    insert_sql="INSERT INTO OLX_BIKE (PRICEs, YEAR, TITLE, ADDRESS) VALUES (?, ?, ?, ?) "
    conn.execute(insert_sql, values)
    conn.commit()#make chnages then commit
    conn.close()

def get_bike_info(dbname):
    conn =sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM OLX_BIKE_RX100")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
