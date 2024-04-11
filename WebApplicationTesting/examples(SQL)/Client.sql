/* Создание таблицы */
CREATE TABLE Client (age INT, name varchar(150));

/* Установка нового разделителя инструкций */
delimiter //

/* Триггер BEFORE INSERT */
CREATE TRIGGER agecheck BEFORE INSERT ON Client
      FOR EACH ROW
          IF NEW.age < 0
          THEN SET NEW.age = 0;
          END IF//

/* Переименование разделителя инструкций */
Delimiter ;

/* Тестирование триггера по добавлению пользователей в таблицу */
INSERT INTO Client VALUES (-10, 'Сергей'), (20, 'Иван'), (30,'Геннадий');

/* Проверка введенных значений */
SELECT * FROM Client;