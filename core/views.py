# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection, transaction
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import *
import pandas as pd
from datetime import datetime
import os
from django.conf import settings
import openpyxl
import openpyxl.utils


def home(request):
    return render(request, 'core/home.html')


def entities_menu(request):
    entity = request.GET.get('entity', '')
    operation = request.GET.get('operation', '')

    if entity and operation:
        if operation == 'view':
            return redirect(f'{entity}_list')
        elif operation == 'add':
            return redirect(f'{entity}_add')
        elif operation == 'update':
            return redirect(f'{entity}_update')
        elif operation == 'delete':
            return redirect(f'{entity}_delete')

    return render(request, 'core/entities_menu.html')


# ============= VISITOR CRUD =============
def visitor_list(request):
    visitors = Visitor.objects.all()

    filter_column = request.GET.get('filter_column', '')
    filter_value = request.GET.get('filter_value', '')

    if filter_column and filter_value:
        filter_dict = {filter_column + '__icontains': filter_value}
        visitors = visitors.filter(**filter_dict)

    if request.GET.get('save_result'):
        return save_query_result(list(visitors.values()), 'visitors_filtered')

    columns = ['id', 'full_name', 'birth_date', 'citizenship', 'ticket_type', 'visit_date', 'review']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Посетители',
        'items': visitors,
        'columns': columns,
        'entity_type': 'visitor',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def visitor_add(request):
    if request.method == 'POST':
        try:
            visitor = Visitor(
                full_name=request.POST['full_name'],
                birth_date=request.POST['birth_date'],
                citizenship=request.POST['citizenship'],
                ticket_type=request.POST['ticket_type'],
                visit_date=request.POST['visit_date'],
                review=request.POST.get('review', '')
            )

            # Валидация: дата посещения не может быть раньше даты рождения
            if visitor.visit_date < visitor.birth_date:
                messages.error(request, 'Дата посещения не может быть раньше даты рождения!')
                return redirect('visitor_add')

            visitor.save()
            messages.success(request, 'Посетитель успешно добавлен!')
            return redirect('visitor_list')
        except Exception as e:
            messages.error(request, f'Ошибка при добавлении: {str(e)}')

    fields = [
        {'name': 'full_name', 'label': 'ФИО', 'type': 'text', 'required': True},
        {'name': 'birth_date', 'label': 'Дата рождения', 'type': 'date', 'required': True},
        {'name': 'citizenship', 'label': 'Гражданство', 'type': 'text', 'required': True},
        {'name': 'ticket_type', 'label': 'Тип билета', 'type': 'text', 'required': True},
        {'name': 'visit_date', 'label': 'Дата посещения', 'type': 'date', 'required': True},
        {'name': 'review', 'label': 'Отзыв', 'type': 'textarea', 'required': False},
    ]

    return render(request, 'core/entity_form_add.html', {
        'entity_name': 'Посетитель',
        'operation': 'Добавить',
        'fields': fields,
        'entity_type': 'visitor'
    })


def visitor_update(request):
    visitors = Visitor.objects.all()
    selected_id = request.GET.get('id')

    if selected_id:
        visitor = get_object_or_404(Visitor, id=selected_id)

        if request.method == 'POST':
            try:
                visitor.full_name = request.POST['full_name']
                visitor.birth_date = request.POST['birth_date']
                visitor.citizenship = request.POST['citizenship']
                visitor.ticket_type = request.POST['ticket_type']
                visitor.visit_date = request.POST['visit_date']
                visitor.review = request.POST.get('review', '')

                # Валидация
                if visitor.visit_date < visitor.birth_date:
                    messages.error(request, 'Дата посещения не может быть раньше даты рождения!')
                    return redirect(f'visitor_update?id={selected_id}')

                visitor.save()
                messages.success(request, 'Посетитель успешно обновлен!')
                return redirect('visitor_list')
            except Exception as e:
                messages.error(request, f'Ошибка при обновлении: {str(e)}')

        fields = [
            {'name': 'full_name', 'label': 'ФИО', 'type': 'text', 'required': True, 'value': visitor.full_name},
            {'name': 'birth_date', 'label': 'Дата рождения', 'type': 'date', 'required': True,
             'value': visitor.birth_date},
            {'name': 'citizenship', 'label': 'Гражданство', 'type': 'text', 'required': True,
             'value': visitor.citizenship},
            {'name': 'ticket_type', 'label': 'Тип билета', 'type': 'text', 'required': True,
             'value': visitor.ticket_type},
            {'name': 'visit_date', 'label': 'Дата посещения', 'type': 'date', 'required': True,
             'value': visitor.visit_date},
            {'name': 'review', 'label': 'Отзыв', 'type': 'textarea', 'required': False, 'value': visitor.review or ''},
        ]

        return render(request, 'core/entity_form_update.html', {
            'entity_name': 'Посетитель',
            'operation': 'Обновить',
            'fields': fields,
            'entity_type': 'visitor'
        })

    columns = ['id', 'full_name', 'birth_date', 'citizenship']
    return render(request, 'core/entity_select.html', {
        'entity_name': 'Посетитель',
        'items': visitors,
        'columns': columns,
        'entity_type': 'visitor',
        'operation': 'обновления'
    })


