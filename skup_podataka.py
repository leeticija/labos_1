import sqlite3

CREATE_INSECTS_TABLE = """
  CREATE TABLE IF NOT EXISTS insects(
    id INTEGER NOT NULL PRIMARY KEY,
    genus TEXT,
    specie TEXT,
    binomial_name TEXT,
    order_id INTEGER NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(id)
  );
  """

CREATE_ORDERS_TABLE = """
  CREATE TABLE IF NOT EXISTS orders(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT,
    common_name TEXT,
    wings TEXT,
    total_species INTEGER,
    total_families INTEGER,
    metamorphosis TEXT
  );
  """

SELECT_INSECT = """
SELECT %s FROM %s;
"""

INSERT_ALL_INTO_INSECTS = """
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Mantis', 'religiosa', 'Mantis religiosa', 9);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Anax', 'imperator', 'Anax imperator', 4);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Allacrotelsa', 'spinulata', 'Allacrotelsa spinulata', 2);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Petrobius', 'brevistylus', 'Petrobius brevistylus', 1);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Caenis', 'hilaris', 'Caenis hilaris', 3);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Alloperla', 'petasata', 'Alloperla petasata', 5);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Timema', 'californicum', 'Timema californicum', 6);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Arethaea', 'phantasma', 'Arethaea phantasma', 7);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Forficula', 'auricularia', 'Forficula auricularia', 8);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Parcoblatta', 'americana', 'Parcoblatta americana', 10);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Tenodera', 'sinensis', 'Tenodera sinensis', 9);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Argia', 'emma', 'Argia emma', 4);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Pseudosermyle', 'catalinae', 'Pseudosermyle catalinae', 6);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Utaperla', 'gaspesiana', 'Utaperla gaspesiana', 5);
INSERT INTO insects(genus, specie, binomial_name, order_id) VALUES('Eurycotis', 'floridiana', 'Eurycotis floridiana', 10);

"""

INSERT_ALL_INTO_ORDERS = """
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Microcoryphia', 'Bristletails', 'None', 450, 2, 'None');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Zygentoma', 'Silverfish, Firebrats', 'None', 370, 5, 'None');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Ephemeroptera', 'Mayflies', 'Two pair', 2000, 19, 'Incomplete');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Odonata', 'Damselflies, Dragonflies', 'Two pair', 5000, 29, 'Incomplete');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Plecoptera', 'Stoneflies', 'Two pair', 2000, 10, 'Incomplete');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Phasmida', 'Walkingsticks', 'Wings either greatly reduced or lacking', 3000, 2, 'Gradual');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Orthoptera', 'Crickets, Grasshoppers, and Katydids', 'Two pair or wingless', 24000, 29, 'Gradual');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Dermaptera', 'Earwigs', 'Two pair or wingless', 2000, 8, 'Gradual');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Mantodea', 'Mantids', 'Two pair or wingless', 1800, 8, 'Gradual');
INSERT INTO orders(name, common_name, wings, total_species, total_families, metamorphosis) VALUES('Blattodea', 'Cockroaches and termites', 'Two pair or wingless', 4000, 5, 'Gradual');
"""

FILE = "insects.db"

def fill_database(connection):
  print("Filling database...")
  cursor = connection.cursor()
  cursor.executescript(CREATE_ORDERS_TABLE)
  print("created orders table")
  cursor.executescript(CREATE_INSECTS_TABLE)
  print("created insects table")
  cursor.executescript(INSERT_ALL_INTO_ORDERS)
  print("inserted into orders table")
  cursor.executescript(INSERT_ALL_INTO_INSECTS)
  print("inserted into insects table")

def select(connection, table, columns):
  print("Selecting from insect...")
  what = ",".join(columns)
  print("selectam columne: ", what, " iz tablice: ", table)
  cursor = connection.cursor()
  cursor.execute(SELECT_INSECT %(what, table))
  return cursor.fetchall()

try:
  conn = sqlite3.connect(FILE)
  print("Connected to database!")
  fill_database(conn)
  print(select(conn, 'insects', ['genus, specie']))

except sqlite3.Error as error:
  print("Database sqlite.db not formed.")
  print(error)

finally:
  conn.close()