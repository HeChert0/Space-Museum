-- Space Museum Database Dump
-- Generated: 2025-12-03 02:02:38.703360
-- Database: PostgreSQL

SET client_encoding = 'UTF8';


-- Table: derevo
-- DROP TABLE IF EXISTS derevo CASCADE;

CREATE TABLE IF NOT EXISTS derevo (
    id INTEGER NOT NULL,
    stvol TEXT,
    fitil BOOLEAN,
    PRIMARY KEY (id)
);

-- Data for derevo
INSERT INTO derevo (id, stvol, fitil) VALUES (1, 'ага', TRUE);
INSERT INTO derevo (id, stvol, fitil) VALUES (2, 'неее', TRUE);


-- Table: employee
-- DROP TABLE IF EXISTS employee CASCADE;

CREATE TABLE IF NOT EXISTS employee (
    employee_id INTEGER NOT NULL DEFAULT nextval('employee_employee_id_seq'::regclass),
    full_name VARCHAR(255) NOT NULL,
    position VARCHAR(100),
    hire_date DATE,
    department VARCHAR(100),
    phone VARCHAR(20),
    qualification VARCHAR(100),
    PRIMARY KEY (employee_id)
);

-- Data for employee
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (2, 'Петрова Мария Сергеевна', 'Главный хранитель', '2012-09-01', 'Отдел фондов', '+375 29 623-45-78', 'Кандидат искусствоведения');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (3, 'Сидоров Алексей Петрович', 'Заведующий отделом выставок', '2015-03-10', 'Выставочный отдел', '+375 29 734-56-89', 'Менеджер проектов');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (4, 'Кузнецова Ольга Викторовна', 'Реставратор', '2018-11-15', 'Реставрационная мастерская', '+375 29 845-67-90', 'Реставратор высшей категории');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (5, 'Смирнов Дмитрий Игоревич', 'Экскурсовод', '2021-06-20', 'Экскурсионный отдел', '+375 29 956-78-01', 'Историк, специалист по космонавтике');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (6, 'Васильева Елена Андреевна', 'Экскурсовод', '2022-08-01', 'Экскурсионный отдел', '+375 29 167-89-12', 'Астрофизик');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (7, 'Новиков Павел Александрович', 'Экскурсовод', '2023-01-15', 'Экскурсионный отдел', '+375 29 278-90-23', 'Инженер ракетно-космической техники');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (8, 'Козлова Анна Михайловна', 'Научный сотрудник', '2019-02-11', 'Научный отдел', '+375 29 389-01-34', 'Кандидат физико-математических наук');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (9, 'Лебедев Артем Владимирович', 'IT-специалист', '2020-07-01', 'IT-отдел', '+375 44 492-12-45', 'Системный администратор');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (10, 'Соколова Ирина Юрьевна', 'Бухгалтер', '2014-04-25', 'Бухгалтерия', '+375 44 583-23-56', 'Экономист');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (11, 'Михайлов Сергей Борисович', 'Специалист по безопасности', '2017-10-30', 'Служба безопасности', '+375 44 674-34-67', 'Офицер запаса');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (12, 'Федорова Татьяна Олеговна', 'Менеджер по персоналу', '2021-09-01', 'Отдел кадров', '+375 44 765-45-78', 'HR-менеджер');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (13, 'Волков Андрей Романович', 'Архивариус', '2016-05-16', 'Отдел фондов', '+375 44 856-56-89', 'Историк-архивист');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (14, 'Зайцева Екатерина Дмитриевна', 'Методист', '2022-11-01', 'Экскурсионный отдел', '+375 44 947-67-90', 'Педагог');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (15, 'Беляев Роман Станиславович', 'Завхоз', '2013-08-19', 'АХО', '+375 44 138-78-01', 'Инженер по эксплуатации');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (16, 'Иванов Иван Иванович', 'Секретать директора музея', '2010-05-20', 'Администрация', '+375 29 229-89-12', 'Доктор исторических наук');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (17, 'Петрова Дарья Сергеевна', 'Помощница главный хранитель', '2012-09-01', 'Отдел фондов', '+375 29 319-90-23', 'Кандидат искусствоведения');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (1, 'Иванов Иван Ивановыч', 'Директор музея', '2000-02-21', 'Администрация', '+375 29 512-34-67', 'Доктор исторических наук');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (18, 'Сидоров Игорь Петрович', 'Помощнк заведующего отделом выставок', '2015-03-10', 'Выставочный отдел', '+375 29 408-01-34', 'Менеджер проектов');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (19, 'Кузнецова Валерия Викторовна', 'Реставратор', '2018-11-15', 'Реставрационная мастерская', '+375 29 597-12-45', 'Реставратор высшей категории');
INSERT INTO employee (employee_id, full_name, position, hire_date, department, phone, qualification) VALUES (20, 'Смирнов Никита Игоревич', 'Экскурсовод', '2021-06-20', 'Экскурсионный отдел', '+375 29 686-23-56', 'Историк, специалист по космонавтике');


