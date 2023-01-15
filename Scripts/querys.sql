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
# ----------------------------------

# 3- Listing orders
	# 3.1 - List all orders of a certain day
DELIMITER $$
CREATE PROCEDURE orders_on_day
	(day_nr INT, month_nr INT)
BEGIN
SELECT * FROM dorlux.order
	WHERE year(orderDate) = day_nr AND month(orderDate) = month_nr;
END $$
CALL orders_on_day(2023, 1);
    
    # 3.2 - List Orders of a especific category in a specific status
DELIMITER $$
CREATE PROCEDURE list_order_in_category_status(category_nr INT, status_name VARCHAR(200))
BEGIN
SELECT * FROM
	dorlux.order AS Orders INNER JOIN order_has_Item AS Ord_has_item
		ON Orders.idOrder = Ord_has_item.Order_idOrder
	INNER JOIN Item AS It
		ON It.idItem = Ord_has_item.Item_idItem
	WHERE category = category  AND status = status_name;
END
$$
CALL list_order_in_category_status(2, 'PENDING');

    # 3.3 - List all orders Processed with address attached
SELECT idOrder, status, orderDate, idClient, VAT, street, zipCode, city FROM
	dorlux.order AS Orders INNER JOIN dorlux.client AS Cl
		ON Orders.Client_idClient = Cl.idClient
	INNER JOIN Client_has_Address AS cl_has_addr
		ON cl_has_addr.Client_idClient = Cl.idClient 
	INNER JOIN Address AS addr
		ON cl_has_addr.Address_idAdress = addr.idAdress
	WHERE status = 'PROCESSED';
	
    
    
# 4- Employees
	# 4.1 - List all orders attached to a certain Employee
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






# Miguel: 1 and 2
# Hugo: 7 and 8 
# Ianni boy: 5
# Quintela: 3 and 4
# 6 - global 


# 1- Change order status and update the responsible employee for the order
    # 1.1 - Pending to Processed
    # 1.2 - Processed to Delivering
    # 1.3 - Delivering to Delivered
    # 1.4 - From anything to Canceled

# 2- Register requirement - Create a new client
    # 2.1 - Delete a client
    # 2.2 - Update a client

# 3- Listing orders
	# 3.1 - List all orders of a certain day
    # 3.2 - Listing Pending Orders of a especific category
    # 3.3 - List all orders Processed for delivery with address attached
    
# 4- Employees
	# 4.1 - List all orders attached to an certain Employee

# 5- Client
	# 5.1 - List all orders made by a Client
    # 5.2 - List top 10 Clients
	
# 6- Order Manipulation
	# Develop a trigger that decrease the stockNr when an order is made and increases when an order is cancelled
    

# 7- Supliers
	# 7.1 - How many items do we bought from suppliers, and which ones
    
# 8 - Items
	# 8.1 - List the current stock