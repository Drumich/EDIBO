make database and show it through angular       


WHEN CONNECTED THROUGH SSH >
mysql -u user -p  < aA1!...          
    
------------------------------------------------------------------  
CREATE TABLE ediboKG5(id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20),lastname VARCHAR(20),age INT NOT NULL DEFAULT 420,date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);                     
ALTER TABLE ediboKG ADD age INT NOT NULL; - add a column to a table                             
      
  
      
- UPDATE edibo SET location = "USA" WHERE name = "Donald"   - updates tables location for Donald    
- ALTER TABLE edibo MODIFY location VARCHAR(20) NOT NULL DEFAULT "Riga";      


INSERT INTO ediboKG3(name,lastname,age,date) VALUES("Kriss","G",69,now());          
SELECT DATE_FORMAT(date, "%d/%m/%Y") FROM ediboKG3;         
SELECT age as "kaut kads numurs",date as datums FROM ediboKG3;  
select name as Vards,age as Vecums,date as Datums from ediboKG3 WHERE name = "Kriss";

    
------------------------------------------------------------------    
show database/s     
use databasename; - switches to database          
show grants; - shows what you can do              
show tables; - shows tables             
describe tablename; - shows details about this table        
delimiter $$ - changes execute ; to $$         



------------------------------------------------------------------    
!if column doesn't allow nulls and you don't enter a value,then column uses DEFAULT values provided!            
example CREATE TABLE asd(date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);     






















------------------------------------------------------------------------------------------------
select * from INFORMATION_SCHEMA.TABLES WHERE table_name = "tabula"; - shows !options! what you can do with table and stuff    
SELECT CREATE_TIME FROM INFORMATION_SCHEMA.TABLES WHERE table_name = "mana_tabula1"; - shows what time table was created and stuff     

