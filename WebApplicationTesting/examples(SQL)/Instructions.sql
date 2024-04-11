/* ПРИМЕРЫ ИНСТРУКЦИЙ */
/* 1. Создание пользователя */
CREATE USER 'user2' IDENTIFIED BY '123456';

/* Присвоения всех привилегий во всех БД и таблицах */
/* 2. Просмотр прав пользователей*/
USE mysql;
SELECT * FROM user;

/* 3. Передача выборочных прав пользователю */
GRANT SELECT,INSERT, UPDATE,DELETE, CREATE, ALTER,
DROP ON *.* TO user2
WITH GRANT OPTION;

/* 4. Удаление привилегий для одного пользователя */
REVOKE ALL PRIVILEGES ON *.* FROM 'user2';