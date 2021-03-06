set global local_infile = 1;
CREATE DATABASE IF NOT EXISTS AOC2021;

/* DAY 1 */
DROP TABLE IF EXISTS AOC2021.D1_TEST; CREATE TABLE IF NOT EXISTS AOC2021.D1_TEST(ordering int,RAW_DATA int);
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\SQLSetup\\D1testsql.txt' INTO TABLE AOC2021.D1_TEST
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
DROP TABLE IF EXISTS AOC2021.D1_INPUT; CREATE TABLE IF NOT EXISTS AOC2021.D1_INPUT(ordering int,RAW_DATA int);
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\SQLSetup\\D1inputsql.txt' INTO TABLE AOC2021.D1_INPUT
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
  
/* DAY 2 */
DROP TABLE IF EXISTS AOC2021.D2_TEST; CREATE TABLE IF NOT EXISTS AOC2021.D2_TEST(ordering int, RAW_DATA varchar(10));
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\SQLSetup\\D2testsql.txt' INTO TABLE AOC2021.D2_TEST
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
DROP TABLE IF EXISTS AOC2021.D2_INPUT; CREATE TABLE IF NOT EXISTS AOC2021.D2_INPUT(ordering int, RAW_DATA varchar(10));
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\SQLSetup\\D2inputsql.txt' INTO TABLE AOC2021.D2_INPUT
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

/* DAY 3 */
DROP TABLE IF EXISTS AOC2021.D3_TEST; CREATE TABLE IF NOT EXISTS AOC2021.D3_TEST(ordering int, RAW_DATA varchar(15));
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\SQLSetup\\D3testsql.txt' INTO TABLE AOC2021.D3_TEST
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
DROP TABLE IF EXISTS AOC2021.D3_INPUT; CREATE TABLE IF NOT EXISTS AOC2021.D3_INPUT(ordering int, RAW_DATA varchar(15));
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\SQLSetup\\D3inputsql.txt' INTO TABLE AOC2021.D3_INPUT
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
  
  /* DAY 4 */
DROP TABLE IF EXISTS AOC2021.D4_TEST; CREATE TABLE IF NOT EXISTS AOC2021.D4_TEST(ordering int, f1 int, f2 int, f3 int, f4 int, f5 int);
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\SQLSetup\\D4testsql.txt' INTO TABLE AOC2021.D4_TEST
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
DROP TABLE IF EXISTS AOC2021.D4_INPUT; CREATE TABLE IF NOT EXISTS AOC2021.D4_INPUT(ordering int, f1 int, f2 int, f3 int, f4 int, f5 int);
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\SQLSetup\\D4inputsql.txt' INTO TABLE AOC2021.D4_INPUT
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
  
 