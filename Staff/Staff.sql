charset utf8;
DROP DATABASE IF EXISTS Staff;  
CREATE DATABASE Staff;
USE Staff;
DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee
(	
	EmployeeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 	
	Staff_Name VARCHAR(150) NOT NULL,   
	Staff_Status BIT,
	Staff_Post VARCHAR(50),
    Staff_Schedule ,
    Staff_Salary 
);

