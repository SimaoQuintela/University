USE dorlux;

SELECT * FROM dorlux.order;
SELECT * FROM category;
SELECT * FROM client;
SELECT * FROM client_has_address;
SELECT * FROM contact;
SELECT * FROM employee;
SELECT * FROM item;
SELECT * FROM order_has_item;
SELECT * FROM suplier;
SELECT * FROM suplier_provide_item;

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