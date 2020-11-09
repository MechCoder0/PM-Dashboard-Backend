CREATE TABLE budget(
   Id INT GENERATED ALWAYS AS IDENTITY,
   number int not null,
   task_area VARCHAR (10) not null,
   ceiling_value int not null,
   funded_value int not null,
   eac_revenue int not null,	
   eac_profit int not null,	
   eac_profit_percent int not null,	
   PRIMARY KEY(Id)
); 