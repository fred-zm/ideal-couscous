import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sicheresP@ssw0rt",
    db="test"
)

def insert_termin_into_test():
    datum = input("Datum:")
    land = input("Land:")
    stadt = input("Stadt:")
    val = f"'{datum}','{land}','{stadt}'"

    sql = f"insert into testtermine value ({val})"
    my_cursor.execute(f"{sql}")
    my_db.commit()

my_cursor = my_db.cursor()
insert_termin_into_test()
my_cursor.execute("SELECT * FROM testtermine")
for termin in my_cursor:
    print(termin)