CREATE TABLE public."task"(
   Id INT GENERATED ALWAYS AS IDENTITY,
   "description" VARCHAR (500) not null,
   category VARCHAR (500) not null,
   PRIMARY KEY(Id)
); 