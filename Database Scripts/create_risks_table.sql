CREATE TABLE public."risk"(
   Id INT GENERATED ALWAYS AS IDENTITY,
   "riskItem" VARCHAR (500) not null,
   actions VARCHAR (500) not null,
   impact VARCHAR (25) not null,
   "impactDate" date not null,
   status VARCHAR (5) not null,
   PRIMARY KEY(Id)
); 