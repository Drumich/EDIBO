make database and show it through angular   

CREATE TABLE ediboKG3(name VARCHAR(20),lastname VARCHAR(20),age INT NOT NULL DEFAULT 69,date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
INSERT INTO ediboKG3(name,lastname,age,date) VALUES("Kriss","G",69,now());
    

show grants; - shows what you can do        
use databasename; - switches to database    
show tables; - shows tables     
describe tablename; - shows details about this table    
ALTER TABLE ediboKG ADD age INT NOT NULL; - add a column to a table           


























select * from INFORMATION_SCHETA.TABLES WHERE table_name = "tabula"; - shows !options! what you can do with table and stuff    
SELECT CREATE_TIME FROM INFORMATION_SCHEMA.TABLES WHERE table_name = "mana_tabula1"; - shows what time table was created and stuff     
