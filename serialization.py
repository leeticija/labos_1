import sqlite3
import csv 
import json
import pprint

SELECT_ALL_FROM_ORDERS_AND_JOIN_INSECTS = """
SELECT genus, specie, binomial_name, order_id, order_name, common_name, wings, total_species, total_families, metamorphosis
FROM orders
JOIN insects
WHERE insects.order_id = orders.id;
"""

SELECT_ALL_FROM_ORDERS = """SELECT id FROM orders;"""

SELECT_INSECTS_BY_ORDER_ID = """
SELECT * FROM insects
WHERE order_id = ?;
"""

SELECT_FROM_ORDER_BY_ID = """
SELECT * FROM orders WHERE id = ?;
"""

def selectAll(connection):
  print("Selecting and joining...")
  cursor = connection.cursor()
  cursor.execute(SELECT_ALL_FROM_ORDERS_AND_JOIN_INSECTS)
  return cursor.fetchall()

def getOrderIds(connection):
  cursor = connection.cursor()
  cursor.execute(SELECT_ALL_FROM_ORDERS)
  return cursor.fetchall()

def getInsectsByOrderId(connection, order_id):
  cursor = connection.cursor()
  cursor.execute(SELECT_INSECTS_BY_ORDER_ID, [order_id])
  return cursor.fetchall()

def getOrderData(connection, id):
  cursor = connection.cursor()
  cursor.execute(SELECT_FROM_ORDER_BY_ID, [id])
  return cursor.fetchall()

def getInsectJson(insect_result_set):
  j = {}
  j["id"] = insect_result_set[0]
  j["genus"] = insect_result_set[1]
  j["specie"] = insect_result_set[2]
  j["binomial_name"] = insect_result_set[3]
  j["order_id"] = insect_result_set[4]
  return j

def getFilledJson(order_data, insects):
  j = {}
  j["id"] = order_data[0]
  j["order_name"] = order_data[1]
  j["common_name"] = order_data[2]
  j["wings"] = order_data[3]
  j["total_species"] = order_data[4]
  j["total_families"] = order_data[5]
  j["metamorphosis"] = order_data[6]
  j["examples"] = []
  for insect in insects:
    j["examples"].append(getInsectJson(insect))
  return j

full_list = []
FILE = "insects.db"
pp = pprint.PrettyPrinter(indent=4)
try:
  conn = sqlite3.connect(FILE)
  print("Connected to database!")
  orders = getOrderIds(conn)
  #print(insects)
  for i in orders:
    order_data = getOrderData(conn, i[0])
    print(order_data)
    insects = getInsectsByOrderId(conn, i[0])
    jsn = getFilledJson(order_data[0], insects)
    pp.pprint(jsn)
    full_list.append(jsn)

except sqlite3.Error as error:
  print("Database error.")
  print(error)

finally:
  conn.close()

with open("insects.json", "w") as outfile:
  full_json = {}
  full_json["database"] = full_list
  outfile.write(json.dumps(full_json, indent=4))
