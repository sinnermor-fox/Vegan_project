
Проект для расчета питания

- models - содержит модели соответствующие таблицам с бд
- routes - содержит ендпоинты апи
- controls - содержит логику расчетов
- serializators - содержать сериализаторы для апи


Логика работы через телеграмм

1. Bot отправляет запрос к сервисы с передачей парметра username
2. Сервис делает запрос в таблицу пользователей и узнает id
-  Из таблицы меню забираются значения сегодняшего дня где user_id=id
- по полученному массиву значений получают Food_description, netto из таблицы menu
3. Полученный запрос отправляем обратно в телеграмм пользователю