/* Тестирование прав доступа также можно осуществить с помощью SQLзапросов: */
/* 1. Проверка наличия анонимных пользователей: */
SELECT user, host
FROM mysql.user
WHERE user = '';

/* 2. Проверка наличия слабых паролей: */
SELECT user, host
FROM mysql.user
WHERE LENGTH(password) < 8;

/* 3. Проверка наличия пользователей с доступом к базам данных, к которым они не должны иметь доступ: */
SELECT DISTINCT USER,HOST
FROM mysql.db
WHERE db NOT IN ('mysql','information_schema','performance_schema');