-- Table: excursion
-- DROP TABLE IF EXISTS excursion CASCADE;

CREATE TABLE IF NOT EXISTS excursion (
    excursion_id INTEGER NOT NULL DEFAULT nextval('excursion_excursion_id_seq'::regclass),
    title VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    language VARCHAR(50),
    ticket_num SMALLINT,
    price NUMERIC,
    duration INTEGER,
    employee_id INTEGER NOT NULL,
    PRIMARY KEY (excursion_id),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id) ON DELETE RESTRICT
);

-- Data for excursion
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (1, 'Обзорная по музею', '2025-10-28', 'Русский', 25, '45.00', 90, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (2, 'Путешествие к планетам-гигантам', '2025-10-29', 'Русский', 15, '65.00', 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (3, 'Первые шаги в космосе', '2025-10-30', 'Английский', 20, '85.00', 90, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (4, 'Для самых маленьких: Космическое приключение', '2025-11-01', 'Русский', 30, '30.00', 45, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (5, 'Жизнь на орбите', '2025-11-02', 'Русский', 20, '55.00', 75, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (6, 'Обзорная по музею', '2025-11-03', 'Русский', 25, '45.00', 90, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (7, 'Покорение Луны: как это было', '2025-11-04', 'Русский', 15, '70.00', 60, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (8, 'Звездные войны: мифы и реальность', '2025-11-05', 'Русский', 20, '60.00', 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (9, 'Обзорная по музею', '2025-11-06', 'Английский', 20, '85.00', 90, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (10, 'В поисках внеземной жизни', '2025-11-07', 'Русский', 15, '65.00', 75, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (11, 'Ракетные двигатели: от РД-107 до Raptor', '2025-11-08', 'Русский', 10, '90.00', 60, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (12, 'Космическая медицина', '2025-11-09', 'Русский', 15, '55.00', 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (13, 'Обзорная по музею', '2025-11-10', 'Русский', 25, '45.00', 90, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (14, 'Как устроен телескоп Хаббл', '2025-11-11', 'Русский', 15, '70.00', 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (15, 'История скафандров', '2025-11-12', 'Русский', 20, '60.00', 75, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (16, 'Космос для детей: игра и обучение', '2025-11-13', 'Русский', 25, '35.00', 45, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (17, 'Марс: новые горизонты', '2025-11-14', 'Русский', 15, '50.00', 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (18, 'Солнечная система: путешествие по планетам', '2025-11-15', 'Английский', 20, '80.00', 90, 7);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (19, 'Космические технологии будущего', '2025-11-16', 'Русский', 20, '45.00', 75, 5);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (20, 'Астрономия для начинающих', '2025-11-17', 'Русский', 30, '30.00', 60, 6);
INSERT INTO excursion (excursion_id, title, date, language, ticket_num, price, duration, employee_id) VALUES (21, 'Космос для детей: игра и обучение', '2025-10-24', 'Русский', 20, '30.00', 60, 5);


-- Table: excursion_visitor
-- DROP TABLE IF EXISTS excursion_visitor CASCADE;

CREATE TABLE IF NOT EXISTS excursion_visitor (
    excursion_id INTEGER NOT NULL,
    visitor_id INTEGER NOT NULL,
    PRIMARY KEY (excursion_id, visitor_id),
    FOREIGN KEY (excursion_id) REFERENCES excursion(excursion_id) ON DELETE CASCADE,
    FOREIGN KEY (visitor_id) REFERENCES visitor(visitor_id) ON DELETE CASCADE
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
    exhibit_id INTEGER NOT NULL DEFAULT nextval('exhibit_exhibit_id_seq'::regclass),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    creation_date DATE,
    country VARCHAR(50),
    state VARCHAR(50),
    type VARCHAR(50),
    mission_id INTEGER,
    PRIMARY KEY (exhibit_id),
    FOREIGN KEY (mission_id) REFERENCES space_mission(mission_id) ON DELETE SET NULL
);

-- Data for exhibit
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (1, 'Спускаемый аппарат "Восток-1"', 'Оригинальный спускаемый аппарат, в котором Юрий Гагарин совершил первый полет.', '1961-01-01', 'СССР', 'На экспозиции', 'Оригинал', 1);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (2, 'Макет корабля "Аполлон-11"', 'Полноразмерный макет командного и лунного модулей.', '1970-01-01', 'США', 'На экспозиции', 'Макет', 2);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (3, 'Копия "Спутника-1"', 'Точная копия первого искусственного спутника Земли.', '1958-01-01', 'СССР', 'На экспозиции', 'Копия', 3);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (4, 'Золотая пластинка "Вояджера"', 'Копия пластинки с посланием для внеземных цивилизаций.', '1977-01-01', 'США', 'На экспозиции', 'Копия', 4);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (5, 'Скафандр "Беркут"', 'Оригинальный скафандр, использовавшийся Алексеем Леоновым.', '1964-01-01', 'СССР', 'На реставрации', 'Оригинал', 13);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (6, 'Макет станции "Салют-1"', 'Макет первой в мире орбитальной станции в масштабе 1:10.', '1972-01-01', 'СССР', 'На экспозиции', 'Макет', 8);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (7, 'Стыковочный узел "Союз-Аполлон"', 'Тренировочный образец андрогинно-периферийного агрегата стыковки.', '1974-01-01', 'СССР/США', 'На экспозиции', 'Оригинал', 7);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (8, 'Лунный камень (образец)', 'Образец лунного грунта, доставленный миссией "Луна-16".', '1970-09-24', 'СССР', 'В хранилище', 'Оригинал', NULL);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (9, 'Скафандр "Орлан-ДМА"', 'Скафандр для работы в открытом космосе на станции "Мир".', '1985-01-01', 'СССР', 'На экспозиции', 'Оригинал', 9);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (10, 'Зеркало телескопа "Хаббл" (макет)', 'Макет главного зеркала космического телескопа.', '1990-01-01', 'США', 'На экспозиции', 'Макет', 10);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (11, 'Макет марсохода "Соджорнер"', 'Полноразмерный макет первого успешного марсохода.', '1996-01-01', 'США', 'На экспозиции', 'Макет', 14);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (12, 'Спускаемый аппарат "Венера-7"', 'Оригинальный аппарат, совершивший посадку на Венеру.', '1970-01-01', 'СССР', 'На экспозиции', 'Оригинал', 6);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (13, 'Модуль "Заря" (макет)', 'Макет первого модуля МКС в масштабе 1:20.', '1998-01-01', 'Россия', 'На экспозиции', 'Макет', 12);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (14, 'Кресло "Казбек-УМ"', 'Летное кресло из корабля "Союз".', '1980-01-01', 'СССР', 'На экспозиции', 'Оригинал', NULL);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (15, 'Корабль "Орион" (макет)', 'Макет перспективного пилотируемого корабля.', '2020-01-01', 'США', 'На экспозиции', 'Макет', 15);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (16, 'Спускаемый аппарат "Восток-1"', 'Оригинальный спускаемый аппарат, в котором Белка и Стрелка совершили первый полет.', '1961-01-01', 'СССР', 'На экспозиции', 'Оригинал', 1);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (17, 'Макет корабля "Аполлон-11"', 'Полноразмерный макет командного и лунного модулей.', '1970-01-01', 'США', 'На экспозиции', 'Макет', 2);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (18, 'Копия "Спутника-1"', 'Точная копия первого искусственного спутника Марса.', '1958-01-01', 'СССР', 'На экспозиции', 'Копия', 3);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (19, 'Золотая пластинка "Вояджера"', 'Копия пластинки с посланием для внеземных цивилизаций.', '1977-01-01', 'США', 'На экспозиции', 'Копия', 4);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (20, 'Скафандр "Беркут"', 'Оригинальный скафандр, использовавшийся Юрием Гагариным.', '1964-01-01', 'СССР', 'На реставрации', 'Оригинал', 13);
INSERT INTO exhibit (exhibit_id, title, description, creation_date, country, state, type, mission_id) VALUES (21, 'Кепарис', 'Из тросника', '2002-02-22', 'РОССИЯ', 'Найс', 'Найденный', NULL);


-- Table: exhibition
-- DROP TABLE IF EXISTS exhibition CASCADE;

CREATE TABLE IF NOT EXISTS exhibition (
    exhibition_id INTEGER NOT NULL DEFAULT nextval('exhibition_exhibition_id_seq'::regclass),
    title VARCHAR(255) NOT NULL,
    theme VARCHAR(100),
    start_date DATE NOT NULL,
    end_date DATE,
    location VARCHAR(255),
    type VARCHAR(50),
    PRIMARY KEY (exhibition_id)
);

-- Data for exhibition
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (1, 'Первые в космосе', 'История советской космонавтики', '2025-01-15', '2026-01-15', 'Главный зал', 'Постоянная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (2, 'Покорители Луны', 'Лунная гонка СССР и США', '2025-09-01', '2026-03-01', 'Зал №2', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (3, 'Роботы в космосе', 'Автоматические межпланетные станции', '2024-12-01', '2025-12-01', 'Зал №3', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (4, 'Женщины в космонавтике', 'Вклад женщин в освоение космоса', '2025-03-01', '2025-06-01', 'Галерея', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (5, 'Орбитальные станции: от Салюта до МКС', 'Жизнь и работа на орбите', '2025-05-01', NULL, 'Зал №1', 'Постоянная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (6, 'Телескопы: Окно во Вселенную', 'История космических обсерваторий', '2025-10-01', '2026-02-01', 'Зал №4', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (7, 'Красная планета: Миссии на Марс', 'Исследование Марса', '2026-01-01', '2026-07-01', 'Зал №2', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (8, 'Космическая еда', 'Питание на орбите', '2025-11-01', '2026-01-01', 'Малый зал', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (9, 'Искусство и космос', 'Космос в работах художников', '2025-07-10', '2025-09-10', 'Арт-пространство', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (10, 'Частные полеты', 'Новая эра коммерческого космоса', '2026-04-01', '2026-08-01', 'Зал №3', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (11, 'Сделано в СССР', 'Достижения советской инженерии', '2025-01-01', NULL, 'Главный зал', 'Постоянная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (12, 'Космические скафандры', 'Эволюция защитного снаряжения', '2025-08-15', '2025-12-15', 'Зал №4', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (13, 'Открытый космос', 'История выходов в безвоздушное пространство', '2025-06-20', '2025-10-20', 'Зал №2', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (14, 'Венера: Неизведанная соседка', 'Исследования Венеры', '2026-02-01', '2026-05-01', 'Зал №3', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (15, 'Будущее космонавтики', 'Проекты и концепции будущего', '2026-09-01', '2027-09-01', 'Главный зал', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (16, 'Первые на Марсе', 'История американсой космонавтики', '2025-01-15', '2026-01-15', 'Главный зал', 'Постоянная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (17, 'Покорители Венеры', 'Лунная гонка СССР и США', '2025-09-01', '2026-03-01', 'Зал №2', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (18, 'Роботы в космосе для детей', 'Автоматические межпланетные станции', '2024-12-01', '2025-12-01', 'Зал №3', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (19, 'Мужчины в космонавтике', 'Вклад мужчины в освоение космоса', '2025-03-01', '2025-06-01', 'Галерея', 'Временная');
INSERT INTO exhibition (exhibition_id, title, theme, start_date, end_date, location, type) VALUES (20, 'Орбитальные станции', 'Жизнь и работа на орбите', '2025-05-01', NULL, 'Зал №1', 'Постоянная');


-- Table: exhibition_employee
-- DROP TABLE IF EXISTS exhibition_employee CASCADE;

CREATE TABLE IF NOT EXISTS exhibition_employee (
    exhibition_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    PRIMARY KEY (exhibition_id, employee_id),
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
    exhibition_id INTEGER NOT NULL,
    excursion_id INTEGER NOT NULL,
    PRIMARY KEY (exhibition_id, excursion_id),
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
    exhibition_id INTEGER NOT NULL,
    exhibit_id INTEGER NOT NULL,
    PRIMARY KEY (exhibition_id, exhibit_id),
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
    mission_id INTEGER NOT NULL DEFAULT nextval('space_mission_mission_id_seq'::regclass),
    title VARCHAR(255) NOT NULL,
    country VARCHAR(100),
    start_date DATE,
    end_date DATE,
    crew TEXT[],
    goal VARCHAR(255),
    PRIMARY KEY (mission_id)
);

-- Data for space_mission
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (1, 'Восток-1', 'СССР', '1961-04-12', '1961-04-12', ARRAY['Юрий Гагарин'], 'Первый пилотируемый полет в космос');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (2, 'Аполлон-11', 'США', '1969-07-16', '1969-07-24', ARRAY['Нил Армстронг', 'Базз Олдрин', 'Майкл Коллинз'], 'Первая высадка человека на Луну');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (3, 'Спутник-1', 'СССР', '1957-10-04', '1958-01-04', ARRAY[], 'Запуск первого искусственного спутника Земли');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (4, 'Вояджер-1', 'США', '1977-09-05', NULL, ARRAY[], 'Исследование дальних планет Солнечной системы');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (5, 'Луна-9', 'СССР', '1966-01-31', '1966-02-06', ARRAY[], 'Первая мягкая посадка на Луну');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (6, 'Венера-7', 'СССР', '1970-08-17', '1970-12-15', ARRAY[], 'Первая мягкая посадка на Венеру');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (7, 'Союз-Аполлон', 'СССР/США', '1975-07-15', '1975-07-24', ARRAY['Алексей Леонов', 'Валерий Кубасов', 'Томас Стаффорд'], 'Первая стыковка кораблей разных стран');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (8, 'Салют-1', 'СССР', '1971-04-19', '1971-10-11', ARRAY[], 'Запуск первой в мире орбитальной станции');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (9, 'Мир', 'СССР/Россия', '1986-02-19', '2001-03-23', ARRAY[], 'Создание многомодульной орбитальной станции');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (10, 'Хаббл (STS-31)', 'США/ЕКА', '1990-04-24', NULL, ARRAY['Лорен Шрайвер', 'Чарльз Болден'], 'Вывод на орбиту космического телескопа');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (11, 'Марс-3', 'СССР', '1971-05-28', '1972-08-22', ARRAY[], 'Первая мягкая посадка на Марс');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (12, 'Международная космическая станция (МКС)', 'Международный', '1998-11-20', NULL, ARRAY[], 'Создание международной пилотируемой орбитальной станции');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (13, 'Восход-2', 'СССР', '1965-03-18', '1965-03-19', ARRAY['Павел Беляев', 'Алексей Леонов'], 'Первый выход человека в открытый космос');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (14, 'Mars Pathfinder', 'США', '1996-12-04', '1997-09-27', ARRAY[], 'Доставка первого марсохода "Соджорнер"');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (15, 'Артемида-1', 'США', '2022-11-16', '2022-12-11', ARRAY[], 'Беспилотный облет Луны кораблем "Орион"');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (16, 'Чанъэ-5', 'Китай', '2020-11-23', '2020-12-16', ARRAY[], 'Доставка лунного грунта на Землю');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (17, 'Perseverance', 'США', '2020-07-30', NULL, ARRAY[], 'Поиск следов жизни на Марсе и сбор образцов');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (18, 'Hayabusa2', 'Япония', '2014-12-03', '2020-12-05', ARRAY[], 'Исследование астероида Рюгу и доставка образцов');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (19, 'Джеймс Уэбб', 'США/ЕКА/Канада', '2021-12-25', NULL, ARRAY[], 'Исследование ранней Вселенной в инфракрасном диапазоне');
INSERT INTO space_mission (mission_id, title, country, start_date, end_date, crew, goal) VALUES (20, 'Венера-Д', 'Россия', '2024-11-01', NULL, ARRAY[], 'Комплексное исследование атмосферы и поверхности Венеры');


-- Table: visitor
-- DROP TABLE IF EXISTS visitor CASCADE;

CREATE TABLE IF NOT EXISTS visitor (
    visitor_id INTEGER NOT NULL DEFAULT nextval('visitor_visitor_id_seq'::regclass),
    full_name VARCHAR(255) NOT NULL,
    birth_date DATE,
    citizenship VARCHAR(100),
    ticket_type VARCHAR(50),
    visit_date DATE,
    review TEXT,
    PRIMARY KEY (visitor_id)
);

-- Data for visitor
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (1, 'Александров Александр Александрович', '1990-05-15', 'Россия', 'Взрослый', '2025-10-20', 'Очень понравилась выставка про Луну!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (2, 'Борисова Богдана Борисовна', '2015-01-20', 'Россия', 'Детский', '2025-10-20', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (3, 'John Smith', '1985-11-30', 'США', 'Взрослый', '2025-10-21', 'Amazing collection of Soviet space history.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (4, 'Мария Иванова', '1992-07-22', 'Беларусь', 'Взрослый', '2025-10-21', 'Впечатляет!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (5, 'Сергеев Сергей Сергеевич', '1978-03-12', 'Россия', 'Взрослый', '2025-10-22', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (6, 'Орлова Ольга Олеговна', '1995-09-05', 'Россия', 'Льготный', '2025-10-22', 'Спасибо за интересную экскурсию.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (7, 'Григорьев Григорий Григорьевич', '2001-12-01', 'Казахстан', 'Взрослый', '2025-10-23', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (8, 'Антонова Антонина Антоновна', '1965-02-18', 'Россия', 'Пенсионный', '2025-10-23', 'Вспомнила молодость, спасибо!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (9, 'Wei Zhang', '1998-08-08', 'Китай', 'Взрослый', '2025-10-24', 'Very educational.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (10, 'Давыдов Давид Давидович', '2017-06-10', 'Россия', 'Детский', '2025-10-24', 'Ракета большая!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (11, 'Егоров Егор Егорович', '1988-04-04', 'Россия', 'Взрослый', '2025-10-25', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (12, 'Фомина Фаина Федоровна', '1999-10-10', 'Россия', 'Студенческий', '2025-10-25', 'Приду еще раз с друзьями.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (13, 'Hans Schmidt', '1975-01-25', 'Германия', 'Взрослый', '2025-10-26', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (14, 'Кириллов Кирилл Кириллович', '2003-07-07', 'Россия', 'Взрослый', '2025-10-26', 'Круто, но мало интерактива.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (15, 'Лазарева Лариса Львовна', '1982-11-11', 'Украина', 'Взрослый', '2025-10-27', 'Очень познавательно.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (16, 'Александров Александр Александрович', '1990-05-15', 'Россия', 'Взрослый', '2025-10-20', 'Очень понравилась выставка про Марс!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (17, 'Борисова Богдана Борисовна', '2015-01-20', 'Россия', 'Детский', '2025-10-20', NULL);
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (18, 'Mitt Smith', '1985-11-30', 'США', 'Взрослый', '2025-10-21', 'Amazing collection of Soviet space history.');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (19, 'Наталья Иванова', '1992-07-22', 'Беларусь', 'Взрослый', '2025-10-21', 'Круто!');
INSERT INTO visitor (visitor_id, full_name, birth_date, citizenship, ticket_type, visit_date, review) VALUES (20, 'Сергеев Андрей Сергеевич', '1978-03-12', 'Россия', 'Взрослый', '2025-10-22', NULL);


-- Reset sequences
SELECT setval(pg_get_serial_sequence('employee', 'employee_id'), COALESCE((SELECT MAX(employee_id) FROM employee), 1));
SELECT setval(pg_get_serial_sequence('excursion', 'excursion_id'), COALESCE((SELECT MAX(excursion_id) FROM excursion), 1));
SELECT setval(pg_get_serial_sequence('exhibit', 'exhibit_id'), COALESCE((SELECT MAX(exhibit_id) FROM exhibit), 1));
SELECT setval(pg_get_serial_sequence('exhibition', 'exhibition_id'), COALESCE((SELECT MAX(exhibition_id) FROM exhibition), 1));
SELECT setval(pg_get_serial_sequence('space_mission', 'mission_id'), COALESCE((SELECT MAX(mission_id) FROM space_mission), 1));
SELECT setval(pg_get_serial_sequence('visitor', 'visitor_id'), COALESCE((SELECT MAX(visitor_id) FROM visitor), 1));
