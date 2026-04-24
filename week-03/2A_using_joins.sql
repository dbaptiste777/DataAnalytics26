/* Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name. */

SELECT p.productid, p.productname, p.unitprice, c.categoryid 
FROM products AS  p JOIN categories AS c 
ON p.categoryid = cProductID.categoryid ORDER BY c.categoryname, p.productname; 

/* Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name. */

SELECT p.productid, p.productname, p.unitprice, s.companyname
FROM products AS p JOIN suppliers AS s
ON p.supplierid = s.supplierid
WHERE p.unitprice > 75
ORDER BY p.productname;  

/* Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name. */

SELECT 
    p.productid,
    p.productname,
    p.unitprice,
    c.categoryname,
    s.companyname AS suppliername
FROM products AS p
JOIN suppliers AS s 
    ON p.supplierid = s.supplierid
JOIN categories AS c 
    ON p.categoryid = c.categoryid
ORDER BY p.productname;

/* Create a single query to list the order id, ship name, ship address, and shipping
company name of every order that shipped to Germany. Assign the shipping company
name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
shipped to. */

SELECT 
    o.orderid,
    o.shipname,
    o.shipaddress,
    s.companyname AS Shipper
FROM orders AS o
JOIN shippers AS s
    ON o.shipvia = s.shipperid
WHERE o.shipcountry = 'Germany'
ORDER BY Shipper, o.shipname;


/* Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name. */

SELECT o.ShipName, o.ShipAddress,
		s.CompanyName AS Shipper,
        COUNT(*) AS OrderCount
FROM orders AS o
INNER JOIN shippers AS s
	ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName,
			o.ShipAddress,
            s.CompanyName
ORDER BY Shipper, o.ShipName;


/* Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale.
∗ Hint: You will need to join on three tables to accomplish this. (One of these tables
has a sneaky space in the name, so you will need to surround it with backticks, like
this: `table name`) */

SELECT 
    o.orderid,
    o.orderdate,
    o.shipname,
    o.shipaddress
FROM Orders o
JOIN `Order Details` od
    ON o.orderid = od.orderid
JOIN Products p
    ON od.productid = p.productid
WHERE p.productname = 'Sasquatch Ale';


