/* write a query to list the product id, product name, and unit price of every product that Northwind sells. (Hint: To help
set up your query, look at the schema preview to see what column names belong to each table. Or use SELECT * to query all columns
first, then refine your query to just the columns you want.) */

SELECT productid, productname, unitprice FROM products;

-- Write a query to identify the products where the unit price is $7.50 or less. --

SELECT productname, unitprice FROM products WHERE unitprice <= 7.50;

/* What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? 
Write a query that answers this question. */ 

SELECT productname, unitsinstock, unitsonorder FROM products  WHERE unitsinstock = 0 AND unitsonorder >= 1;

/* Examine the products table. How does it identify the type (category) of each item
sold? Where can you find a list of all categories? Write a set of queries to answer these
questions, ending with a query that creates a list of all the seafood items we carry. */

SELECT p.productname, FROM products JOIN categories ON categoryid WHERE categoryname= 'seafood'

/* Examine the products table again. How do you know what supplier each product
comes from? Where can you find info on suppliers? Write a set of queries to find the
specific identifier for "Tokyo Traders" and then find all products from that supplier.*/

SELECT SupplierID, CompanyName FROM suppliers WHERE CompanyName = 'Tokyo Traders';

SELECT ProductID, ProductName, SupplierID FROM products WHERE SupplierID = 4;

SELECT p.ProductID, p.ProductName, s.CompanyName FROM products AS p INNER JOIN suppliers AS s ON p.SupplierID = s.SupplierID WHERE s.CompanyName = 'Tokyo Traders';


/* How many employees work at northwind? What employees have "manager"
somewhere in their job title? Write queries to answer each question. */

SELECT * FROM employees; SELECT COUNT(EmployeeID) FROM employees; 
SELECT EmployeeID, FirstName, LastName, Title FROM employees WHERE Title LIKE '%manager%';
 