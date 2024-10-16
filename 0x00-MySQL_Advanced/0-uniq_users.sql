--SQL script that creates a table users
-- With these attributes:
--id, integer, never null, auto increment and primary key
--email, string (255 characters), never null and unique
--name, string (255 characters)
--If the table already exists, your script should not fail

CREATE TABLE users (id integer NOT NULL AUTO_INCREMENT, PRIMARY KEY (id),
                   email varchar(255) NOT NULL UNIQUE,
                   name varchar(255));
