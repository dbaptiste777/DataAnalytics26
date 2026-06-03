6\. Use the Information panel in Workbench to review basic data about each table: 

∗ What is the primary key of the table? 

∗ What are the parent tables of this table? (i.e. What tables do any foreign keys 

reference?) 



A. The primary key of the table is shipper ID, employee ID, region ID, territory ID, supplier ID, product ID, 

B. The parent tables of this table is northwind orders, northwind order detailsm northwind produxts, northwind employeeterritory, and northwind territories.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



7\. Expand the Columns folder under the table in the schema panel. Jot down your notes 

to the below questions in a text or markdown file saved as northwind\_review.txt or 

northwind\_review.md (you can use Notepad on your computer for this). Note: it may 

be helpful to copy and paste the list of questions into your text document first, then 

proceed with answering each question. 



**Tables:**



**Categories:**

Pk:CategoryID

Fk:N/A

I would bring category name and category ID into PowerBI because it identifies 





**Customers:**

Pk:CustomerID

Fk:N/A

I would bring company name, contact name and contact title into PowerBI because it identifies the different vendors that are used in this database.



**Employees:**

Pk:EmployeeID

Fk:N/A

I would bring First name, last name and title.



**EmployeeTerritories:**

Pk:EmployeeID

Fk:FK\_EmployeeTerriroties\_Employees

I would bring this column into PowerBI because it identifies the sales territories that each employee belongs to.





**OrderDetails:**

Pk: OrderID, ProductID

Fk:N/A

I would bring this column into PowerBI because it identifies the prices and the item identifiers.





**Orders:**

Pk:OrderID

Fk:N/A

I would bring Order ID, Order date, and shipped date. This is great information to have when creating visual data for this database.





**Products:**

Pk:ProductID

Fk:N/A

I would bring ProductName, quantity per unit, unit price as relevant columns for PowerBI.





.This is great information to have when creating visual data for this database.





**Region:**

Pk:RegionID

Fk:

I would bring the region description column. This is great information to have when creating visual data for this database to separate territories.



**Shippers:**

Pk:ShipperID

Fk:

I would bring ShipperID and CompanyName. This is great information to have when cleaning the database.



**Suppliers:**

Pk:SupplierID

Fk:N/A

I would bring supplierID, CompanyName, ContactName, and ContactTitle. This is great information to have when creating visual data for this database.





**Territories:**

Pk:Territory

Fk:N/A

I would bring territoryID and the regionID into power BI since it identifies where the pro







