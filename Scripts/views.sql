-- Creating Clients View
CREATE VIEW Clients 
AS
	SELECT idClient AS "Id", name AS "Name",  phone AS "PhoneNr", street AS "Street", zipCode AS "ZipCode", city AS "City"
    FROM client AS cl INNER JOIN contact AS cont
		ON cl.contact = cont.idContact
	INNER JOIN Client_has_Address AS Cl_has_addr
		ON cl.idClient = Cl_has_addr.Client_idClient
	INNER JOIN Address AS Addr
		ON Cl_has_addr.Address_idAdress = Addr.idAdress
	ORDER BY name ASC;
    
-- Select View Clients
SELECT * FROM Clients;
    
-- Drop View Clients
DROP VIEW Clients;