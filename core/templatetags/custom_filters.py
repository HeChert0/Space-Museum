# core/templatetags/custom_filters.py

from django import template
from django.template.defaultfilters import stringfilter
import datetime
import re

register = template.Library()


@register.filter
def get_item(obj, key):
    """Получить атрибут объекта или элемент словаря по ключу"""
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(key)
    try:
        return getattr(obj, key, None)
    except:
        return None


@register.filter
def length(value):
    """Получить длину значения"""
    if value is None:
        return 0
    return len(str(value))


@register.filter
def dict_get(dict_obj, key):
    """Получить значение из словаря по ключу"""
    if isinstance(dict_obj, dict):
        return dict_obj.get(key, '')
    return getattr(dict_obj, key, '')

@register.filter
def is_array(value):
    """Проверяет, является ли значение массивом PostgreSQL"""
    if value and isinstance(value, str):
        return value.startswith('{') and value.endswith('}')
    return False


@register.filter
def format_array(value):
    """Форматирует PostgreSQL массивы для отображения"""
    if value is None:
        return ''

    # Если это строка, начинающаяся с { и заканчивающаяся }, это массив PostgreSQL
    if isinstance(value, str) and value.startswith('{') and value.endswith('}'):
        # Убираем фигурные скобки и возвращаем элементы через запятую
        return value[1:-1]

    return value


@register.filter
def format_date(value):
    """Форматирует дату в формат dd.mm.yyyy"""
    if value is None:
        return ''

    # Если это объект datetime
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.strftime('%d.%m.%Y')

    # Если это строка с датой
    if isinstance(value, str):
        # Убираем слово midnight и время
        value = value.replace(' midnight', '').replace(' 00:00:00', '')

        # Убираем время если есть
        if ' ' in value:
            value = value.split(' ')[0]

        # Пробуем разные форматы
        try:
            # Формат YYYY-MM-DD
            if '-' in value and len(value) == 10:
                parts = value.split('-')
                if len(parts) == 3 and len(parts[0]) == 4:
                    date_obj = datetime.datetime.strptime(value, '%Y-%m-%d')
                    return date_obj.strftime('%d.%m.%Y')
        except:
            pass

        # Проверяем на невалидные годы
        if '-' in value:
            year_str = value.split('-')[0]
            try:
                year = int(year_str)
                if year < 1 or year > 9999:
                    return f"Некорректная дата: {value}"
            except:
                pass

    return str(value).replace(' midnight', '').replace(' 00:00:00', '')


@register.filter
def is_array_field(field_type):
    """Проверяет, является ли поле массивом"""
    return field_type and 'ARRAY' in field_type.upper()


@register.filter
def format_for_input(value, field_type):
    """Форматирует значение для input поля"""
    if value is None:
        return ''

    # Для массивов убираем фигурные скобки
    if field_type and 'ARRAY' in field_type.upper():
        if isinstance(value, str) and value.startswith('{') and value.endswith('}'):
            return value[1:-1]

    # Для дат форматируем в YYYY-MM-DD для input type="date"
    if field_type == 'date':
        if isinstance(value, (datetime.date, datetime.datetime)):
            return value.strftime('%Y-%m-%d')
        elif isinstance(value, str):
            # Убираем midnight и время
            value = value.replace(' midnight', '').replace(' 00:00:00', '')
            if ' ' in value:
                return value.split(' ')[0]
            return value

    return value


@register.filter
def format_phone(value):
    """Форматирует телефонные номера, убирая лишние символы"""
    if value is None:
        return ''

    value_str = str(value)

    # Если строка начинается с +, это телефон - убираем все кроме цифр и +
    if value_str.startswith('+'):
        # Сохраняем + в начале и убираем все нецифровые символы
        cleaned = '+' + ''.join(filter(str.isdigit, value_str[1:]))
        return cleaned

    return value_str
