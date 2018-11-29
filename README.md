CREATE USER 'dbproject'@'localhost' IDENTIFIED BY 'password';

create database pdb1;

GRANT ALL ON pdb1.* TO 'dbproject'@'localhost';

pip install json2table

python3 -m pip install PyMySQL

pip install geopy
