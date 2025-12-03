# core/templatetags/custom_filters.py

from django import template
import re

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return getattr(dictionary, key, '')

@register.filter
def dict_get(dict_obj, key):
    """Получить значение из словаря по ключу"""
    if isinstance(dict_obj, dict):
        return dict_obj.get(key, '')
    return getattr(dict_obj, key, '')

@register.filter
def format_array(value):
    """Форматирует PostgreSQL массив для отображения"""
    if value and isinstance(value, str):
        # Проверяем, является ли это массивом PostgreSQL
        if value.startswith('{') and value.endswith('}'):
            # Убираем фигурные скобки
            content = value[1:-1]
            # Убираем кавычки и форматируем
            content = content.replace('"', '')
            # Если элементы разделены запятыми
            if ',' in content:
                items = content.split(',')
                return ', '.join(items)
            return content
        # Проверяем на багованный формат (каждая буква через запятую)
        elif value.count(', ') == len(value.replace(', ', '')) - 1 and len(value) > 10:
            # Убираем лишние запятые между буквами
            return value.replace(', ', '')
    return value

@register.filter
def is_array(value):
    """Проверяет, является ли значение массивом PostgreSQL"""
    if value and isinstance(value, str):
        return value.startswith('{') and value.endswith('}')
    return False
