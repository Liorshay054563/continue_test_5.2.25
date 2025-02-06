import sqlite3

# Test 5.2.2025
# part c

def connect_sql(db_name):
    """Connect to SQL"""
    conn = sqlite3.connect(db_name)  # creates a connector
    conn.row_factory = sqlite3.Row  # allow me to use column name
    cursor = conn.cursor()  # creates a cursor
    return conn,cursor

def read_table(cursor,query):
    """show the output of query"""
    cursor.execute(query)
    rows = cursor.fetchall()
    result_list = [list(row) for row in rows]
    return result_list


def change_table(conn,cursor,query, parameters):
    cursor.execute(query,parameters)
    conn.commit()  # save into the db file

conn, cursor = connect_sql('Test_5.2.25 movies.db')

# 4)
# א
print(read_table(cursor,"""select * from movies"""))

# ב
movie_name = input("Enter movie name: ")
print(read_table(cursor,f"""select * from movies
where movie_name like '%{movie_name}%'"""))

# ג
values = [input("Enter movie name: "), input("Enter genre: "), input("Enter country: "), input("Enter language: "),
          input("Enter year: "), input("Enter revenue: ")]
print(values)
change_table(conn,cursor,"""insert into movies (movie_name,genre,country,language,year,revenue)
values (?,?,?,?,?,?)""",values)

