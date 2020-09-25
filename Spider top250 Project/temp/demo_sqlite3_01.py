import sqlite3

# 1. create a database in RAM
conn = sqlite3.connect("test.db")
print("Open Database Successfully.")

# 2. create a cursor object
cursor = conn.cursor()

# 3. execute sql
# 3.1 create table
cursor.execute("""create table company
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL);""")

print("Table created successfully.")

# 3.2 Insert into 数据
cursor.execute("""INSERT INTO company(ID, NAME, AGE, ADDRESS, SALARY)
                            VALUES(1, 'myles', 32, 'SH', 20000.00)""")

cursor.execute("""INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY) 
                                VALUES(2, 'Alex', 32, 'BJ', 18800.00)
""")
print("Insert Data Successfully.")


# 3.3 select ... from... 查询
rows_lst = cursor.execute("""select * from company""")

print("ID\t|NAME\t|AGE\t|ADDRESS\t|SALARY\t")
for row in rows_lst:
    print("{}\t|{}\t|{}\t|{}\t|{}\t".format(row[0], row[1], row[2], row[3], row[4]))

# 3.4 update...set... 更新
cursor.execute("""UPDATE COMPANY SET SALARY='25000.00' WHERE ID=2 """)
print("Total number of rows updated: {}".format(conn.total_changes))

rows_lst = cursor.execute("SELECT * FROM COMPANY")
print("ID\t|NAME\t|AGE\t|ADDRESS\t|SALARY\t")
for row in rows_lst:
    print("{}\t|{}\t|{}\t|{}\t|{}\t".format(row[0], row[1], row[2], row[3], row[4]))

# 3.5 delete from ... where... 删除
cursor.execute("DELETE FROM COMPANY WHERE ID=2")
print("Total number of rows deleted: {}".format(conn.total_changes))

print("ID\t|NAME\t|AGE\t|ADDRESS\t|SALARY\t")
for row in rows_lst:
    print("{}\t|{}\t|{}\t|{}\t|{}\t".format(row[0], row[1], row[2], row[3], row[4]))

# 3.6 DROP TABLE
cursor.execute("DROP TABLE COMPANY;")

conn.commit()
conn.close()

