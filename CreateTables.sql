set global local_infile = 1;
CREATE DATABASE IF NOT EXISTS AOC2021;

/* DAY 1 */
DROP TABLE IF EXISTS AOC2021.D1_TEST; CREATE TABLE IF NOT EXISTS AOC2021.D1_TEST(RAW_DATA int);
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\D1\\test.txt' INTO TABLE AOC2021.D1_TEST
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
DROP TABLE IF EXISTS AOC2021.D1_INPUT; CREATE TABLE IF NOT EXISTS AOC2021.D1_INPUT(RAW_DATA int);
LOAD DATA LOCAL INFILE 'C:\\Users\\Ryan\\Documents\\Git Local\\Advent of Code 2021\\AdventofCode2021\\D1\\input.txt' INTO TABLE AOC2021.D1_INPUT
  FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
  
/* DAY 2 */