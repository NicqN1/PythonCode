import sqlite3
conn = sqlite3.connect('Fastcars.sqlite')
def create_top3_db():
    conn.execute("CREATE TABLE Cars(id INTEGER PRIMARY KEY, Name TEXT, TopSpeed INT)")
    conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Koenigsegg Agera R','273')")
    conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Hennessey Venom GT','270')")
    conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Bugatti Veyron','268')")