def visitor_delete(request):
    if request.method == 'POST':
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                visitor = Visitor.objects.get(id=delete_id)
                visitor.delete()
                messages.success(request, f'Посетитель "{visitor.full_name}" успешно удален!')
            except Visitor.DoesNotExist:
                messages.error(request, 'Посетитель не найден!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('visitor_delete')

    visitors = Visitor.objects.all()
    columns = ['id', 'full_name', 'birth_date', 'citizenship']

    return render(request, 'core/entity_select.html', {
        'entity_name': 'Посетитель',
        'items': visitors,
        'columns': columns,
        'entity_type': 'visitor',
        'operation': 'удаления'
    })


# ============= EMPLOYEE CRUD =============
def employee_list(request):
    employees = Employee.objects.all()

    filter_column = request.GET.get('filter_column', '')
    filter_value = request.GET.get('filter_value', '')

    if filter_column and filter_value:
        filter_dict = {filter_column + '__icontains': filter_value}
        employees = employees.filter(**filter_dict)

    if request.GET.get('save_result'):
        return save_query_result(list(employees.values()), 'employees_filtered')

    columns = ['id', 'full_name', 'position', 'hire_date', 'department', 'phone', 'qualification']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Сотрудники',
        'items': employees,
        'columns': columns,
        'entity_type': 'employee',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def employee_add(request):
    if request.method == 'POST':
        try:
            employee = Employee(
                full_name=request.POST['full_name'],
                position=request.POST['position'],
                hire_date=request.POST['hire_date'],
                department=request.POST['department'],
                phone=request.POST['phone'],
                qualification=request.POST['qualification']
            )

            # Валидация: дата найма не может быть в будущем
            from datetime import date
            if employee.hire_date > date.today():
                messages.error(request, 'Дата найма не может быть в будущем!')
                return redirect('employee_add')

            employee.save()
            messages.success(request, 'Сотрудник успешно добавлен!')
            return redirect('employee_list')
        except Exception as e:
            messages.error(request, f'Ошибка при добавлении: {str(e)}')

    fields = [
        {'name': 'full_name', 'label': 'ФИО', 'type': 'text', 'required': True},
        {'name': 'position', 'label': 'Должность', 'type': 'text', 'required': True},
        {'name': 'hire_date', 'label': 'Дата найма', 'type': 'date', 'required': True},
        {'name': 'department', 'label': 'Отдел', 'type': 'text', 'required': True},
        {'name': 'phone', 'label': 'Телефон', 'type': 'text', 'required': True},
        {'name': 'qualification', 'label': 'Квалификация', 'type': 'text', 'required': True},
    ]

    return render(request, 'core/entity_form_add.html', {
        'entity_name': 'Сотрудник',
        'operation': 'Добавить',
        'fields': fields,
        'entity_type': 'employee'
    })


def employee_update(request):
    employees = Employee.objects.all()
    selected_id = request.GET.get('id')

    if selected_id:
        employee = get_object_or_404(Employee, id=selected_id)

        if request.method == 'POST':
            try:
                employee.full_name = request.POST['full_name']
                employee.position = request.POST['position']
                employee.hire_date = request.POST['hire_date']
                employee.department = request.POST['department']
                employee.phone = request.POST['phone']
                employee.qualification = request.POST['qualification']

                # Валидация
                from datetime import date
                if employee.hire_date > date.today():
                    messages.error(request, 'Дата найма не может быть в будущем!')
                    return redirect(f'employee_update?id={selected_id}')

                employee.save()
                messages.success(request, 'Сотрудник успешно обновлен!')
                return redirect('employee_list')
            except Exception as e:
                messages.error(request, f'Ошибка при обновлении: {str(e)}')

        fields = [
            {'name': 'full_name', 'label': 'ФИО', 'type': 'text', 'required': True, 'value': employee.full_name},
            {'name': 'position', 'label': 'Должность', 'type': 'text', 'required': True, 'value': employee.position},
            {'name': 'hire_date', 'label': 'Дата найма', 'type': 'date', 'required': True, 'value': employee.hire_date},
            {'name': 'department', 'label': 'Отдел', 'type': 'text', 'required': True, 'value': employee.department},
            {'name': 'phone', 'label': 'Телефон', 'type': 'text', 'required': True, 'value': employee.phone},
            {'name': 'qualification', 'label': 'Квалификация', 'type': 'text', 'required': True,
             'value': employee.qualification},
        ]

        return render(request, 'core/entity_form_update.html', {
            'entity_name': 'Сотрудник',
            'operation': 'Обновить',
            'fields': fields,
            'entity_type': 'employee'
        })

    columns = ['id', 'full_name', 'position', 'department']
    return render(request, 'core/entity_select.html', {
        'entity_name': 'Сотрудник',
        'items': employees,
        'columns': columns,
        'entity_type': 'employee',
        'operation': 'обновления'
    })


def employee_delete(request):
    if request.method == 'POST':
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                employee = Employee.objects.get(id=delete_id)
                employee.delete()
                messages.success(request, f'Сотрудник "{employee.full_name}" успешно удален!')
            except Employee.DoesNotExist:
                messages.error(request, 'Сотрудник не найден!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('employee_delete')

    employees = Employee.objects.all()
    columns = ['id', 'full_name', 'position', 'department']

    return render(request, 'core/entity_select.html', {
        'entity_name': 'Сотрудник',
        'items': employees,
        'columns': columns,
        'entity_type': 'employee',
        'operation': 'удаления'
    })


# ============= EXHIBITION CRUD =============
def exhibition_list(request):
    exhibitions = Exhibition.objects.all()

    filter_column = request.GET.get('filter_column', '')
    filter_value = request.GET.get('filter_value', '')

    if filter_column and filter_value:
        filter_dict = {filter_column + '__icontains': filter_value}
        exhibitions = exhibitions.filter(**filter_dict)

    if request.GET.get('save_result'):
        return save_query_result(list(exhibitions.values()), 'exhibitions_filtered')

    columns = ['id', 'title', 'theme', 'start_date', 'end_date', 'location', 'type']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Выставки',
        'items': exhibitions,
        'columns': columns,
        'entity_type': 'exhibition',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def exhibition_add(request):
    if request.method == 'POST':
        try:
            exhibition = Exhibition(
                title=request.POST['title'],
                theme=request.POST['theme'],
                start_date=request.POST['start_date'],
                end_date=request.POST['end_date'],
                location=request.POST['location'],
                type=request.POST['type']
            )

            # Валидация: дата окончания не может быть раньше даты начала
            if exhibition.end_date < exhibition.start_date:
                messages.error(request, 'Дата окончания не может быть раньше даты начала!')
                return redirect('exhibition_add')

            exhibition.save()
            messages.success(request, 'Выставка успешно добавлена!')
            return redirect('exhibition_list')
        except Exception as e:
            messages.error(request, f'Ошибка при добавлении: {str(e)}')

    fields = [
        {'name': 'title', 'label': 'Название', 'type': 'text', 'required': True},
        {'name': 'theme', 'label': 'Тема', 'type': 'text', 'required': True},
        {'name': 'start_date', 'label': 'Дата начала', 'type': 'date', 'required': True},
        {'name': 'end_date', 'label': 'Дата окончания', 'type': 'date', 'required': True},
        {'name': 'location', 'label': 'Место проведения', 'type': 'text', 'required': True},
        {'name': 'type', 'label': 'Тип', 'type': 'text', 'required': True},
    ]

    return render(request, 'core/entity_form_add.html', {
        'entity_name': 'Выставка',
        'operation': 'Добавить',
        'fields': fields,
        'entity_type': 'exhibition'
    })


def exhibition_update(request):
    exhibitions = Exhibition.objects.all()
    selected_id = request.GET.get('id')

    if selected_id:
        exhibition = get_object_or_404(Exhibition, id=selected_id)

        if request.method == 'POST':
            try:
                exhibition.title = request.POST['title']
                exhibition.theme = request.POST['theme']
                exhibition.start_date = request.POST['start_date']
                exhibition.end_date = request.POST['end_date']
                exhibition.location = request.POST['location']
                exhibition.type = request.POST['type']

                # Валидация
                if exhibition.end_date < exhibition.start_date:
                    messages.error(request, 'Дата окончания не может быть раньше даты начала!')
                    return redirect(f'exhibition_update?id={selected_id}')

                exhibition.save()
                messages.success(request, 'Выставка успешно обновлена!')
                return redirect('exhibition_list')
            except Exception as e:
                messages.error(request, f'Ошибка при обновлении: {str(e)}')

        fields = [
            {'name': 'title', 'label': 'Название', 'type': 'text', 'required': True, 'value': exhibition.title},
            {'name': 'theme', 'label': 'Тема', 'type': 'text', 'required': True, 'value': exhibition.theme},
            {'name': 'start_date', 'label': 'Дата начала', 'type': 'date', 'required': True,
             'value': exhibition.start_date},
            {'name': 'end_date', 'label': 'Дата окончания', 'type': 'date', 'required': True,
             'value': exhibition.end_date},
            {'name': 'location', 'label': 'Место проведения', 'type': 'text', 'required': True,
             'value': exhibition.location},
            {'name': 'type', 'label': 'Тип', 'type': 'text', 'required': True, 'value': exhibition.type},
        ]

        return render(request, 'core/entity_form_update.html', {
            'entity_name': 'Выставка',
            'operation': 'Обновить',
            'fields': fields,
            'entity_type': 'exhibition'
        })

    columns = ['id', 'title', 'theme', 'location']
    return render(request, 'core/entity_select.html', {
        'entity_name': 'Выставка',
        'items': exhibitions,
        'columns': columns,
        'entity_type': 'exhibition',
        'operation': 'обновления'
    })


def exhibition_delete(request):
    if request.method == 'POST':
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                exhibition = Exhibition.objects.get(id=delete_id)
                exhibition.delete()
                messages.success(request, f'Выставка "{exhibition.title}" успешно удалена!')
            except Exhibition.DoesNotExist:
                messages.error(request, 'Выставка не найдена!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('exhibition_delete')

    exhibitions = Exhibition.objects.all()
    columns = ['id', 'title', 'theme', 'location']

    return render(request, 'core/entity_select.html', {
        'entity_name': 'Выставка',
        'items': exhibitions,
        'columns': columns,
        'entity_type': 'exhibition',
        'operation': 'удаления'
    })


# ============= EXCURSION CRUD =============
def excursion_list(request):
    excursions = Excursion.objects.all()

    filter_column = request.GET.get('filter_column', '')
    filter_value = request.GET.get('filter_value', '')

    if filter_column and filter_value:
        filter_dict = {filter_column + '__icontains': filter_value}
        excursions = excursions.filter(**filter_dict)

    if request.GET.get('save_result'):
        return save_query_result(list(excursions.values()), 'excursions_filtered')

    columns = ['id', 'title', 'date', 'language', 'ticket_num', 'price', 'duration', 'employee_id']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Экскурсии',
        'items': excursions,
        'columns': columns,
        'entity_type': 'excursion',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def excursion_add(request):
    if request.method == 'POST':
        try:
            excursion = Excursion(
                title=request.POST['title'],
                date=request.POST['date'],
                language=request.POST['language'],
                ticket_num=request.POST['ticket_num'],
                price=request.POST['price'],
                duration=request.POST['duration']
            )

            # Обработка employee_id
            employee_id = request.POST.get('employee_id', '')
            if employee_id:
                try:
                    excursion.employee = Employee.objects.get(id=employee_id)
                except Employee.DoesNotExist:
                    messages.error(request, f'Сотрудник с ID {employee_id} не найден!')
                    return redirect('excursion_add')

            # Валидация
            if int(excursion.ticket_num) < 0:
                messages.error(request, 'Количество билетов не может быть отрицательным!')
                return redirect('excursion_add')

            if float(excursion.price) < 0:
                messages.error(request, 'Цена не может быть отрицательной!')
                return redirect('excursion_add')

            if int(excursion.duration) <= 0:
                messages.error(request, 'Продолжительность должна быть положительной!')
                return redirect('excursion_add')

            excursion.save()
            messages.success(request, 'Экскурсия успешно добавлена!')
            return redirect('excursion_list')
        except Exception as e:
            messages.error(request, f'Ошибка при добавлении: {str(e)}')

    fields = [
        {'name': 'title', 'label': 'Название', 'type': 'text', 'required': True},
        {'name': 'date', 'label': 'Дата', 'type': 'date', 'required': True},
        {'name': 'language', 'label': 'Язык', 'type': 'text', 'required': True},
        {'name': 'ticket_num', 'label': 'Количество билетов', 'type': 'number', 'required': True},
        {'name': 'price', 'label': 'Цена', 'type': 'number', 'required': True},
        {'name': 'duration', 'label': 'Продолжительность (минуты)', 'type': 'number', 'required': True},
        {'name': 'employee_id', 'label': 'ID сотрудника', 'type': 'number', 'required': False},
    ]

    return render(request, 'core/entity_form_add.html', {
        'entity_name': 'Экскурсия',
        'operation': 'Добавить',
        'fields': fields,
        'entity_type': 'excursion'
    })


def excursion_update(request):
    excursions = Excursion.objects.all()
    selected_id = request.GET.get('id')

    if selected_id:
        excursion = get_object_or_404(Excursion, id=selected_id)

        if request.method == 'POST':
            try:
                excursion.title = request.POST['title']
                excursion.date = request.POST['date']
                excursion.language = request.POST['language']
                excursion.ticket_num = request.POST['ticket_num']
                excursion.price = request.POST['price']
                excursion.duration = request.POST['duration']

                employee_id = request.POST.get('employee_id', '')
                if employee_id:
                    try:
                        excursion.employee = Employee.objects.get(id=employee_id)
                    except Employee.DoesNotExist:
                        messages.error(request, f'Сотрудник с ID {employee_id} не найден!')
                        return redirect(f'excursion_update?id={selected_id}')
                else:
                    excursion.employee = None

                # Валидация
                if int(excursion.ticket_num) < 0:
                    messages.error(request, 'Количество билетов не может быть отрицательным!')
                    return redirect(f'excursion_update?id={selected_id}')

                if float(excursion.price) < 0:
                    messages.error(request, 'Цена не может быть отрицательной!')
                    return redirect(f'excursion_update?id={selected_id}')

                if int(excursion.duration) <= 0:
                    messages.error(request, 'Продолжительность должна быть положительной!')
                    return redirect(f'excursion_update?id={selected_id}')

                excursion.save()
                messages.success(request, 'Экскурсия успешно обновлена!')
                return redirect('excursion_list')
            except Exception as e:
                messages.error(request, f'Ошибка при обновлении: {str(e)}')

        fields = [
            {'name': 'title', 'label': 'Название', 'type': 'text', 'required': True, 'value': excursion.title},
            {'name': 'date', 'label': 'Дата', 'type': 'date', 'required': True, 'value': excursion.date},
            {'name': 'language', 'label': 'Язык', 'type': 'text', 'required': True, 'value': excursion.language},
            {'name': 'ticket_num', 'label': 'Количество билетов', 'type': 'number', 'required': True,
             'value': excursion.ticket_num},
            {'name': 'price', 'label': 'Цена', 'type': 'number', 'required': True, 'value': excursion.price},
            {'name': 'duration', 'label': 'Продолжительность (минуты)', 'type': 'number', 'required': True,
             'value': excursion.duration},
            {'name': 'employee_id', 'label': 'ID сотрудника', 'type': 'number', 'required': False,
             'value': excursion.employee_id if excursion.employee else ''},
        ]

        return render(request, 'core/entity_form_update.html', {
            'entity_name': 'Экскурсия',
            'operation': 'Обновить',
            'fields': fields,
            'entity_type': 'excursion'
        })

    columns = ['id', 'title', 'date', 'language']
    return render(request, 'core/entity_select.html', {
        'entity_name': 'Экскурсия',
        'items': excursions,
        'columns': columns,
        'entity_type': 'excursion',
        'operation': 'обновления'
    })


def excursion_delete(request):
    if request.method == 'POST':
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                excursion = Excursion.objects.get(id=delete_id)
                excursion.delete()
                messages.success(request, f'Экскурсия "{excursion.title}" успешно удалена!')
            except Excursion.DoesNotExist:
                messages.error(request, 'Экскурсия не найдена!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('excursion_delete')

    excursions = Excursion.objects.all()
    columns = ['id', 'title', 'date', 'language']

    return render(request, 'core/entity_select.html', {
        'entity_name': 'Экскурсия',
        'items': excursions,
        'columns': columns,
        'entity_type': 'excursion',
        'operation': 'удаления'
    })


# ============= EXHIBIT CRUD =============
def exhibit_list(request):
    exhibits = Exhibit.objects.all()

    filter_column = request.GET.get('filter_column', '')
    filter_value = request.GET.get('filter_value', '')

    if filter_column and filter_value:
        filter_dict = {filter_column + '__icontains': filter_value}
        exhibits = exhibits.filter(**filter_dict)

    if request.GET.get('save_result'):
        return save_query_result(list(exhibits.values()), 'exhibits_filtered')

    columns = ['id', 'title', 'description', 'creation_date', 'country', 'state', 'type', 'mission_id']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Экспонаты',
        'items': exhibits,
        'columns': columns,
        'entity_type': 'exhibit',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def exhibit_add(request):
    if request.method == 'POST':
        try:
            exhibit = Exhibit(
                title=request.POST['title'],
                description=request.POST['description'],
                creation_date=request.POST['creation_date'],
                country=request.POST['country'],
                state=request.POST['state'],
                type=request.POST['type']
            )

            mission_id = request.POST.get('mission_id', '')
            if mission_id:
                try:
                    exhibit.mission = SpaceMission.objects.get(id=mission_id)
                except SpaceMission.DoesNotExist:
                    messages.error(request, f'Миссия с ID {mission_id} не найдена!')
                    return redirect('exhibit_add')

            # Валидация: дата создания не может быть в будущем
            from datetime import date
            if exhibit.creation_date > date.today():
                messages.error(request, 'Дата создания не может быть в будущем!')
                return redirect('exhibit_add')

            exhibit.save()
            messages.success(request, 'Экспонат успешно добавлен!')
            return redirect('exhibit_list')
        except Exception as e:
            messages.error(request, f'Ошибка при добавлении: {str(e)}')

    fields = [
        {'name': 'title', 'label': 'Название', 'type': 'text', 'required': True},
        {'name': 'description', 'label': 'Описание', 'type': 'textarea', 'required': True},
        {'name': 'creation_date', 'label': 'Дата создания', 'type': 'date', 'required': True},
        {'name': 'country', 'label': 'Страна', 'type': 'text', 'required': True},
        {'name': 'state', 'label': 'Состояние', 'type': 'text', 'required': True},
        {'name': 'type', 'label': 'Тип', 'type': 'text', 'required': True},
        {'name': 'mission_id', 'label': 'ID миссии', 'type': 'number', 'required': False},
    ]

    return render(request, 'core/entity_form_add.html', {
        'entity_name': 'Экспонат',
        'operation': 'Добавить',
        'fields': fields,
        'entity_type': 'exhibit'
    })


def exhibit_update(request):
    exhibits = Exhibit.objects.all()
    selected_id = request.GET.get('id')

    if selected_id:
        exhibit = get_object_or_404(Exhibit, id=selected_id)

        if request.method == 'POST':
            try:
                exhibit.title = request.POST['title']
                exhibit.description = request.POST['description']
                exhibit.creation_date = request.POST['creation_date']
                exhibit.country = request.POST['country']
                exhibit.state = request.POST['state']
                exhibit.type = request.POST['type']

                mission_id = request.POST.get('mission_id', '')
                if mission_id:
                    try:
                        exhibit.mission = SpaceMission.objects.get(id=mission_id)
                    except SpaceMission.DoesNotExist:
                        messages.error(request, f'Миссия с ID {mission_id} не найдена!')
                        return redirect(f'exhibit_update?id={selected_id}')
                else:
                    exhibit.mission = None

                # Валидация
                from datetime import date
                if exhibit.creation_date > date.today():
                    messages.error(request, 'Дата создания не может быть в будущем!')
                    return redirect(f'exhibit_update?id={selected_id}')

                exhibit.save()
                messages.success(request, 'Экспонат успешно обновлен!')
                return redirect('exhibit_list')
            except Exception as e:
                messages.error(request, f'Ошибка при обновлении: {str(e)}')

        fields = [
            {'name': 'title', 'label': 'Название', 'type': 'text', 'required': True, 'value': exhibit.title},
            {'name': 'description', 'label': 'Описание', 'type': 'textarea', 'required': True,
             'value': exhibit.description},
            {'name': 'creation_date', 'label': 'Дата создания', 'type': 'date', 'required': True,
             'value': exhibit.creation_date},
            {'name': 'country', 'label': 'Страна', 'type': 'text', 'required': True, 'value': exhibit.country},
            {'name': 'state', 'label': 'Состояние', 'type': 'text', 'required': True, 'value': exhibit.state},
            {'name': 'type', 'label': 'Тип', 'type': 'text', 'required': True, 'value': exhibit.type},
            {'name': 'mission_id', 'label': 'ID миссии', 'type': 'number', 'required': False,
             'value': exhibit.mission_id if exhibit.mission else ''},
        ]

        return render(request, 'core/entity_form_update.html', {
            'entity_name': 'Экспонат',
            'operation': 'Обновить',
            'fields': fields,
            'entity_type': 'exhibit'
        })

    columns = ['id', 'title', 'country', 'type']
    return render(request, 'core/entity_select.html', {
        'entity_name': 'Экспонат',
        'items': exhibits,
        'columns': columns,
        'entity_type': 'exhibit',
        'operation': 'обновления'
    })


def exhibit_delete(request):
    if request.method == 'POST':
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                exhibit = Exhibit.objects.get(id=delete_id)
                exhibit.delete()
                messages.success(request, f'Экспонат "{exhibit.title}" успешно удален!')
            except Exhibit.DoesNotExist:
                messages.error(request, 'Экспонат не найден!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('exhibit_delete')

    exhibits = Exhibit.objects.all()
    columns = ['id', 'title', 'country', 'type']

    return render(request, 'core/entity_select.html', {
        'entity_name': 'Экспонат',
        'items': exhibits,
        'columns': columns,
        'entity_type': 'exhibit',
        'operation': 'удаления'
    })


# ============= SPACE MISSION CRUD =============
def mission_list(request):
    missions = SpaceMission.objects.all()

    filter_column = request.GET.get('filter_column', '')
    filter_value = request.GET.get('filter_value', '')

    if filter_column and filter_value:
        filter_dict = {filter_column + '__icontains': filter_value}
        missions = missions.filter(**filter_dict)

    if request.GET.get('save_result'):
        return save_query_result(list(missions.values()), 'missions_filtered')

    columns = ['id', 'title', 'country', 'start_date', 'end_date', 'crew', 'goal']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Космические миссии',
        'items': missions,
        'columns': columns,
        'entity_type': 'mission',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def mission_add(request):
    if request.method == 'POST':
        try:
            mission = SpaceMission(
                title=request.POST['title'],
                country=request.POST['country'],
                start_date=request.POST['start_date'],
                end_date=request.POST['end_date'],
                crew=request.POST['crew'],
                goal=request.POST['goal']
            )

            # Валидация: дата окончания не может быть раньше даты начала
            if mission.end_date < mission.start_date:
                messages.error(request, 'Дата окончания не может быть раньше даты начала!')
                return redirect('mission_add')

            mission.save()
            messages.success(request, 'Космическая миссия успешно добавлена!')
            return redirect('mission_list')
        except Exception as e:
            messages.error(request, f'Ошибка при добавлении: {str(e)}')

    fields = [
        {'name': 'title', 'label': 'Название', 'type': 'text', 'required': True},
        {'name': 'country', 'label': 'Страна', 'type': 'text', 'required': True},
        {'name': 'start_date', 'label': 'Дата начала', 'type': 'date', 'required': True},
        {'name': 'end_date', 'label': 'Дата окончания', 'type': 'date', 'required': True},
        {'name': 'crew', 'label': 'Экипаж', 'type': 'textarea', 'required': True},
        {'name': 'goal', 'label': 'Цель', 'type': 'text', 'required': True},
    ]

    return render(request, 'core/entity_form_add.html', {
        'entity_name': 'Космическая миссия',
        'operation': 'Добавить',
        'fields': fields,
        'entity_type': 'mission'
    })


def mission_update(request):
    missions = SpaceMission.objects.all()
    selected_id = request.GET.get('id')

    if selected_id:
        mission = get_object_or_404(SpaceMission, id=selected_id)

        if request.method == 'POST':
            try:
                mission.title = request.POST['title']
                mission.country = request.POST['country']
                mission.start_date = request.POST['start_date']
                mission.end_date = request.POST['end_date']
                mission.crew = request.POST['crew']
                mission.goal = request.POST['goal']

                # Валидация
                if mission.end_date < mission.start_date:
                    messages.error(request, 'Дата окончания не может быть раньше даты начала!')
                    return redirect(f'mission_update?id={selected_id}')

                mission.save()
                messages.success(request, 'Космическая миссия успешно обновлена!')
                return redirect('mission_list')
            except Exception as e:
                messages.error(request, f'Ошибка при обновлении: {str(e)}')

        fields = [
            {'name': 'title', 'label': 'Название', 'type': 'text', 'required': True, 'value': mission.title},
            {'name': 'country', 'label': 'Страна', 'type': 'text', 'required': True, 'value': mission.country},
            {'name': 'start_date', 'label': 'Дата начала', 'type': 'date', 'required': True,
             'value': mission.start_date},
            {'name': 'end_date', 'label': 'Дата окончания', 'type': 'date', 'required': True,
             'value': mission.end_date},
            {'name': 'crew', 'label': 'Экипаж', 'type': 'textarea', 'required': True, 'value': mission.crew},
            {'name': 'goal', 'label': 'Цель', 'type': 'text', 'required': True, 'value': mission.goal},
        ]

        return render(request, 'core/entity_form_update.html', {
            'entity_name': 'Космическая миссия',
            'operation': 'Обновить',
            'fields': fields,
            'entity_type': 'mission'
        })

    columns = ['id', 'title', 'country', 'goal']
    return render(request, 'core/entity_select.html', {
        'entity_name': 'Космическая миссия',
        'items': missions,
        'columns': columns,
        'entity_type': 'mission',
        'operation': 'обновления'
    })


def mission_delete(request):
    if request.method == 'POST':
        delete_id = request.POST.get('delete_id')
        if delete_id:
            try:
                mission = SpaceMission.objects.get(id=delete_id)
                mission.delete()
                messages.success(request, f'Миссия "{mission.title}" успешно удалена!')
            except SpaceMission.DoesNotExist:
                messages.error(request, 'Миссия не найдена!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('mission_delete')

    missions = SpaceMission.objects.all()
    columns = ['id', 'title', 'country', 'goal']

    return render(request, 'core/entity_select.html', {
        'entity_name': 'Космическая миссия',
        'items': missions,
        'columns': columns,
        'entity_type': 'mission',
        'operation': 'удаления'
    })


# ============= UTILITY FUNCTIONS =============
def save_query_result(data, name):
    """Сохранение результата запроса в Excel"""
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{name}_{timestamp}.xlsx'
    filepath = os.path.join(backup_dir, filename)

    df = pd.DataFrame(data)

    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name=name[:31])  # Excel ограничение на имя листа

        # Автоматическая настройка ширины колонок
        worksheet = writer.sheets[name[:31]]
        for idx, col in enumerate(df.columns):
            max_length = max(
                df[col].astype(str).map(len).max() if not df.empty else 0,
                len(str(col))
            ) + 2
            worksheet.column_dimensions[openpyxl.utils.get_column_letter(idx + 1)].width = min(max_length, 50)

    return HttpResponse(f'Результат запроса сохранен в файл {filename}')


def save_database_state(request):
    """Сохранение состояния всей БД"""
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'backup_{timestamp}.xlsx'
    filepath = os.path.join(backup_dir, filename)

    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        tables = {
            'visitors': Visitor.objects.all().values(),
            'employees': Employee.objects.all().values(),
            'exhibitions': Exhibition.objects.all().values(),
            'excursions': Excursion.objects.all().values(),
            'exhibits': Exhibit.objects.all().values(),
            'missions': SpaceMission.objects.all().values(),
        }

        for sheet_name, data in tables.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Автоматическая настройка ширины колонок
            worksheet = writer.sheets[sheet_name]
            for idx, col in enumerate(df.columns):
                max_length = max(
                    df[col].astype(str).map(len).max() if not df.empty else 0,
                    len(str(col))
                ) + 2
                worksheet.column_dimensions[openpyxl.utils.get_column_letter(idx + 1)].width = min(max_length, 50)

    messages.success(request, f'Состояние базы данных сохранено в файл {filename}')
    return redirect('home')


def special_queries(request):
    """Страница для специальных SQL запросов"""
    query_result = None
    columns = []
    lab_type = request.POST.get('lab_type', '')
    selected_query = request.POST.get('query_type', '')

    # Словарь всех запросов Лабораторной работы 5
    lab5_queries = {
        # Employee запросы
        'emp_1': """SELECT e.full_name AS "ФИО", e.position FROM employee e""",
        'emp_2': """SELECT * FROM employee WHERE position = 'Экскурсовод'""",
        'emp_3': """SELECT * FROM employee ORDER BY hire_date ASC""",
        'emp_4': """SELECT * FROM employee WHERE full_name LIKE 'П%'""",

        # Excursion запросы
        'exc_1': """SELECT e.title AS "Название выставки", e.date FROM excursion e""",
        'exc_2': """SELECT title, duration FROM excursion ORDER BY duration DESC""",
        'exc_3': """SELECT DISTINCT title FROM excursion WHERE title LIKE '%Косм%'""",
        'exc_4': """SELECT e.full_name, ex.title AS excursion 
                    FROM employee AS e 
                    INNER JOIN excursion AS ex ON e.employee_id = ex.employee_id""",
        'exc_5': """SELECT e.full_name, e.position, ex.title AS excursion_title, ex.language 
                    FROM employee AS e 
                    LEFT JOIN excursion AS ex ON e.employee_id = ex.employee_id""",
        'exc_6': """SELECT ex.title AS excursion_title, ex.language, e.full_name, e.position 
                    FROM employee AS e 
                    RIGHT JOIN excursion AS ex ON e.employee_id = ex.employee_id""",
        'exc_7': """SELECT e.employee_id, e.full_name, e.position, 
                    ex.excursion_id, ex.title AS excursion_title, ex.date, ex.language 
                    FROM employee AS e 
                    FULL JOIN excursion AS ex ON e.employee_id = ex.employee_id""",

        # Exhibit запросы
        'exh_1': """SELECT e.title AS "Название экспоната", e.state FROM exhibit e""",
        'exh_2': """SELECT title, creation_date, country FROM exhibit 
                    WHERE creation_date < '1970-01-01' AND country = 'СССР'""",
        'exh_3': """SELECT title, creation_date FROM exhibit ORDER BY creation_date ASC""",
        'exh_4': """SELECT DISTINCT title FROM exhibit WHERE title LIKE '%Макет%'""",
        'exh_5': """SELECT e.title AS exhibit_title, e.type, m.title AS mission_name, m.start_date 
                    FROM exhibit AS e 
                    INNER JOIN space_mission AS m ON e.mission_id = m.mission_id""",
        'exh_6': """SELECT e.title AS exhibit_title, e.country, e.type, 
                    m.title AS mission_name, m.start_date 
                    FROM exhibit AS e 
                    LEFT JOIN space_mission AS m ON e.mission_id = m.mission_id""",
        'exh_7': """SELECT m.title AS mission_name, m.start_date, 
                    e.title AS exhibit_title, e.type 
                    FROM exhibit AS e 
                    RIGHT JOIN space_mission AS m ON e.mission_id = m.mission_id""",
        'exh_8': """SELECT e.exhibit_id, e.title AS exhibit_title, e.type, 
                    m.mission_id, m.title AS mission_name, m.start_date 
                    FROM exhibit AS e 
                    FULL JOIN space_mission AS m ON e.mission_id = m.mission_id""",

        # Space Mission запросы
        'sm_1': """SELECT s.title AS "Название Миссии", s.country FROM space_mission s""",
        'sm_2': """SELECT title, start_date, end_date FROM space_mission 
                   WHERE start_date > '1970-01-01' AND end_date < '2000-01-01'""",
        'sm_3': """SELECT title, country FROM space_mission ORDER BY country DESC""",
        'sm_4': """SELECT title, country FROM space_mission WHERE country LIKE '%США%'""",

        # Exhibition запросы
        'exb_1': """SELECT e.title AS "Название выставки", e.theme FROM exhibition e""",
        'exb_2': """SELECT title, start_date, end_date, type FROM exhibition 
                    WHERE type = 'Временная' AND end_date IS NOT NULL""",
        'exb_3': """SELECT title, start_date, end_date FROM exhibition ORDER BY end_date ASC""",
        'exb_4': """SELECT title, location FROM exhibition WHERE location LIKE '%Зал%'""",
        'exb_5': """SELECT ex.title AS exhibition_title, ex.location, e.full_name, e.position 
                    FROM exhibition AS ex 
                    INNER JOIN exhibition_employee AS ee ON ex.exhibition_id = ee.exhibition_id 
                    INNER JOIN employee AS e ON ee.employee_id = e.employee_id""",
        'exb_6': """SELECT ex.title AS exhibition_title, ex.theme, ex.location, 
                    e.full_name, e.position 
                    FROM exhibition AS ex 
                    LEFT JOIN exhibition_employee AS ee ON ex.exhibition_id = ee.exhibition_id 
                    LEFT JOIN employee AS e ON ee.employee_id = e.employee_id""",
        'exb_7': """SELECT e.full_name, e.position, ex.title AS exhibition_title, ex.location 
                    FROM exhibition AS ex 
                    RIGHT JOIN exhibition_employee AS ee ON ex.exhibition_id = ee.exhibition_id 
                    RIGHT JOIN employee AS e ON ee.employee_id = e.employee_id""",
        'exb_8': """SELECT ex.exhibition_id, ex.title AS exhibition_title, ex.location, 
                    e.employee_id, e.full_name, e.position 
                    FROM exhibition AS ex 
                    FULL JOIN exhibition_employee AS ee ON ex.exhibition_id = ee.exhibition_id 
                    FULL JOIN employee AS e ON ee.employee_id = e.employee_id""",

        # Visitor запросы
        'vis_1': """SELECT v.ticket_type AS "Тип билета", v.full_name, v.citizenship FROM visitor v""",
        'vis_2': """SELECT full_name, review FROM visitor WHERE review IS NOT NULL""",
        'vis_3': """SELECT full_name, birth_date FROM visitor ORDER BY birth_date DESC""",
        'vis_4': """SELECT full_name, review FROM visitor WHERE review LIKE '%!%'""",
        'vis_5': """SELECT ex.title AS excursion_title, ex.date AS excursion_date, 
                    v.full_name AS visitor_name, v.ticket_type 
                    FROM excursion AS ex 
                    INNER JOIN excursion_visitor AS ev ON ex.excursion_id = ev.excursion_id 
                    INNER JOIN visitor AS v ON ev.visitor_id = v.visitor_id""",
        'vis_6': """SELECT ex.excursion_id, ex.title AS excursion_title, ex.date, ex.language, 
                    v.visitor_id, v.full_name AS visitor_name, v.visit_date 
                    FROM excursion AS ex 
                    LEFT JOIN excursion_visitor AS ev ON ex.excursion_id = ev.excursion_id 
                    LEFT JOIN visitor AS v ON ev.visitor_id = v.visitor_id""",
        'vis_7': """SELECT v.full_name AS visitor_name, v.ticket_type, 
                    ex.excursion_id, ex.title AS excursion_title, ex.date 
                    FROM excursion AS ex 
                    RIGHT JOIN excursion_visitor AS ev ON ex.excursion_id = ev.excursion_id 
                    RIGHT JOIN visitor AS v ON ev.visitor_id = v.visitor_id""",
        'vis_8': """SELECT ex.excursion_id, ex.title AS excursion_title, ex.date, 
                    v.visitor_id, v.full_name AS visitor_name, v.visit_date 
                    FROM excursion AS ex 
                    FULL JOIN excursion_visitor AS ev ON ex.excursion_id = ev.excursion_id 
                    FULL JOIN visitor AS v ON ev.visitor_id = v.visitor_id"""
    }

    lab6_queries = {
        'lab6_1': """
            SELECT 
                e.employee_id,
                e.full_name,
                COUNT(ex.excursion_id) AS excursions_conducted,
                SUM(ex.ticket_num) AS total_tickets
            FROM employee e
            LEFT JOIN excursion ex ON e.employee_id = ex.employee_id
            WHERE e.department = 'Экскурсионный отдел'
            GROUP BY e.employee_id, e.full_name
            HAVING COUNT(ex.excursion_id) > ALL(
                SELECT COUNT(ex2.excursion_id)
                FROM employee e2
                LEFT JOIN excursion ex2 ON e2.employee_id = ex2.employee_id
                WHERE e2.department = 'Администрация'
                GROUP BY e2.employee_id
            )
            INTERSECT ALL
            SELECT 
                e.employee_id,
                e.full_name,
                COUNT(ex.excursion_id) AS excursions_conducted,
                SUM(ex.ticket_num) AS total_tickets
            FROM employee e
            LEFT JOIN excursion ex ON e.employee_id = ex.employee_id
            WHERE e.department = 'Экскурсионный отдел'
            GROUP BY e.employee_id, e.full_name
            HAVING COUNT(ex.excursion_id) >= 2 AND SUM(ex.ticket_num) > 100
            ORDER BY excursions_conducted DESC, total_tickets DESC
        """,

        'lab6_2': """
            SELECT excursion_id, title, language, duration, ticket_num
            FROM excursion
            WHERE language = 'Русский'
            GROUP BY excursion_id, title, language, duration, ticket_num
            HAVING duration = (SELECT MIN(duration) FROM excursion WHERE language = 'Русский')
            INTERSECT
            SELECT excursion_id, title, language, duration, ticket_num
            FROM excursion
            WHERE language = 'Русский'
            GROUP BY excursion_id, title, language, duration, ticket_num
            HAVING ticket_num > (SELECT AVG(ticket_num) FROM excursion WHERE language = 'Русский')
            ORDER BY duration, ticket_num
        """,

        'lab6_3': """
            WITH country_stats AS (
                SELECT 
                    country,
                    COUNT(*) as exhibit_count,
                    AVG(EXTRACT(YEAR FROM creation_date)) as avg_year
                FROM exhibit
                WHERE EXTRACT(YEAR FROM creation_date) > 1960
                GROUP BY country
                HAVING COUNT(*) > 2
            )
            SELECT country, exhibit_count, avg_year
            FROM country_stats
            UNION
            SELECT 
                country,
                COUNT(*) as exhibit_count,
                AVG(EXTRACT(YEAR FROM creation_date)) as avg_year
            FROM exhibit
            WHERE country NOT IN (
                SELECT DISTINCT country
                FROM exhibit
                WHERE type = 'Макет'
            )
            GROUP BY country
            ORDER BY exhibit_count DESC, avg_year DESC
        """,

        'lab6_4': """
            SELECT 
                country,
                COUNT(*) as mission_count,
                MAX(EXTRACT(YEAR FROM start_date)) as max_start_year
            FROM space_mission
            GROUP BY country
            HAVING COUNT(*) > ANY(
                SELECT COUNT(*)
                FROM space_mission
                GROUP BY country
                HAVING COUNT(*) < 3
            )
            UNION ALL
            SELECT 
                country,
                COUNT(*) as mission_count,
                MAX(EXTRACT(YEAR FROM start_date)) as max_start_year
            FROM space_mission
            WHERE goal LIKE '%первый%'
            GROUP BY country
            ORDER BY mission_count DESC, max_start_year DESC
        """,

        'lab6_5': """
            SELECT 
                e.exhibition_id,
                e.title,
                e.type,
                COUNT(ex.exhibit_id) as exhibit_count
            FROM exhibition e
            INNER JOIN exhibit ex ON e.exhibition_id = ex.exhibition_id
            WHERE e.location = 'Главный зал'
            GROUP BY e.exhibition_id, e.title, e.type
            HAVING COUNT(ex.exhibit_id) > 2
            EXCEPT ALL
            SELECT 
                e.exhibition_id,
                e.title,
                e.type,
                COUNT(ex.exhibit_id) as exhibit_count
            FROM exhibition e
            INNER JOIN exhibit ex ON e.exhibition_id = ex.exhibition_id
            WHERE e.type = 'Временная'
            GROUP BY e.exhibition_id, e.title, e.type
            ORDER BY exhibit_count DESC
        """,

        'lab6_6': """
            SELECT 
                visitor_id,
                full_name,
                birth_date,
                COUNT(review) as review_count
            FROM visitor
            WHERE review IS NOT NULL
            GROUP BY visitor_id, full_name, birth_date
            HAVING COUNT(review) >= 1
            EXCEPT
            SELECT 
                visitor_id,
                full_name,
                birth_date,
                COUNT(review) as review_count
            FROM visitor
            WHERE birth_date < '1950-01-01'
            GROUP BY visitor_id, full_name, birth_date
            ORDER BY birth_date DESC
        """
    }

    if request.method == 'POST':
        query_sql = None

        if lab_type == 'lab5' and selected_query in lab5_queries:
            query_sql = lab5_queries[selected_query]
        elif lab_type == 'lab6' and selected_query in lab6_queries:
            query_sql = lab6_queries[selected_query]

        if query_sql:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query_sql)
                    columns = [col[0] for col in cursor.description]
                    query_result = cursor.fetchall()
            except Exception as e:
                messages.error(request, f'Ошибка выполнения запроса: {str(e)}')

        # Сохранение результата
        if request.POST.get('save_result') and query_result:
            return save_query_result(
                [dict(zip(columns, row)) for row in query_result],
                'special_query'
            )

    return render(request, 'core/special_queries.html', {
        'query_result': query_result,
        'columns': columns,
        'selected_query': selected_query,
        'lab_type': lab_type
    })