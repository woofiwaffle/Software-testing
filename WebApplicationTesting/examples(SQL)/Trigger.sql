/* Проверка, что дата начала раньше, чем дата конца тура */
drop trigger if exists check_date_start_finish_update;
delimiter //

/* создание триггера перед обновление на таблицу tours */
create trigger check_date_start_finish_update before update on
tours
for each row
  BEGIN

/* проверка даты на корректность */
     IF new.date_start > new.date_finish THEN
     SIGNAL SQLSTATE '45000'
     SET

/* вывод сообщения об ошибке */
     MESSAGE_TEXT = 'Дата начала тура не может быть позже даты конца тура';
  END IF;
END //
