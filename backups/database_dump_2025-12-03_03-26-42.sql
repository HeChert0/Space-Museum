-- Space Museum Database Dump
-- Generated: 2025-12-03 03:26:42.178887
-- Database: PostgreSQL

SET client_encoding = 'UTF8';


-- Table: derevo
-- DROP TABLE IF EXISTS derevo CASCADE;

CREATE TABLE IF NOT EXISTS derevo (
    id INTEGER NOT NULL,
    stvol VARCHAR(255),
    fitil BOOLEAN,
    PRIMARY KEY (id)
);

-- Data for derevo
INSERT INTO derevo (id, stvol, fitil) VALUES (1, 'ага', TRUE);
INSERT INTO derevo (id, stvol, fitil) VALUES (2, 'неее', TRUE);


-- Table: employee
-- DROP TABLE IF EXISTS employee CASCADE;

CREATE TABLE IF NOT EXISTS employee (
    employee_id INTEGER NOT NULL,
    full_name VARCHAR(255),
    position VARCHAR(255),
    hire_date TIMESTAMP,
    department VARCHAR(255),
    phone VARCHAR(255),
    qualification VARCHAR(255),
    PRIMARY KEY (employee_id)
);

-- Data for employee
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (2, 'Петрова Мария Сергеевна', 'Главный хранитель', '2012-09-01 00:00:00', 'Отдел фондов', '+375 29 623-45-78', 'Кандидат искусствоведения');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (3, 'Сидоров Алексей Петрович', 'Заведующий отделом выставок', '2015-03-10 00:00:00', 'Выставочный отдел', '+375 29 734-56-89', 'Менеджер проектов');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (4, 'Кузнецова Ольга Викторовна', 'Реставратор', '2018-11-15 00:00:00', 'Реставрационная мастерская', '+375 29 845-67-90', 'Реставратор высшей категории');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (5, 'Смирнов Дмитрий Игоревич', 'Экскурсовод', '2021-06-20 00:00:00', 'Экскурсионный отдел', '+375 29 956-78-01', 'Историк, специалист по космонавтике');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (6, 'Васильева Елена Андреевна', 'Экскурсовод', '2022-08-01 00:00:00', 'Экскурсионный отдел', '+375 29 167-89-12', 'Астрофизик');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (7, 'Новиков Павел Александрович', 'Экскурсовод', '2023-01-15 00:00:00', 'Экскурсионный отдел', '+375 29 278-90-23', 'Инженер ракетно-космической техники');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (8, 'Козлова Анна Михайловна', 'Научный сотрудник', '2019-02-11 00:00:00', 'Научный отдел', '+375 29 389-01-34', 'Кандидат физико-математических наук');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (9, 'Лебедев Артем Владимирович', 'IT-специалист', '2020-07-01 00:00:00', 'IT-отдел', '+375 44 492-12-45', 'Системный администратор');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (10, 'Соколова Ирина Юрьевна', 'Бухгалтер', '2014-04-25 00:00:00', 'Бухгалтерия', '+375 44 583-23-56', 'Экономист');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (11, 'Михайлов Сергей Борисович', 'Специалист по безопасности', '2017-10-30 00:00:00', 'Служба безопасности', '+375 44 674-34-67', 'Офицер запаса');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (12, 'Федорова Татьяна Олеговна', 'Менеджер по персоналу', '2021-09-01 00:00:00', 'Отдел кадров', '+375 44 765-45-78', 'HR-менеджер');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (13, 'Волков Андрей Романович', 'Архивариус', '2016-05-16 00:00:00', 'Отдел фондов', '+375 44 856-56-89', 'Историк-архивист');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (14, 'Зайцева Екатерина Дмитриевна', 'Методист', '2022-11-01 00:00:00', 'Экскурсионный отдел', '+375 44 947-67-90', 'Педагог');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (15, 'Беляев Роман Станиславович', 'Завхоз', '2013-08-19 00:00:00', 'АХО', '+375 44 138-78-01', 'Инженер по эксплуатации');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (16, 'Иванов Иван Иванович', 'Секретать директора музея', '2010-05-20 00:00:00', 'Администрация', '+375 29 229-89-12', 'Доктор исторических наук');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (17, 'Петрова Дарья Сергеевна', 'Помощница главный хранитель', '2012-09-01 00:00:00', 'Отдел фондов', '+375 29 319-90-23', 'Кандидат искусствоведения');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (1, 'Иванов Иван Ивановыч', 'Директор музея', '2000-02-21 00:00:00', 'Администрация', '+375 29 512-34-67', 'Доктор исторических наук');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (18, 'Сидоров Игорь Петрович', 'Помощнк заведующего отделом выставок', '2015-03-10 00:00:00', 'Выставочный отдел', '+375 29 408-01-34', 'Менеджер проектов');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (19, 'Кузнецова Валерия Викторовна', 'Реставратор', '2018-11-15 00:00:00', 'Реставрационная мастерская', '+375 29 597-12-45', 'Реставратор высшей категории');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (20, 'Смирнов Никита Игоревич', 'Экскурсовод', '2021-06-20 00:00:00', 'Экскурсионный отдел', '+375 29 686-23-56', 'Историк, специалист по космонавтике');


