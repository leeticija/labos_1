import sqlite3

CREATE_INSECT_TABLE = """
  CREATE TABLE IF NOT EXISTS insect(
    id INTEGER NOT NULL PRIMARY KEY,
    genus TEXT,
    species TEXT,
    binomial_name TEXT,
    order_id INTEGER
  );
  """

CREATE_ORDER_TABLE = """
  CREATE TABLE IF NOT EXISTS insect(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT,
    common_name TEXT,
    wings TEXT,
    regeneration TEXT,
    total_species INTEGER,
    number_of_families INTEGER,
    metamorphosis TEXT
  );
  """

SELECT_INSECT = """
SELECT ? FROM insect;
"""

INSERT_INTO_INSECT = """
INSERT INTO insect(genus, species, binomial_name, order_id) VALUES('Mantis', 'religiosa', 'Mantis religiosa', 2);
INSERT INTO insect(genus, species, binomial_name, order_id) VALUES('Anax', 'imperator', 'Anax imperator', 3);
"""

FILE = "insects.db"

def insert():
  #cursor.executemany("""
  #  INSERT INTO some_table ('item_num', 'item_name')
  #  VALUES (?, ?)""", values_to_insert)
  return

def fill_database(connection):
  print("Filling database...")
  cursor = connection.cursor()
  cursor.executescript(CREATE_INSECT_TABLE)
  cursor.executescript(INSERT_INTO_INSECT)

def select(connection, table, columns):
  print("Selecting from insect...")
  what = ",".join(columns)
  print("selectam columne: ", what)
  cursor = connection.cursor()
  cursor.execute(SELECT_INSECT, ('genus'))
  return cursor.fetchall()

try:
  conn = sqlite3.connect(FILE)
  print("Connected to database!")
  fill_database(conn)
  print(select(conn, 'insect', ['*']))
  #cursor = conn.cursor()
  #cursor.execute(select_insects_query)

  #result = cursor.fetchall()
  #print("cursor result: ", result)
  #cursor.close()

except sqlite3.Error as error:
  print("Database sqlite.db not formed.")
  print(error)
finally:
  #conn.commit()
  conn.close()