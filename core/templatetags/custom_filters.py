# core/templatetags/custom_filters.py

from django import template

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
