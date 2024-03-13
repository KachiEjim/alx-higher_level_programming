-- SQL script to print the full description of the table first_table
SELECT CONCAT('Table: ', table_name, '\n', create_statement)
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
