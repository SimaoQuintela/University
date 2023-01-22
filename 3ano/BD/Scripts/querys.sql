# FETCH ALL DATA FROM THE DATABASE
USE dorlux;

SELECT * FROM dorlux.order;
SELECT * FROM category;
SELECT * FROM client;
SELECT * FROM address;
SELECT * FROM client_has_address;
SELECT * FROM contact;
SELECT * FROM employee;
SELECT * FROM item;
SELECT * FROM order_has_item;
SELECT * FROM suplier;
SELECT * FROM suplier_provide_item;

DROP SCHEMA dorlux;

# RM01 - Anything to Processed
# RM02 - Anything to Delivering
# RM03 - Anything to Delivered
# RM04 - Anything to Canceled
DELIMITER $$
CREATE PROCEDURE change_order_status(status_name VARCHAR(200), idOrder_nr INT)
BEGIN
UPDATE dorlux.order
    SET dorlux.order.status = status_name , dorlux.order.upDate = NOW()
    WHERE idOrder = idOrder_nr;
END $$
CALL change_order_status('DELIVERED', 2)
CALL change_order_status('PROCESSED', 3)
CALL change_order_status('CANCELED', 4)
CALL change_order_status('DELIVERING', 5)

-- RM5 - List all orders of a certain year in a certain month
DROP PROCEDURE orders_on_year_month
-- -----------------------------------------------------------
DELIMITER $$
CREATE PROCEDURE orders_on_year_month(year_nr INT, month_nr INT)
BEGIN
SELECT * FROM dorlux.order
	WHERE year(orderDate) = year_nr AND month(orderDate) = month_nr;
END $$
CALL orders_on_year_month(2023, 1);
    
-- RM6 - List Orders of a especific category in a specific status
DROP PROCEDURE orders_on_year_month;
DELIMITER $$
CREATE PROCEDURE list_order_in_category_status(category_nr INT, status_name VARCHAR(200))
BEGIN
SELECT * FROM
	dorlux.order AS Orders INNER JOIN order_has_Item AS Ord_has_item
		ON Orders.idOrder = Ord_has_item.Order_idOrder
	INNER JOIN Item AS It
		ON It.idItem = Ord_has_item.Item_idItem
	WHERE category = category_nr  AND status = status_name;
END
$$

CALL list_order_in_category_status(2, 'PENDING');
CALL list_order_in_category_status(1, 'PROCESSED');

-- RM07 - List all orders Processed with address attached
SELECT idOrder, status, orderDate, idClient, VAT, street, zipCode, city FROM
	dorlux.order AS Orders INNER JOIN dorlux.client AS Cl
		ON Orders.Client_idClient = Cl.idClient
	INNER JOIN Client_has_Address AS cl_has_addr
		ON cl_has_addr.Client_idClient = Cl.idClient 
	INNER JOIN Address AS addr
		ON cl_has_addr.Address_idAdress = addr.idAdress
	WHERE status = 'PROCESSED';
	
# RM08 - List all orders attached to a certain Employee
DELIMITER $$
CREATE PROCEDURE list_orders_attached_to_employee(employee_id INT)
BEGIN
SELECT idOrder, status, shippingPrice, orderDate, idEmployee, salary FROM
	dorlux.order AS Orders INNER JOIN employee as Emp
		ON Orders.Employee = Emp.idEmployee
	WHERE idEmployee = employee_id;
END
$$
CALL list_orders_attached_to_employee(2)

# RM09 - What orders a client have made ?
DELIMITER $$
CREATE PROCEDURE orders_of_client(idClient_nr INT)
BEGIN
SELECT 
	cont.name AS UserName,
    tab_ord.idOrder AS idOrder,
    tab_ord.status AS Status
    FROM
dorlux.Order AS tab_ord INNER JOIN Order_has_Item AS ord_has_it
		ON tab_ord.idOrder = ord_has_it.order_idOrder
	INNER JOIN Item AS it
		ON ord_has_it.Item_idItem = it.idItem
	INNER JOIN dorlux.Client AS Cl
		On tab_ord.Client_idClient = Cl.idClient
	INNER JOIN contact AS cont
		ON Cl.contact = cont.idContact
	WHERE Cl.idClient = idClient_nr;
END
$$
CALL orders_of_client(1)

# RM10 - Top X clients
DELIMITER $$
CREATE PROCEDURE top_X_clients(top_limit INT)
BEGIN
SELECT Cl.idClient AS "idClient", cont.name AS "Nome", it.priceSell*ord_has_it.amount AS ValorGasto FROM 
	dorlux.Order AS tab_ord INNER JOIN Order_has_Item AS ord_has_it
		ON tab_ord.idOrder = ord_has_it.order_idOrder
	INNER JOIN Item AS it
		ON ord_has_it.Item_idItem = it.idItem
	INNER JOIN dorlux.Client AS Cl
		On tab_ord.Client_idClient = Cl.idClient
	INNER JOIN contact AS cont
		ON Cl.contact = cont.idContact
	
    GROUP BY Order_idOrder
    ORDER BY ValorGasto DESC
	LIMIT top_limit;
END
$$
CALL top_X_clients(10);
CALL top_X_clients(20);
CALL top_X_clients(30);

# RM11 - How many items do we bought from a supplier
DELIMITER $$
CREATE FUNCTION  fuItemsCompradosForn(vatForn INT)
         RETURNS INT
         DETERMINISTIC
BEGIN
    DECLARE numeroitems INT;
    SELECT COUNT(I.idItem) INTO numeroitems FROM item AS I
         INNER JOIN suplier_provide_item AS SPI
             ON I.idItem = SPI.Item_idItem
         INNER JOIN suplier AS S
             ON SPI.Suplier_VAT = S.VAT
         WHERE S.VAT = vatForn;
    RETURN numeroitems;
END $$
SELECT fuItemsCompradosForn(795294490)

# RM11 - Which items we bought from a supplier
DROP PROCEDURE spQuaisItemsForn; 

DELIMITER $$
CREATE PROCEDURE spQuaisItemsForn(vatForn INT)
BEGIN
    SELECT I.name, I.description FROM item AS I
         INNER JOIN suplier_provide_item AS SPI
             ON I.idItem = SPI.Item_idItem
         INNER JOIN suplier AS S
             ON SPI.Suplier_VAT = S.VAT
         WHERE S.VAT = vatForn;
END $$
CALL spQuaisItemsForn(795294490);

# RM12 - List the current stock
SELECT I.name, I.description, I.stockNr FROM Item AS I


# RM-13 - Orders items by stock number
SELECT * FROM Item
	ORDER BY stockNr DESC

# RM-14 - Order categories by name
SELECT * FROM category
	ORDER BY name ASC

# RM-15 - Order employees by salary
SELECT * FROM employee
	ORDER BY salary DESC
