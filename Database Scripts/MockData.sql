Capability
INSERT INTO public.capability(
	id, "number", name, size, status, length, dependency)
	VALUES (23, 466357, 'Research EIN', 'M', 'Elaboration Complete', 10, 'N/A');
	
INSERT INTO public.capability(
	id, "number", name, size, status, length, dependency)
	VALUES (24, 515946, 'Work General Request (EO Correspondence Case)', 'XXL', 'In Elaboration', 100, 'N/A');
	
INSERT INTO public.capability(
	id, "number", name, size, status, length, dependency)
	VALUES (25, 459095, 'Systematically Initiate Case Creation Process', 'L', 'In Elaboration', 50, 'N/A');

INSERT INTO public.capability(
	id, "number", name, size, status, length, dependency)
	VALUES (26, 514606, 'Work Other Request (EO Correspondence Case)', 'L', 'In Elaboration', 30, 'N/A');
	
INSERT INTO public.capability(
	id, "number", name, size, status, length, dependency)
	VALUES (27, 485031, 'Load Disclosable Files/Documents from MEDS', 'M', 'In Elaboration', 70, 'N/A');

budget
INSERT INTO public.budget(
	id, num, task_area, ceiling_value, funded_value, eac_revenue, eac_profit, eac_profit_percent)
	VALUES (1, 1, 'FFP ECM', 10990047, 10990047, 10990047, 1555641, 14.15);
	
INSERT INTO public.budget(
	id, num, task_area, ceiling_value, funded_value, eac_revenue, eac_profit, eac_profit_percent)
	VALUES (2, 2, 'Release Management (TM)', 2697466, 210682, 208048, 21839, 10.5);
	
INSERT INTO public.budget(
	id, num, task_area, ceiling_value, funded_value, eac_revenue, eac_profit, eac_profit_percent)
	VALUES (3, 3, 'Requirements Engineering Support (TM)', 1023955, 376632, 376385, 88946, 23.63);

Resource Management
INSERT INTO public."resourceManagement" ("projectName","resourceName","duration","status","updatedDate") VALUES ('Tableau', 'Praveen', 40, 'Working','2020-08-31');
INSERT INTO public."resourceManagement" ("projectName","resourceName","duration","status","updatedDate") VALUES ('Tableau', 'Lexa', 40, 'Working','2020-08-31');
INSERT INTO public."resourceManagement"  ("projectName","resourceName","duration","status","updatedDate") VALUES ('Tableau', 'Heather', 40, 'ToDo','2020-08-31');
INSERT INTO public."resourceManagement"  ("projectName","resourceName","duration","status","updatedDate") VALUES ('React', 'Andy', 40, 'Working','2020-08-31');
INSERT INTO public."resourceManagement"  ("projectName","resourceName","duration","status","updatedDate") VALUES ('Api', 'Isaac', 40, 'Working','2020-08-31');
INSERT INTO public."resourceManagement"  ("projectName","resourceName","duration","status","updatedDate")  VALUES ('Api', 'Paul', 40, 'ToDo','2020-08-31');
INSERT INTO public."resourceManagement"  ("projectName","resourceName","duration","status","updatedDate")  VALUES ('OpenSource', 'Jon', 40, 'Done','2020-08-31');
