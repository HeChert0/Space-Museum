# core/validators.py
import re
from datetime import date, datetime
from django.core.exceptions import ValidationError

# Списки для выпадающих меню
COUNTRIES = [
    'Россия', 'Беларусь', 'США', 'Китай', 'Казахстан', 'Украина',
    'Германия', 'Япония', 'Индия', 'Франция', 'Великобритания'
]

TICKET_TYPES = ['Взрослый', 'Детский', 'Пенсионный', 'Студенческий']

DEPARTMENTS = [
    'Отдел фондов', 'Выставочный отдел', 'Реставрационная мастерская',
    'Экскурсионный отдел', 'Научный отдел', 'IT-отдел', 'Бухгалтерия',
    'Служба безопасности', 'Отдел кадров', 'АХО', 'Администрация'
]

POSITIONS_BY_DEPARTMENT = {
    'Отдел фондов': ['Главный хранитель', 'Хранитель', 'Помощник хранителя'],
    'Выставочный отдел': ['Заведующий отделом выставок', 'Экспозитор', 'Помощник экспозитора'],
    'Реставрационная мастерская': ['Главный реставратор', 'Реставратор', 'Реставратор высшей категории'],
    'Экскурсионный отдел': ['Главный экскурсовод', 'Экскурсовод', 'Экскурсовод-стажер'],
    'Научный отдел': ['Научный сотрудник', 'Младший научный сотрудник', 'Старший научный сотрудник'],
    'IT-отдел': ['IT-специалист', 'Системный администратор', 'Программист'],
    'Бухгалтерия': ['Главный бухгалтер', 'Бухгалтер', 'Помощник бухгалтера'],
    'Служба безопасности': ['Начальник службы безопасности', 'Специалист по безопасности', 'Охранник'],
    'Отдел кадров': ['Начальник отдела кадров', 'Менеджер по персоналу', 'Специалист по кадрам'],
    'АХО': ['Заведующий АХО', 'Специалист АХО', 'Техник'],
    'Администрация': ['Директор музея', 'Заместитель директора', 'Секретарь директора']
}

EXHIBITION_LOCATIONS = ['Главный зал', 'Зал №1', 'Зал №2', 'Зал №3', 'Зал №4', 'Малый зал', 'Арт-пространство',
                        'Галерея']
EXHIBITION_TYPES = ['Постоянная', 'Временная']

EXCURSION_LANGUAGES = ['Русский', 'Английский', 'Белорусский']

SPACE_COUNTRIES = ['США', 'СССР', 'Россия', 'Китай', 'Индия', 'Япония', 'ЕКА', 'Международный']

EXHIBIT_STATES = ['На экспозиции', 'На реставрации', 'В хранилище']
EXHIBIT_TYPES = ['Макет', 'Копия', 'Оригинал']


def validate_fio(fio):
    """Валидация ФИО - только буквы и дефис"""
    fio = fio.strip()

    if not fio:
        raise ValidationError('ФИО не может быть пустым')

    # Проверка на допустимые символы (только буквы и дефис)
    if not re.match(r'^[а-яА-ЯёЁa-zA-Z\-\s]+$', fio):
        raise ValidationError('ФИО может содержать только буквы и дефис')

    # Проверка на минимальную длину
    if len(fio) < 5:
        raise ValidationError('ФИО слишком короткое')

    # Проверка на максимальную длину
    if len(fio) > 100:
        raise ValidationError('ФИО слишком длинное')

    # Проверка на наличие хотя бы одного пробела (должно быть минимум 2 слова)
    parts = fio.split()
    if len(parts) < 2:
        raise ValidationError('ФИО должно содержать минимум фамилию и имя')

    # Проверка каждой части ФИО
    for part in parts:
        # Каждая часть должна начинаться с заглавной буквы
        if not part[0].isupper():
            raise ValidationError('Каждая часть ФИО должна начинаться с заглавной буквы')

        # Проверка на недопустимые комбинации
        if '--' in part:
            raise ValidationError('Недопустимы двойные дефисы')

        # Часть не может начинаться или заканчиваться дефисом
        if part.startswith('-') or part.endswith('-'):
            raise ValidationError('Части ФИО не могут начинаться или заканчиваться дефисом')

    return fio


def validate_phone(phone, country_code):
    """Валидация телефона"""
    # Убираем все нецифровые символы
    digits_only = re.sub(r'\D', '', phone)

    if country_code == '+375':  # Беларусь
        if len(digits_only) != 9:
            raise ValidationError('Белорусский номер должен содержать 9 цифр после кода')
    elif country_code == '+7':  # Россия
        if len(digits_only) != 10:
            raise ValidationError('Российский номер должен содержать 10 цифр после кода')
    else:
        raise ValidationError('Неподдерживаемый код страны')

    return country_code + digits_only


def validate_date_format(date_str):
    """Проверка формата даты дд.мм.гггг"""
    try:
        return datetime.strptime(date_str, '%d.%m.%Y').date()
    except ValueError:
        raise ValidationError('Дата должна быть в формате ДД.ММ.ГГГГ')


def validate_text_field(value, max_length, min_length=0, allow_digits=False, allow_special=False):
    """Универсальная валидация текстовых полей"""
    if not value or len(value.strip()) < min_length:
        raise ValidationError(f'Поле должно содержать минимум {min_length} символов')

    if len(value) > max_length:
        raise ValidationError(f'Поле не может быть длиннее {max_length} символов')

    # Проверка на пустые символы
    if value.strip() == '':
        raise ValidationError('Поле не может состоять только из пробелов')

    # Проверка на цифры
    if not allow_digits and re.search(r'\d', value):
        raise ValidationError('Поле не может содержать цифры')

    # Проверка на спецсимволы
    if not allow_special and re.search(r'[!@#$%^&*_+=\[\]{};:\\|<>/?`~]', value):
        raise ValidationError('Поле содержит недопустимые символы')

    return value.strip()


def check_unique_id(model_class, id_field, id_value, exclude_id=None):
    """Проверка уникальности ID"""
    query = {id_field: id_value}
    queryset = model_class.objects.filter(**query)

    if exclude_id:
        queryset = queryset.exclude(**{id_field: exclude_id})

    if queryset.exists():
        raise ValidationError(f'Запись с ID {id_value} уже существует')

    return id_value


# Добавим класс для ошибок с указанием поля
class FieldValidationError(ValidationError):
    def init(self, message, field=None):
        super().init(message)
        self.field = field


def check_unique_phone(model_class, phone_value, exclude_id=None):
    """Проверка уникальности телефона"""
    queryset = model_class.objects.filter(phone=phone_value)

    if exclude_id:
        queryset = queryset.exclude(employee_id=exclude_id)

    if queryset.exists():
        error = FieldValidationError(f'Сотрудник с телефоном {phone_value} уже существует')
        error.field = 'phone_number'
        raise error

    return phone_value
