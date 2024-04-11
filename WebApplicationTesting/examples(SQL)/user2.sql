/* создание пользователя user2 с паролем «2222» */
CREATE USER 'user2' IDENTIFIED BY '2222';

/* присвоение пользователю user2 всех привилегий во всех БД и таблицах, включая привилегию GRANT */
GRANT ALL
ON *.*
TO user2
WITH GRANT OPTION;

/* вход в БД MySQL */
USE mysql;

/* просмотр информации о пользователях сервера, и их привилегиях */
SELECT *
FROM user;

/* лишение user2 всех привилегий, данных функцией GRANT */
REVOKE ALL PRIVILEGES
ON *.*
FROM 'user2';