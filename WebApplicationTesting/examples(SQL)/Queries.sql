/* 1. Вставка данных */
INSERT INTO mytable (col1, col2) VALUES ('value1', 123);
SELECT * FROM mytable WHERE col1 = 'value1';

/* 2. Обновление данных */
UPDATE mytable SET col1 = 'value2' WHERE col2 = 123;
SELECT * FROM mytable WHERE col2 = 123;

/* 3. Удаление данных */
DELETE FROM mytable WHERE col1 = 'value2';
SELECT * FROM mytable;
