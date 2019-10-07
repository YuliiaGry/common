from typing import List
import psycopg2
import os

def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    with con.cursor() as cur:
        cur.execute("INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)"
                "VALUES  ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore');")


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    with(cur):
        cur.execute('SELECT * FROM Customers;')
        return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    with(cur):
        cur.execute("SELECT * FROM Customers WHERE Country = 'Germany';")
        return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """

    with con.cursor() as cur:
        cur.execute("UPDATE Customers SET CustomerName = 'Johnny Depp' "
                    "WHERE CustomerId = (SELECT MIN(CustomerID) "
                    "FROM Customers);")

def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    with con.cursor() as cur:
        cur.execute("DELETE FROM Customers "
                    "WHERE CustomerId = (SELECT MAX( CustomerID) From Customers);")

def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    with cur:
        cur.execute("SELECT Country FROM suppliers;")
        return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    with cur:
        cur.execute("SELECT Country FROM suppliers ORDER BY Country DESC;")
        return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    with cur:
        cur.execute("SELECT COUNT(CustomerId) as count, City FROM Customers GROUP BY City ;")
        return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    with cur:
        cur.execute('SELECT a.Country, a.count FROM '
                    '(SELECT Country, Count(Customerid) AS count FROM Customers GROUP BY Country) as a where a.count > 10;')
        return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    with cur:
        cur.execute("SELECT * FROM Customers LIMIT 10;")
        return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    with cur:
        cur.execute('SELECT * FROM Customers WHERE CustomerID>11;')
        return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    with cur:
        cur.execute("SELECT supplierid, suppliername, contactname, city, country "
                    "FROM suppliers "
                    "WHERE country in ('USA', 'UK', 'Japan'); ")
        return cur.fetchall()



def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    with cur:
        cur.execute("SELECT b.ProductName FROM products as b "
                    "INNER JOIN suppliers as a on a.supplierid = b.supplierid WHERE a.country='Sweden';")
        return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    with cur:
        cur.execute("SELECT b.ProductId, b.ProductName, b.Unit, b.Price, a.Country, a.City, a.SupplierName "
                    "FROM products as b INNER JOIN suppliers as a on  a.supplierid = b.supplierid;")
        return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    with cur:
        cur.execute("SELECT a.customername, a.contactname, a.country, b.orderid "
                    "FROM customers a FULL OUTER JOIN orders AS b ON a.customerId=b.customerId;")
        return cur.fetchall()

def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    with cur:
        cur.execute("SELECT a.CustomerName, a.address, a.Country as customercountry, b.Country  as suppliercountry, b.SupplierName "
                    "FROM customers as a FULL JOIN suppliers b ON  a.country = b.country ORDER BY a.country,b.country;")
        return cur.fetchall()