-- Table: excursion
-- DROP TABLE IF EXISTS excursion CASCADE;

CREATE TABLE IF NOT EXISTS excursion (
    excursion_id INTEGER NOT NULL,
    title VARCHAR(255),
    date TIMESTAMP,
    language VARCHAR(255),
    ticket_num INTEGER,
    price INTEGER,
    duration INTEGER,
    employee_id INTEGER,
    PRIMARY KEY (excursion_id),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id) ON DELETE CASCADE
);

-- Data for excursion
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (1, 'Обзорная по музею', '2025-10-28 00:00:00', 'Русский', 25, 45, 90, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (2, 'Путешествие к планетам-гигантам', '2025-10-29 00:00:00', 'Русский', 15, 65, 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (3, 'Первые шаги в космосе', '2025-10-30 00:00:00', 'Английский', 20, 85, 90, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (4, 'Для самых маленьких: Космическое приключение', '2025-11-01 00:00:00', 'Русский', 30, 30, 45, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (5, 'Жизнь на орбите', '2025-11-02 00:00:00', 'Русский', 20, 55, 75, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (6, 'Обзорная по музею', '2025-11-03 00:00:00', 'Русский', 25, 45, 90, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (7, 'Покорение Луны: как это было', '2025-11-04 00:00:00', 'Русский', 15, 70, 60, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (8, 'Звездные войны: мифы и реальность', '2025-11-05 00:00:00', 'Русский', 20, 60, 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (9, 'Обзорная по музею', '2025-11-06 00:00:00', 'Английский', 20, 85, 90, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (10, 'В поисках внеземной жизни', '2025-11-07 00:00:00', 'Русский', 15, 65, 75, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (11, 'Ракетные двигатели: от РД-107 до Raptor', '2025-11-08 00:00:00', 'Русский', 10, 90, 60, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (12, 'Космическая медицина', '2025-11-09 00:00:00', 'Русский', 15, 55, 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (13, 'Обзорная по музею', '2025-11-10 00:00:00', 'Русский', 25, 45, 90, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (14, 'Как устроен телескоп Хаббл', '2025-11-11 00:00:00', 'Русский', 15, 70, 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (15, 'История скафандров', '2025-11-12 00:00:00', 'Русский', 20, 60, 75, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (16, 'Космос для детей: игра и обучение', '2025-11-13 00:00:00', 'Русский', 25, 35, 45, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (17, 'Марс: новые горизонты', '2025-11-14 00:00:00', 'Русский', 15, 50, 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (18, 'Солнечная система: путешествие по планетам', '2025-11-15 00:00:00', 'Английский', 20, 80, 90, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (19, 'Космические технологии будущего', '2025-11-16 00:00:00', 'Русский', 20, 45, 75, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (20, 'Астрономия для начинающих', '2025-11-17 00:00:00', 'Русский', 30, 30, 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (21, 'Космос для детей: игра и обучение', '2025-10-24 00:00:00', 'Русский', 20, 30, 60, 5);


-- Table: excursion_visitor
-- DROP TABLE IF EXISTS excursion_visitor CASCADE;

CREATE TABLE IF NOT EXISTS excursion_visitor (
    excursion_id INTEGER,
    visitor_id INTEGER,
    FOREIGN KEY (excursion_id) REFERENCES excursion(excursion_id) ON DELETE CASCADE
);

-- Data for excursion_visitor
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (1, 1);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (1, 2);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (3, 3);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (2, 4);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (4, 10);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (5, 6);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (7, 8);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (9, 9);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (10, 12);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (11, 14);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (1, 5);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (2, 7);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (4, 11);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (5, 13);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (7, 15);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (6, 16);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (8, 17);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (12, 18);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (13, 19);
INSERT INTO excursion_visitor (excursion_id, visitor_id) VALUES (14, 20);


-- Table: exhibit
-- DROP TABLE IF EXISTS exhibit CASCADE;

CREATE TABLE IF NOT EXISTS exhibit (
    exhibit_id INTEGER NOT NULL,
    title VARCHAR(255),
    description VARCHAR(255),
    creation_date TIMESTAMP,
    country VARCHAR(255),
    state VARCHAR(255),
    type VARCHAR(255),
    mission_id INTEGER,
    PRIMARY KEY (exhibit_id)
);

-- Data for exhibit
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (1, 'Спускаемый аппарат "Восток-1"', 'Оригинальный спускаемый аппарат, в котором Юрий Гагарин совершил первый полет.', '1961-01-01 00:00:00', 'СССР', 'На экспозиции', 'Оригинал', 1);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (2, 'Макет корабля "Аполлон-11"', 'Полноразмерный макет командного и лунного модулей.', '1970-01-01 00:00:00', 'США', 'На экспозиции', 'Макет', 2);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (3, 'Копия "Спутника-1"', 'Точная копия первого искусственного спутника Земли.', '1958-01-01 00:00:00', 'СССР', 'На экспозиции', 'Копия', 3);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (4, 'Золотая пластинка "Вояджера"', 'Копия пластинки с посланием для внеземных цивилизаций.', '1977-01-01 00:00:00', 'США', 'На экспозиции', 'Копия', 4);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (5, 'Скафандр "Беркут"', 'Оригинальный скафандр, использовавшийся Алексеем Леоновым.', '1964-01-01 00:00:00', 'СССР', 'На реставрации', 'Оригинал', 13);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (6, 'Макет станции "Салют-1"', 'Макет первой в мире орбитальной станции в масштабе 1:10.', '1972-01-01 00:00:00', 'СССР', 'На экспозиции', 'Макет', 8);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (7, 'Стыковочный узел "Союз-Аполлон"', 'Тренировочный образец андрогинно-периферийного агрегата стыковки.', '1974-01-01 00:00:00', 'СССР/США', 'На экспозиции', 'Оригинал', 7);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (8, 'Лунный камень (образец)', 'Образец лунного грунта, доставленный миссией "Луна-16".', '1970-09-24 00:00:00', 'СССР', 'В хранилище', 'Оригинал', NULL);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (9, 'Скафандр "Орлан-ДМА"', 'Скафандр для работы в открытом космосе на станции "Мир".', '1985-01-01 00:00:00', 'СССР', 'На экспозиции', 'Оригинал', 9);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (10, 'Зеркало телескопа "Хаббл" (макет)', 'Макет главного зеркала космического телескопа.', '1990-01-01 00:00:00', 'США', 'На экспозиции', 'Макет', 10);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (11, 'Макет марсохода "Соджорнер"', 'Полноразмерный макет первого успешного марсохода.', '1996-01-01 00:00:00', 'США', 'На экспозиции', 'Макет', 14);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (12, 'Спускаемый аппарат "Венера-7"', 'Оригинальный аппарат, совершивший посадку на Венеру.', '1970-01-01 00:00:00', 'СССР', 'На экспозиции', 'Оригинал', 6);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (13, 'Модуль "Заря" (макет)', 'Макет первого модуля МКС в масштабе 1:20.', '1998-01-01 00:00:00', 'Россия', 'На экспозиции', 'Макет', 12);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (14, 'Кресло "Казбек-УМ"', 'Летное кресло из корабля "Союз".', '1980-01-01 00:00:00', 'СССР', 'На экспозиции', 'Оригинал', NULL);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (15, 'Корабль "Орион" (макет)', 'Макет перспективного пилотируемого корабля.', '2020-01-01 00:00:00', 'США', 'На экспозиции', 'Макет', 15);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (16, 'Спускаемый аппарат "Восток-1"', 'Оригинальный спускаемый аппарат, в котором Белка и Стрелка совершили первый полет.', '1961-01-01 00:00:00', 'СССР', 'На экспозиции', 'Оригинал', 1);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (17, 'Макет корабля "Аполлон-11"', 'Полноразмерный макет командного и лунного модулей.', '1970-01-01 00:00:00', 'США', 'На экспозиции', 'Макет', 2);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (18, 'Копия "Спутника-1"', 'Точная копия первого искусственного спутника Марса.', '1958-01-01 00:00:00', 'СССР', 'На экспозиции', 'Копия', 3);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (19, 'Золотая пластинка "Вояджера"', 'Копия пластинки с посланием для внеземных цивилизаций.', '1977-01-01 00:00:00', 'США', 'На экспозиции', 'Копия', 4);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (20, 'Скафандр "Беркут"', 'Оригинальный скафандр, использовавшийся Юрием Гагариным.', '1964-01-01 00:00:00', 'СССР', 'На реставрации', 'Оригинал', 13);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (21, 'Кепарис', 'Из тросника', '2002-02-22 00:00:00', 'РОССИЯ', 'Найс', 'Найденный', NULL);


-- Table: exhibition
-- DROP TABLE IF EXISTS exhibition CASCADE;

CREATE TABLE IF NOT EXISTS exhibition (
    exhibition_id INTEGER NOT NULL,
    title VARCHAR(255),
    theme VARCHAR(255),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    location VARCHAR(255),
    type VARCHAR(255),
    PRIMARY KEY (exhibition_id)
);

-- Data for exhibition
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (1, 'Первые в космосе', 'История советской космонавтики', '2025-01-15 00:00:00', '2026-01-15 00:00:00', 'Главный зал', 'Постоянная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (2, 'Покорители Луны', 'Лунная гонка СССР и США', '2025-09-01 00:00:00', '2026-03-01 00:00:00', 'Зал №2', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (3, 'Роботы в космосе', 'Автоматические межпланетные станции', '2024-12-01 00:00:00', '2025-12-01 00:00:00', 'Зал №3', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (4, 'Женщины в космонавтике', 'Вклад женщин в освоение космоса', '2025-03-01 00:00:00', '2025-06-01 00:00:00', 'Галерея', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (5, 'Орбитальные станции: от Салюта до МКС', 'Жизнь и работа на орбите', '2025-05-01 00:00:00', NULL, 'Зал №1', 'Постоянная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (6, 'Телескопы: Окно во Вселенную', 'История космических обсерваторий', '2025-10-01 00:00:00', '2026-02-01 00:00:00', 'Зал №4', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (7, 'Красная планета: Миссии на Марс', 'Исследование Марса', '2026-01-01 00:00:00', '2026-07-01 00:00:00', 'Зал №2', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (8, 'Космическая еда', 'Питание на орбите', '2025-11-01 00:00:00', '2026-01-01 00:00:00', 'Малый зал', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (9, 'Искусство и космос', 'Космос в работах художников', '2025-07-10 00:00:00', '2025-09-10 00:00:00', 'Арт-пространство', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (10, 'Частные полеты', 'Новая эра коммерческого космоса', '2026-04-01 00:00:00', '2026-08-01 00:00:00', 'Зал №3', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (11, 'Сделано в СССР', 'Достижения советской инженерии', '2025-01-01 00:00:00', NULL, 'Главный зал', 'Постоянная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (12, 'Космические скафандры', 'Эволюция защитного снаряжения', '2025-08-15 00:00:00', '2025-12-15 00:00:00', 'Зал №4', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (13, 'Открытый космос', 'История выходов в безвоздушное пространство', '2025-06-20 00:00:00', '2025-10-20 00:00:00', 'Зал №2', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (14, 'Венера: Неизведанная соседка', 'Исследования Венеры', '2026-02-01 00:00:00', '2026-05-01 00:00:00', 'Зал №3', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (15, 'Будущее космонавтики', 'Проекты и концепции будущего', '2026-09-01 00:00:00', '2027-09-01 00:00:00', 'Главный зал', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (16, 'Первые на Марсе', 'История американсой космонавтики', '2025-01-15 00:00:00', '2026-01-15 00:00:00', 'Главный зал', 'Постоянная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (17, 'Покорители Венеры', 'Лунная гонка СССР и США', '2025-09-01 00:00:00', '2026-03-01 00:00:00', 'Зал №2', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (18, 'Роботы в космосе для детей', 'Автоматические межпланетные станции', '2024-12-01 00:00:00', '2025-12-01 00:00:00', 'Зал №3', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (19, 'Мужчины в космонавтике', 'Вклад мужчины в освоение космоса', '2025-03-01 00:00:00', '2025-06-01 00:00:00', 'Галерея', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (20, 'Орбитальные станции', 'Жизнь и работа на орбите', '2025-05-01 00:00:00', NULL, 'Зал №1', 'Постоянная');


-- Table: exhibition_employee
-- DROP TABLE IF EXISTS exhibition_employee CASCADE;

CREATE TABLE IF NOT EXISTS exhibition_employee (
    exhibition_id INTEGER,
    employee_id INTEGER,
    FOREIGN KEY (exhibition_id) REFERENCES exhibition(exhibition_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id) ON DELETE CASCADE
);

-- Data for exhibition_employee
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (1, 2);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (1, 3);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (2, 3);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (2, 8);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (3, 3);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (3, 8);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (4, 3);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (5, 2);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (5, 3);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (6, 8);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (7, 3);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (11, 2);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (12, 4);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (13, 3);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (15, 8);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (8, 4);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (9, 2);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (10, 3);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (14, 8);
INSERT INTO exhibition_employee (exhibition_id, employee_id) VALUES (16, 2);


-- Table: exhibition_excursion
-- DROP TABLE IF EXISTS exhibition_excursion CASCADE;

CREATE TABLE IF NOT EXISTS exhibition_excursion (
    exhibition_id INTEGER,
    excursion_id INTEGER,
    FOREIGN KEY (exhibition_id) REFERENCES exhibition(exhibition_id) ON DELETE CASCADE,
    FOREIGN KEY (excursion_id) REFERENCES excursion(excursion_id) ON DELETE CASCADE
);

-- Data for exhibition_excursion
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (1, 1);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (1, 6);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (2, 7);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (5, 5);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (6, 14);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (7, 2);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (12, 15);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (1, 13);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (2, 3);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (3, 8);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (4, 1);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (5, 1);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (7, 1);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (13, 1);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (15, 10);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (3, 10);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (4, 12);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (8, 4);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (11, 9);
INSERT INTO exhibition_excursion (exhibition_id, excursion_id) VALUES (14, 11);


-- Table: exhibition_exhibit
-- DROP TABLE IF EXISTS exhibition_exhibit CASCADE;

CREATE TABLE IF NOT EXISTS exhibition_exhibit (
    exhibition_id INTEGER,
    exhibit_id INTEGER,
    FOREIGN KEY (exhibition_id) REFERENCES exhibition(exhibition_id) ON DELETE CASCADE,
    FOREIGN KEY (exhibit_id) REFERENCES exhibit(exhibit_id) ON DELETE CASCADE
);

-- Data for exhibition_exhibit
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (1, 1);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (1, 3);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (1, 5);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (2, 2);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (2, 8);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (3, 4);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (3, 11);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (5, 6);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (5, 9);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (5, 13);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (6, 10);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (7, 11);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (12, 5);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (12, 9);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (13, 5);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (8, 7);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (9, 12);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (10, 14);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (11, 15);
INSERT INTO exhibition_exhibit (exhibition_id, exhibit_id) VALUES (14, 3);


-- Table: space_mission
-- DROP TABLE IF EXISTS space_mission CASCADE;

CREATE TABLE IF NOT EXISTS space_mission (
    mission_id INTEGER,
    title VARCHAR(255),
    country VARCHAR(255),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    crew TEXT[],
    goal VARCHAR(255)
);

-- Data for space_mission
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (2, 'Аполлон-11', 'США', '1969-07-16 00:00:00', '1969-07-24 00:00:00', ARRAY['Нил Армстронг', 'Базз Олдрин', 'Майкл Коллинз'], 'Первая высадка человека на Луну');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (3, 'Спутник-1', 'СССР', '1957-10-04 00:00:00', '1958-01-04 00:00:00', NULL, 'Запуск первого искусственного спутника Земли');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (4, 'Вояджер-1', 'США', '1977-09-05 00:00:00', NULL, NULL, 'Исследование дальних планет Солнечной системы');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (5, 'Луна-9', 'СССР', '1966-01-31 00:00:00', '1966-02-06 00:00:00', NULL, 'Первая мягкая посадка на Луну');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (6, 'Венера-7', 'СССР', '1970-08-17 00:00:00', '1970-12-15 00:00:00', NULL, 'Первая мягкая посадка на Венеру');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (7, 'Союз-Аполлон', 'СССР/США', '1975-07-15 00:00:00', '1975-07-24 00:00:00', ARRAY['Алексей Леонов', 'Валерий Кубасов', 'Томас Стаффорд'], 'Первая стыковка кораблей разных стран');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (8, 'Салют-1', 'СССР', '1971-04-19 00:00:00', '1971-10-11 00:00:00', NULL, 'Запуск первой в мире орбитальной станции');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (9, 'Мир', 'СССР/Россия', '1986-02-19 00:00:00', '2001-03-23 00:00:00', NULL, 'Создание многомодульной орбитальной станции');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (10, 'Хаббл (STS-31)', 'США/ЕКА', '1990-04-24 00:00:00', NULL, ARRAY['Лорен Шрайвер', 'Чарльз Болден'], 'Вывод на орбиту космического телескопа');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (11, 'Марс-3', 'СССР', '1971-05-28 00:00:00', '1972-08-22 00:00:00', NULL, 'Первая мягкая посадка на Марс');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (12, 'Международная космическая станция (МКС)', 'Международный', '1998-11-20 00:00:00', NULL, NULL, 'Создание международной пилотируемой орбитальной станции');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (13, 'Восход-2', 'СССР', '1965-03-18 00:00:00', '1965-03-19 00:00:00', ARRAY['Павел Беляев', 'Алексей Леонов'], 'Первый выход человека в открытый космос');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (14, 'Mars Pathfinder', 'США', '1996-12-04 00:00:00', '1997-09-27 00:00:00', NULL, 'Доставка первого марсохода "Соджорнер"');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (15, 'Артемида-1', 'США', '2022-11-16 00:00:00', '2022-12-11 00:00:00', NULL, 'Беспилотный облет Луны кораблем "Орион"');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (16, 'Чанъэ-5', 'Китай', '2020-11-23 00:00:00', '2020-12-16 00:00:00', NULL, 'Доставка лунного грунта на Землю');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (17, 'Perseverance', 'США', '2020-07-30 00:00:00', NULL, NULL, 'Поиск следов жизни на Марсе и сбор образцов');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (18, 'Hayabusa2', 'Япония', '2014-12-03 00:00:00', '2020-12-05 00:00:00', NULL, 'Исследование астероида Рюгу и доставка образцов');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (19, 'Джеймс Уэбб', 'США/ЕКА/Канада', '2021-12-25 00:00:00', NULL, NULL, 'Исследование ранней Вселенной в инфракрасном диапазоне');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (20, 'Венера-Д', 'Россия', '2024-11-01 00:00:00', NULL, NULL, 'Комплексное исследование атмосферы и поверхности Венеры');


-- Table: visitor
-- DROP TABLE IF EXISTS visitor CASCADE;

CREATE TABLE IF NOT EXISTS visitor (
    visitor_id INTEGER NOT NULL,
    full_name VARCHAR(255),
    birth_date TIMESTAMP,
    citizenship VARCHAR(255),
    ticket_type VARCHAR(255),
    visit_date TIMESTAMP,
    review VARCHAR(255),
    PRIMARY KEY (visitor_id)
);

-- Data for visitor
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (1, 'Александров Александр Александрович', '1990-05-15 00:00:00', 'Россия', 'Взрослый', '2025-10-20 00:00:00', 'Очень понравилась выставка про Луну!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (2, 'Борисова Богдана Борисовна', '2015-01-20 00:00:00', 'Россия', 'Детский', '2025-10-20 00:00:00', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (3, 'John Smith', '1985-11-30 00:00:00', 'США', 'Взрослый', '2025-10-21 00:00:00', 'Amazing collection of Soviet space history.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (4, 'Мария Иванова', '1992-07-22 00:00:00', 'Беларусь', 'Взрослый', '2025-10-21 00:00:00', 'Впечатляет!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (5, 'Сергеев Сергей Сергеевич', '1978-03-12 00:00:00', 'Россия', 'Взрослый', '2025-10-22 00:00:00', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (6, 'Орлова Ольга Олеговна', '1995-09-05 00:00:00', 'Россия', 'Льготный', '2025-10-22 00:00:00', 'Спасибо за интересную экскурсию.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (7, 'Григорьев Григорий Григорьевич', '2001-12-01 00:00:00', 'Казахстан', 'Взрослый', '2025-10-23 00:00:00', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (8, 'Антонова Антонина Антоновна', '1965-02-18 00:00:00', 'Россия', 'Пенсионный', '2025-10-23 00:00:00', 'Вспомнила молодость, спасибо!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (9, 'Wei Zhang', '1998-08-08 00:00:00', 'Китай', 'Взрослый', '2025-10-24 00:00:00', 'Very educational.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (10, 'Давыдов Давид Давидович', '2017-06-10 00:00:00', 'Россия', 'Детский', '2025-10-24 00:00:00', 'Ракета большая!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (11, 'Егоров Егор Егорович', '1988-04-04 00:00:00', 'Россия', 'Взрослый', '2025-10-25 00:00:00', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (12, 'Фомина Фаина Федоровна', '1999-10-10 00:00:00', 'Россия', 'Студенческий', '2025-10-25 00:00:00', 'Приду еще раз с друзьями.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (13, 'Hans Schmidt', '1975-01-25 00:00:00', 'Германия', 'Взрослый', '2025-10-26 00:00:00', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (14, 'Кириллов Кирилл Кириллович', '2003-07-07 00:00:00', 'Россия', 'Взрослый', '2025-10-26 00:00:00', 'Круто, но мало интерактива.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (15, 'Лазарева Лариса Львовна', '1982-11-11 00:00:00', 'Украина', 'Взрослый', '2025-10-27 00:00:00', 'Очень познавательно.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (16, 'Александров Александр Александрович', '1990-05-15 00:00:00', 'Россия', 'Взрослый', '2025-10-20 00:00:00', 'Очень понравилась выставка про Марс!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (17, 'Борисова Богдана Борисовна', '2015-01-20 00:00:00', 'Россия', 'Детский', '2025-10-20 00:00:00', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (18, 'Mitt Smith', '1985-11-30 00:00:00', 'США', 'Взрослый', '2025-10-21 00:00:00', 'Amazing collection of Soviet space history.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (19, 'Наталья Иванова', '1992-07-22 00:00:00', 'Беларусь', 'Взрослый', '2025-10-21 00:00:00', 'Круто!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (20, 'Сергеев Андрей Сергеевич', '1978-03-12 00:00:00', 'Россия', 'Взрослый', '2025-10-22 00:00:00', NULL);


-- Reset sequences
