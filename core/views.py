from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection, transaction, models
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import *
import pandas as pd
from datetime import datetime, date
import os
from django.conf import settings
import openpyxl
import openpyxl.utils
import json
import subprocess
import tempfile



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

    columns = ['visitor_id', 'full_name', 'birth_date', 'citizenship', 'ticket_type', 'visit_date', 'review']

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
            # Получаем максимальный ID
            max_id = Visitor.objects.aggregate(models.Max('visitor_id'))['visitor_id__max']
            new_id = (max_id or 0) + 1

            # Преобразуем строки в даты
            birth_date = datetime.strptime(request.POST['birth_date'], '%Y-%m-%d').date()
            visit_date = datetime.strptime(request.POST['visit_date'], '%Y-%m-%d').date()

            # Валидация
            if visit_date < birth_date:
                messages.error(request, 'Дата посещения не может быть раньше даты рождения!')
                return redirect('visitor_add')

            visitor = Visitor(
                visitor_id=new_id,
                full_name=request.POST['full_name'],
                birth_date=birth_date,
                citizenship=request.POST['citizenship'],
                ticket_type=request.POST['ticket_type'],
                visit_date=visit_date,
                review=request.POST.get('review', '')
            )

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
        visitor = get_object_or_404(Visitor, visitor_id=selected_id)

        if request.method == 'POST':
            try:
                visitor.full_name = request.POST['full_name']

                # Преобразуем строки в даты
                birth_date = datetime.strptime(request.POST['birth_date'], '%Y-%m-%d').date()
                visit_date = datetime.strptime(request.POST['visit_date'], '%Y-%m-%d').date()

                # Валидация
                if visit_date < birth_date:
                    messages.error(request, 'Дата посещения не может быть раньше даты рождения!')
                    return redirect(f'visitor_update?id={selected_id}')

                visitor.birth_date = birth_date
                visitor.visit_date = visit_date
                visitor.citizenship = request.POST['citizenship']
                visitor.ticket_type = request.POST['ticket_type']
                visitor.review = request.POST.get('review', '')

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

    columns = ['visitor_id', 'full_name', 'birth_date', 'citizenship']
    return render(request, 'core/entity_select.html', {
        'entity_name': 'Посетитель',
        'items': visitors,
        'columns': columns,
        'entity_type': 'visitor',
        'operation': 'обновления'
    })

    columns = ['visitor_id', 'full_name', 'birth_date', 'citizenship']
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
                visitor = Visitor.objects.get(visitor_id=delete_id)
                visitor.delete()
                messages.success(request, f'Посетитель "{visitor.full_name}" успешно удален!')
            except Visitor.DoesNotExist:
                messages.error(request, 'Посетитель не найден!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('visitor_delete')

    visitors = Visitor.objects.all()
    columns = ['visitor_id', 'full_name', 'birth_date', 'citizenship']

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

    columns = ['employee_id', 'full_name', 'position', 'hire_date', 'department', 'phone', 'qualification']

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
            # Получаем максимальный ID
            max_id = Employee.objects.aggregate(models.Max('employee_id'))['employee_id__max']
            new_id = (max_id or 0) + 1

            # Преобразуем строку в дату
            hire_date = datetime.strptime(request.POST['hire_date'], '%Y-%m-%d').date()

            # Валидация
            if hire_date > date.today():
                messages.error(request, 'Дата найма не может быть в будущем!')
                return redirect('employee_add')

            employee = Employee(
                employee_id=new_id,
                full_name=request.POST['full_name'],
                position=request.POST['position'],
                hire_date=hire_date,
                department=request.POST['department'],
                phone=request.POST['phone'],
                qualification=request.POST['qualification']
            )

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
        employee = get_object_or_404(Employee, employee_id=selected_id)

        if request.method == 'POST':
            try:
                employee.full_name = request.POST['full_name']
                employee.position = request.POST['position']

                hire_date = datetime.strptime(request.POST['hire_date'], '%Y-%m-%d').date()

                if hire_date > date.today():
                    messages.error(request, 'Дата найма не может быть в будущем!')
                    return redirect(f'employee_update?id={selected_id}')

                employee.hire_date = hire_date
                employee.department = request.POST['department']
                employee.phone = request.POST['phone']
                employee.qualification = request.POST['qualification']

                # Валидация

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

    columns = ['employee_id', 'full_name', 'position', 'department']
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
                employee = Employee.objects.get(employee_id=delete_id)
                employee.delete()
                messages.success(request, f'Сотрудник "{employee.full_name}" успешно удален!')
            except Employee.DoesNotExist:
                messages.error(request, 'Сотрудник не найден!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('employee_delete')

    employees = Employee.objects.all()
    columns = ['employee_id', 'full_name', 'position', 'department']

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

    columns = ['exhibition_id', 'title', 'theme', 'start_date', 'end_date', 'location', 'type']

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
            # Получаем максимальный ID
            max_id = Exhibition.objects.aggregate(models.Max('exhibition_id'))['exhibition_id__max']
            new_id = (max_id or 0) + 1

            # Преобразуем строки в даты
            start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()

            # Валидация
            if end_date < start_date:
                messages.error(request, 'Дата окончания не может быть раньше даты начала!')
                return redirect('exhibition_add')

            exhibition = Exhibition(
                exhibition_id=new_id,
                title=request.POST['title'],
                theme=request.POST['theme'],
                start_date=start_date,
                end_date=end_date,
                location=request.POST['location'],
                type=request.POST['type']
            )

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
        exhibition = get_object_or_404(Exhibition, exhibition_id=selected_id)

        if request.method == 'POST':
            try:
                exhibition.title = request.POST['title']
                exhibition.theme = request.POST['theme']

                start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
                end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()

                # Валидация
                if end_date < start_date:
                    messages.error(request, 'Дата начала не может быть больше даты окончания!')
                    return redirect(f'exhibition_update?id={selected_id}')

                exhibition.start_date = start_date
                exhibition.end_date = end_date
                exhibition.location = request.POST['location']
                exhibition.type = request.POST['type']

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

    columns = ['exhibition_id', 'title', 'theme', 'location']
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
                exhibition = Exhibition.objects.get(exhibition_id=delete_id)
                exhibition.delete()
                messages.success(request, f'Выставка "{exhibition.title}" успешно удалена!')
            except Exhibition.DoesNotExist:
                messages.error(request, 'Выставка не найдена!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('exhibition_delete')

    exhibitions = Exhibition.objects.all()
    columns = ['exhibition_id', 'title', 'theme', 'location']

    return render(request, 'core/entity_select.html', {
        'entity_name': 'Выставка',
        'items': exhibitions,
        'columns': columns,
        'entity_type': 'exhibition',
        'operation': 'удаления'
    })


# ============= EXCURSION CRUD =============
def excursion_list(request):
    # Аналогично для экскурсий
    excursions = Excursion.objects.select_related('employee').all()

    filter_column = request.GET.get('filter_column', '')
    filter_value = request.GET.get('filter_value', '')

    if filter_column and filter_value:
        filter_dict = {filter_column + '__icontains': filter_value}
        excursions = excursions.filter(**filter_dict)

    if request.GET.get('save_result'):
        data = []
        for excursion in excursions:
            data.append({
                'excursion_id': excursion.excursion_id,
                'title': excursion.title,
                'date': excursion.date,
                'language': excursion.language,
                'ticket_num': excursion.ticket_num,
                'price': excursion.price,
                'duration': excursion.duration,
                'employee': excursion.employee.full_name if excursion.employee else None
            })
        return save_query_result(data, 'excursions_filtered')

    # Подготавливаем данные для отображения
    excursions_display = []
    for excursion in excursions:
        excursions_display.append({
            'excursion_id': excursion.excursion_id,
            'title': excursion.title,
            'date': excursion.date,
            'language': excursion.language,
            'ticket_num': excursion.ticket_num,
            'price': excursion.price,
            'duration': excursion.duration,
            'employee_name': excursion.employee.full_name if excursion.employee else None
        })

    columns = ['excursion_id', 'title', 'date', 'language', 'ticket_num', 'price', 'duration', 'employee_id']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Экскурсии',
        'items': excursions_display,
        'columns': columns,
        'entity_type': 'excursion',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def excursion_add(request):
    if request.method == 'POST':
        try:
            # Получаем максимальный ID
            max_id = Excursion.objects.aggregate(models.Max('excursion_id'))['excursion_id__max']
            new_id = (max_id or 0) + 1

            # Преобразуем строку в дату
            excursion_date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()

            excursion = Excursion(
                excursion_id=new_id,
                title=request.POST['title'],
                date=excursion_date,
                language=request.POST['language'],
                ticket_num=request.POST['ticket_num'],
                price=request.POST['price'],
                duration=request.POST['duration']
            )

            # Обработка employee_id
            employee_id_value = request.POST.get('employee_id', '').strip()
            if employee_id_value:
                try:
                    employee = Employee.objects.get(employee_id=int(employee_id_value))
                    excursion.employee = employee  # Присваиваем объект
                except (ValueError, Employee.DoesNotExist):
                    messages.error(request, f'Сотрудник с ID {employee_id_value} не найден!')
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
        {'name': 'price', 'label': 'Цена', 'type': 'number', 'required': True, 'step': '0.01'},
        {'name': 'duration', 'label': 'Продолжительность (минуты)', 'type': 'number', 'required': True},
        {'name': 'employee_id', 'label': 'ID сотрудника (необязательно)', 'type': 'number', 'required': False},
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
        excursion = get_object_or_404(Excursion, excursion_id=selected_id)

        if request.method == 'POST':
            try:
                excursion.title = request.POST['title']

                # Преобразуем строку в дату
                excursion_date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
                excursion.date = excursion_date

                excursion.language = request.POST['language']
                excursion.ticket_num = request.POST['ticket_num']
                excursion.price = request.POST['price']
                excursion.duration = request.POST['duration']

                employee_id_value = request.POST.get('employee_id', '').strip()
                if employee_id_value:
                    try:
                        employee = Employee.objects.get(employee_id=int(employee_id_value))
                        excursion.employee = employee
                    except (ValueError, Employee.DoesNotExist):
                        messages.error(request, f'Сотрудник с ID {employee_id_value} не найден!')
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
            {'name': 'price', 'label': 'Цена', 'type': 'number', 'required': True, 'step': '0.01',
             'value': excursion.price},
            {'name': 'duration', 'label': 'Продолжительность (минуты)', 'type': 'number', 'required': True,
             'value': excursion.duration},
            {'name': 'employee_id', 'label': 'ID сотрудника (необязательно)', 'type': 'number', 'required': False,
             'value': excursion.employee_id if excursion.employee else ''},
        ]

        return render(request, 'core/entity_form_update.html', {
            'entity_name': 'Экскурсия',
            'operation': 'Обновить',
            'fields': fields,
            'entity_type': 'excursion'
        })

    columns = ['excursion_id', 'title', 'date', 'language']
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
                excursion = Excursion.objects.get(excursion_id=delete_id)
                excursion.delete()
                messages.success(request, f'Экскурсия "{excursion.title}" успешно удалена!')
            except Excursion.DoesNotExist:
                messages.error(request, 'Экскурсия не найдена!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('excursion_delete')

    excursions = Excursion.objects.all()
    columns = ['excursion_id', 'title', 'date', 'language']

    return render(request, 'core/entity_select.html', {
        'entity_name': 'Экскурсия',
        'items': excursions,
        'columns': columns,
        'entity_type': 'excursion',
        'operation': 'удаления'
    })


# ============= EXHIBIT CRUD =============
def exhibit_list(request):
    # Используем правильное имя поля - mission_id
    exhibits = Exhibit.objects.select_related('mission_id').all()

    filter_column = request.GET.get('filter_column', '')
    filter_value = request.GET.get('filter_value', '')

    if filter_column and filter_value:
        filter_dict = {filter_column + '__icontains': filter_value}
        exhibits = exhibits.filter(**filter_dict)

    if request.GET.get('save_result'):
        data = []
        for exhibit in exhibits:
            data.append({
                'exhibit_id': exhibit.exhibit_id,
                'title': exhibit.title,
                'description': exhibit.description,
                'creation_date': exhibit.creation_date,
                'country': exhibit.country,
                'state': exhibit.state,
                'type': exhibit.type,
                'mission': exhibit.mission_id.title if exhibit.mission_id else None
            })
        return save_query_result(data, 'exhibits_filtered')

    # Подготавливаем данные для отображения
    exhibits_display = []
    for exhibit in exhibits:
        exhibits_display.append({
            'exhibit_id': exhibit.exhibit_id,
            'title': exhibit.title,
            'description': exhibit.description,
            'creation_date': exhibit.creation_date,
            'country': exhibit.country,
            'state': exhibit.state,
            'type': exhibit.type,
            'mission_title': exhibit.mission_id.title if exhibit.mission_id else None
        })

    columns = ['exhibit_id', 'title', 'description', 'creation_date', 'country', 'state', 'type', 'mission_id']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Экспонаты',
        'items': exhibits_display,
        'columns': columns,
        'entity_type': 'exhibit',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def exhibit_add(request):
    if request.method == 'POST':
        try:
            # Получаем максимальный ID
            max_id = Exhibit.objects.aggregate(models.Max('exhibit_id'))['exhibit_id__max']
            new_id = (max_id or 0) + 1

            # Преобразуем строку в дату
            creation_date = datetime.strptime(request.POST['creation_date'], '%Y-%m-%d').date()

            # Валидация
            if creation_date > date.today():
                messages.error(request, 'Дата создания не может быть в будущем!')
                return redirect('exhibit_add')

            exhibit = Exhibit(
                exhibit_id=new_id,
                title=request.POST['title'],
                description=request.POST['description'],
                creation_date=creation_date,
                country=request.POST['country'],
                state=request.POST['state'],
                type=request.POST['type']
            )

            mission_id_value = request.POST.get('mission_id', '').strip()
            if mission_id_value:
                try:
                    # Проверяем существование миссии
                    mission = SpaceMission.objects.get(mission_id=int(mission_id_value))
                    exhibit.mission_id = mission  # Присваиваем объект
                except (ValueError, SpaceMission.DoesNotExist):
                    messages.error(request, f'Миссия с ID {mission_id_value} не найдена!')
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
        {'name': 'mission_id', 'label': 'ID миссии (необязательно)', 'type': 'number', 'required': False},
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
        exhibit = get_object_or_404(Exhibit, exhibit_id=selected_id)

        if request.method == 'POST':
            try:
                exhibit.title = request.POST['title']
                exhibit.description = request.POST['description']

                # Преобразуем строку в дату
                creation_date = datetime.strptime(request.POST['creation_date'], '%Y-%m-%d').date()

                # Валидация
                if creation_date > date.today():
                    messages.error(request, 'Дата создания не может быть в будущем!')
                    return redirect(f'exhibit_update?id={selected_id}')

                exhibit.creation_date = creation_date
                exhibit.country = request.POST['country']
                exhibit.state = request.POST['state']
                exhibit.type = request.POST['type']

                mission_id_value = request.POST.get('mission_id', '').strip()
                if mission_id_value:
                    try:
                        mission = SpaceMission.objects.get(mission_id=int(mission_id_value))
                        exhibit.mission_id = mission
                    except (ValueError, SpaceMission.DoesNotExist):
                        messages.error(request, f'Миссия с ID {mission_id_value} не найдена!')
                        return redirect(f'exhibit_update?id={selected_id}')
                else:
                    exhibit.mission_id = None

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
            {'name': 'mission_id', 'label': 'ID миссии (необязательно)', 'type': 'number', 'required': False,
             'value': exhibit.mission_id.mission_id if exhibit.mission_id else ''},
        ]

        return render(request, 'core/entity_form_update.html', {
            'entity_name': 'Экспонат',
            'operation': 'Обновить',
            'fields': fields,
            'entity_type': 'exhibit'
        })

    columns = ['exhibit_id', 'title', 'country', 'type']
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
                exhibit = Exhibit.objects.get(exhibit_id=delete_id)
                exhibit.delete()
                messages.success(request, f'Экспонат "{exhibit.title}" успешно удален!')
            except Exhibit.DoesNotExist:
                messages.error(request, 'Экспонат не найден!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('exhibit_delete')

    exhibits = Exhibit.objects.all()
    columns = ['exhibit_id', 'title', 'country', 'type']

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
        if filter_column == 'crew':
            # Специальный фильтр для массива crew
            missions = missions.filter(crew__contains=[filter_value])
        else:
            filter_dict = {filter_column + '__icontains': filter_value}
            missions = missions.filter(**filter_dict)

    if request.GET.get('save_result'):
        # Преобразуем crew в строку для сохранения
        data = list(missions.values())
        for item in data:
            if 'crew' in item and item['crew']:
                item['crew'] = ', '.join(item['crew'])
        return save_query_result(data, 'missions_filtered')

    # Преобразуем crew в строку для отображения
    missions_display = []
    for mission in missions:
        mission_dict = {
            'mission_id': mission.mission_id,
            'title': mission.title,
            'country': mission.country,
            'start_date': mission.start_date,
            'end_date': mission.end_date,
            'crew': ', '.join(mission.crew) if mission.crew else '',
            'goal': mission.goal
        }
        missions_display.append(mission_dict)

    columns = ['mission_id', 'title', 'country', 'start_date', 'end_date', 'crew', 'goal']

    return render(request, 'core/entity_list.html', {
        'entity_name': 'Космические миссии',
        'items': missions_display,
        'columns': columns,
        'entity_type': 'mission',
        'filter_column': filter_column,
        'filter_value': filter_value
    })


def mission_add(request):
    if request.method == 'POST':
        try:
            # Получаем максимальный ID
            max_id = SpaceMission.objects.aggregate(models.Max('mission_id'))['mission_id__max']
            new_id = (max_id or 0) + 1

            # Преобразуем строки в даты
            start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()

            # Валидация
            if end_date < start_date:
                messages.error(request, 'Дата окончания не может быть раньше даты начала!')
                return redirect('mission_add')

            # Обработка экипажа - получаем массив
            crew_list = request.POST.getlist('crew[]')
            crew_list = [member.strip() for member in crew_list if member.strip()]  # Убираем пустые

            mission = SpaceMission(
                mission_id=new_id,
                title=request.POST['title'],
                country=request.POST['country'],
                start_date=start_date,
                end_date=end_date,
                crew=crew_list if crew_list else [],  # Передаем как массив Python
                goal=request.POST['goal']
            )

            mission.save()
            messages.success(request, 'Космическая миссия успешно добавлена!')
            return redirect('mission_list')
        except Exception as e:
            messages.error(request, f'Ошибка при добавлении: {str(e)}')

    return render(request, 'core/mission_form_add.html', {
        'entity_name': 'Космическая миссия',
        'operation': 'Добавить',
        'entity_type': 'mission'
    })


def mission_update(request):
    missions = SpaceMission.objects.all()
    selected_id = request.GET.get('id')

    if selected_id:
        mission = get_object_or_404(SpaceMission, mission_id=selected_id)

        if request.method == 'POST':
            try:
                mission.title = request.POST['title']
                mission.country = request.POST['country']

                # Преобразуем строки в даты
                start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
                end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()

                # Валидация
                if end_date < start_date:
                    messages.error(request, 'Дата окончания не может быть раньше даты начала!')
                    return redirect(f'mission_update?id={selected_id}')

                mission.start_date = start_date
                mission.end_date = end_date

                # Обработка экипажа
                crew_list = request.POST.getlist('crew[]')
                crew_list = [member.strip() for member in crew_list if member.strip()]
                mission.crew = crew_list if crew_list else []

                mission.goal = request.POST['goal']

                mission.save()
                messages.success(request, 'Космическая миссия успешно обновлена!')
                return redirect('mission_list')
            except Exception as e:
                messages.error(request, f'Ошибка при обновлении: {str(e)}')

        # Передаем текущий экипаж для отображения
        return render(request, 'core/mission_form_update.html', {
            'entity_name': 'Космическая миссия',
            'operation': 'Обновить',
            'entity_type': 'mission',
            'mission': mission,
            'crew_members': mission.crew if mission.crew else []
        })

    columns = ['mission_id', 'title', 'country', 'goal']
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
                mission = SpaceMission.objects.get(mission_id=delete_id)
                mission.delete()
                messages.success(request, f'Миссия "{mission.title}" успешно удалена!')
            except SpaceMission.DoesNotExist:
                messages.error(request, 'Миссия не найдена!')
            except Exception as e:
                messages.error(request, f'Ошибка при удалении: {str(e)}')
            return redirect('mission_delete')

    missions = SpaceMission.objects.all()
    columns = ['mission_id', 'title', 'country', 'goal']

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
        df.to_excel(writer, index=False, sheet_name=name[:31])

        worksheet = writer.sheets[name[:31]]
        for idx, col in enumerate(df.columns):
            max_length = max(
                df[col].astype(str).map(len).max() if not df.empty else 0,
                len(str(col))
            ) + 2
            worksheet.column_dimensions[openpyxl.utils.get_column_letter(idx + 1)].width = min(max_length, 50)

    return HttpResponse(f'Результат запроса сохранен в файл {filename}')


def save_database_state(request):
    """Страница выбора формата сохранения БД"""
    stats = {}

    with connection.cursor() as cursor:
        # Получаем статистику
        cursor.execute("""
            SELECT COUNT(*) 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        stats['total_tables'] = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name NOT LIKE 'auth_%'
            AND table_name NOT LIKE 'django_%'
        """)
        stats['user_tables'] = cursor.fetchone()[0]

        # Подсчет общего количества записей в пользовательских таблицах
        total_records = 0
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name NOT LIKE 'auth_%'
            AND table_name NOT LIKE 'django_%'
        """)

        for row in cursor.fetchall():
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {row[0]}")
                total_records += cursor.fetchone()[0]
            except:
                pass

        stats['total_records'] = total_records

        # Размер БД
        cursor.execute("""
            SELECT pg_size_pretty(pg_database_size(current_database()))
        """)
        stats['db_size'] = cursor.fetchone()[0]

    return render(request, 'core/save_database.html', stats)


def save_database_excel(request):
    """Сохранение БД в Excel формат"""
    if request.method != 'POST':
        return redirect('save_database_state')

    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'database_backup_{timestamp}.xlsx'
    filepath = os.path.join(backup_dir, filename)

    try:
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            tables_saved = []

            with connection.cursor() as cursor:
                # Получаем список пользовательских таблиц
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name NOT LIKE 'auth_%'
                    AND table_name NOT LIKE 'django_%'
                    ORDER BY table_name
                """)

                user_tables = [row[0] for row in cursor.fetchall()]

                # Сохраняем каждую таблицу
                for table_name in user_tables:
                    try:
                        # Получаем данные из таблицы
                        cursor.execute(f"SELECT * FROM {table_name}")
                        columns = [desc[0] for desc in cursor.description]
                        data = cursor.fetchall()

                        if data:
                            df = pd.DataFrame(data, columns=columns)

                            # Обработка специальных типов данных
                            for col in df.columns:
                                # Преобразуем списки/массивы в строки
                                if df[col].dtype == 'object':
                                    df[col] = df[col].apply(lambda x:
                                                            ', '.join(x) if isinstance(x, list) else x
                                                            )

                            # Сохраняем на отдельный лист (максимум 31 символ для имени листа)
                            sheet_name = table_name[:31]
                            df.to_excel(writer, sheet_name=sheet_name, index=False)

                            # Настройка ширины колонок
                            worksheet = writer.sheets[sheet_name]
                            for idx, col in enumerate(df.columns):
                                max_length = max(
                                    df[col].astype(str).map(len).max() if not df.empty else 0,
                                    len(str(col))
                                ) + 2
                                worksheet.column_dimensions[
                                    openpyxl.utils.get_column_letter(idx + 1)
                                ].width = min(max_length, 50)

                            tables_saved.append(table_name)
                        else:
                            # Если таблица пустая, создаем лист с заголовками
                            df = pd.DataFrame(columns=columns)
                            sheet_name = table_name[:31]
                            df.to_excel(writer, sheet_name=sheet_name, index=False)
                            tables_saved.append(f"{table_name} (пустая)")

                    except Exception as e:
                        print(f"Ошибка при сохранении таблицы {table_name}: {e}")

            # Добавляем информационный лист
            info_data = {
                'Информация': ['Дата создания', 'Количество таблиц', 'Сохраненные таблицы'],
                'Значение': [
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    len(tables_saved),
                    ', '.join(tables_saved)
                ]
            }
            info_df = pd.DataFrame(info_data)
            info_df.to_excel(writer, sheet_name='INFO', index=False)

        # Отправляем файл пользователю
        with open(filepath, 'rb') as file:
            response = HttpResponse(
                file.read(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response

    except Exception as e:
        messages.error(request, f'Ошибка при создании Excel файла: {str(e)}')
        return redirect('save_database_state')


def save_database_sql(request):
    """Сохранение БД в SQL формат"""
    if request.method != 'POST':
        return redirect('save_database_state')

    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'database_dump_{timestamp}.sql'
    filepath = os.path.join(backup_dir, filename)

    try:
        with open(filepath, 'w', encoding='utf-8') as sql_file:
            # Заголовок файла
            sql_file.write("-- Space Museum Database Dump\n")
            sql_file.write(f"-- Generated: {datetime.now()}\n")
            sql_file.write("-- Database: PostgreSQL\n\n")
            sql_file.write("SET client_encoding = 'UTF8';\n\n")

            with connection.cursor() as cursor:
                # Получаем список пользовательских таблиц
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name NOT LIKE 'auth_%'
                    AND table_name NOT LIKE 'django_%'
                    ORDER BY table_name
                """)

                user_tables = [row[0] for row in cursor.fetchall()]

                for table_name in user_tables:
                    sql_file.write(f"\n-- Table: {table_name}\n")
                    sql_file.write(f"-- DROP TABLE IF EXISTS {table_name} CASCADE;\n\n")

                    # Получаем структуру таблицы
                    sql_file.write(f"CREATE TABLE IF NOT EXISTS {table_name} (\n")

                    cursor.execute("""
                        SELECT 
                            column_name,
                            data_type,
                            character_maximum_length,
                            is_nullable,
                            column_default
                        FROM information_schema.columns
                        WHERE table_name = %s
                        ORDER BY ordinal_position
                    """, [table_name])

                    columns = cursor.fetchall()
                    column_definitions = []

                    for col in columns:
                        col_def = f"    {col[0]} "

                        # Тип данных
                        if col[1] == 'character varying' and col[2]:
                            col_def += f"VARCHAR({col[2]})"
                        elif col[1] == 'integer':
                            col_def += "INTEGER"
                        elif col[1] == 'bigint':
                            col_def += "BIGINT"
                        elif col[1] == 'text':
                            col_def += "TEXT"
                        elif col[1] == 'date':
                            col_def += "DATE"
                        elif col[1] == 'timestamp without time zone':
                            col_def += "TIMESTAMP"
                        elif col[1] == 'boolean':
                            col_def += "BOOLEAN"
                        elif col[1] == 'ARRAY':
                            col_def += "TEXT[]"
                        else:
                            col_def += col[1].upper()

                        # NOT NULL
                        if col[3] == 'NO':
                            col_def += " NOT NULL"

                        # DEFAULT
                        if col[4]:
                            col_def += f" DEFAULT {col[4]}"

                        column_definitions.append(col_def)

                    # Получаем PRIMARY KEY
                    cursor.execute("""
                        SELECT kcu.column_name
                        FROM information_schema.table_constraints tc
                        JOIN information_schema.key_column_usage kcu
                            ON tc.constraint_name = kcu.constraint_name
                        WHERE tc.table_name = %s 
                        AND tc.constraint_type = 'PRIMARY KEY'
                    """, [table_name])

                    pk_columns = [row[0] for row in cursor.fetchall()]
                    if pk_columns:
                        column_definitions.append(
                            f"    PRIMARY KEY ({', '.join(pk_columns)})"
                        )

                    # Получаем FOREIGN KEYS
                    cursor.execute("""
                        SELECT
                            kcu.column_name,
                            ccu.table_name AS foreign_table_name,
                            ccu.column_name AS foreign_column_name,
                            rc.delete_rule
                        FROM information_schema.table_constraints AS tc
                        JOIN information_schema.key_column_usage AS kcu
                            ON tc.constraint_name = kcu.constraint_name
                        JOIN information_schema.constraint_column_usage AS ccu
                            ON ccu.constraint_name = tc.constraint_name
                        JOIN information_schema.referential_constraints rc
                            ON tc.constraint_name = rc.constraint_name
                        WHERE tc.constraint_type = 'FOREIGN KEY' 
                        AND tc.table_name = %s
                    """, [table_name])

                    for fk in cursor.fetchall():
                        fk_def = f"    FOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[2]})"
                        if fk[3]:
                            fk_def += f" ON DELETE {fk[3]}"
                        column_definitions.append(fk_def)

                    sql_file.write(',\n'.join(column_definitions))
                    sql_file.write("\n);\n\n")

                    # Получаем данные таблицы
                    cursor.execute(f"SELECT * FROM {table_name}")
                    rows = cursor.fetchall()

                    if rows:
                        columns = [desc[0] for desc in cursor.description]
                        sql_file.write(f"-- Data for {table_name}\n")

                        for row in rows:
                            values = []
                            for val in row:
                                if val is None:
                                    values.append("NULL")
                                elif isinstance(val, bool):
                                    values.append("TRUE" if val else "FALSE")
                                elif isinstance(val, (int, float)):
                                    values.append(str(val))
                                elif isinstance(val, list):
                                    # PostgreSQL array format
                                    array_vals = [f"'{v}'" for v in val]
                                    values.append("ARRAY[" + ", ".join(array_vals) + "]")
                                elif isinstance(val, (date, datetime)):
                                    values.append(f"'{val}'")
                                else:
                                    # Экранируем одинарные кавычки
                                    escaped_val = str(val).replace("'", "''")
                                    values.append(f"'{escaped_val}'")

                            insert_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});\n"
                            sql_file.write(insert_sql)

                        sql_file.write("\n")

                # Добавляем команды для последовательностей (sequences)
                sql_file.write("\n-- Reset sequences\n")
                for table_name in user_tables:
                    cursor.execute("""
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_name = %s
                        AND column_default LIKE 'nextval%%'
                    """, [table_name])

                    for col in cursor.fetchall():
                        sql_file.write(
                            f"SELECT setval(pg_get_serial_sequence('{table_name}', '{col[0]}'), "
                            f"COALESCE((SELECT MAX({col[0]}) FROM {table_name}), 1));\n"
                        )

        # Отправляем файл пользователю
        with open(filepath, 'rb') as file:
            response = HttpResponse(
                file.read(),
                content_type='application/sql'
            )
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response

    except Exception as e:
        messages.error(request, f'Ошибка при создании SQL дампа: {str(e)}')
        return redirect('save_database_state')

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

    # Запросы для Лабораторной работы 6
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


def table_management(request):
    """Главная страница управления таблицами"""
    return render(request, 'core/table_management.html')


def table_add(request):
    """Создание новой таблицы"""
    if request.method == 'POST':
        try:
            table_name = request.POST.get('table_name')

            # Валидация имени таблицы
            if not table_name or not table_name.replace('_', '').isalnum():
                raise ValueError("Некорректное имя таблицы")

            # Построение SQL запроса
            sql_parts = [f"CREATE TABLE {table_name} ("]
            columns = []
            primary_keys = []

            # Обработка колонок
            for key in request.POST:
                if key.startswith('column_name_'):
                    idx = key.split('_')[-1]
                    col_name = request.POST.get(f'column_name_{idx}')
                    col_type = request.POST.get(f'column_type_{idx}')

                    if col_name and col_type:
                        col_def = f"{col_name} {col_type}"

                        # Проверка ограничений
                        if request.POST.get(f'column_primary_{idx}'):
                            primary_keys.append(col_name)

                        if request.POST.get(f'column_notnull_{idx}'):
                            col_def += " NOT NULL"

                        if request.POST.get(f'column_unique_{idx}'):
                            col_def += " UNIQUE"

                        default_val = request.POST.get(f'column_default_{idx}')
                        if default_val and default_val != 'NULL':
                            col_def += f" DEFAULT {default_val}"

                        columns.append(col_def)

            # Добавление primary key
            if primary_keys:
                columns.append(f"PRIMARY KEY ({', '.join(primary_keys)})")

            # Обработка foreign keys
            for key in request.POST:
                if key.startswith('fk_column_'):
                    idx = key.split('_')[-1]
                    fk_column = request.POST.get(f'fk_column_{idx}')
                    fk_ref_table = request.POST.get(f'fk_ref_table_{idx}')
                    fk_ref_column = request.POST.get(f'fk_ref_column_{idx}')
                    fk_on_delete = request.POST.get(f'fk_on_delete_{idx}', 'CASCADE')

                    if fk_column and fk_ref_table and fk_ref_column:
                        fk_def = f"FOREIGN KEY ({fk_column}) REFERENCES {fk_ref_table}({fk_ref_column}) ON DELETE {fk_on_delete}"
                        columns.append(fk_def)

            sql_parts.append(', '.join(columns))
            sql_parts.append(')')

            create_sql = ' '.join(sql_parts)

            # Выполнение SQL
            with connection.cursor() as cursor:
                cursor.execute(create_sql)

            messages.success(request, f'Таблица "{table_name}" успешно создана!')
            return redirect('table_management')

        except Exception as e:
            messages.error(request, f'Ошибка при создании таблицы: {str(e)}')

    # Получение списка существующих таблиц
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name
        """)
        existing_tables = [row[0] for row in cursor.fetchall()]

    return render(request, 'core/table_add.html', {
        'existing_tables': json.dumps(existing_tables)
    })


def table_list(request):
    """Список таблиц для удаления"""
    if request.method == 'POST':
        table_name = request.POST.get('table_name')
        try:
            # Проверка защищенных таблиц
            protected_tables = ['auth_user', 'auth_group', 'django_migrations', 'django_content_type']
            if table_name in protected_tables:
                raise ValueError("Эта таблица защищена от удаления")

            with connection.cursor() as cursor:
                cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")

            messages.success(request, f'Таблица "{table_name}" успешно удалена!')

        except Exception as e:
            messages.error(request, f'Ошибка при удалении таблицы: {str(e)}')

        return redirect('table_list')

    # Получение информации о таблицах
    tables = []
    with connection.cursor() as cursor:
        # Получаем все таблицы
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name NOT LIKE 'django_%'
            AND table_name NOT LIKE 'auth_%'
            ORDER BY table_name
        """)

        for row in cursor.fetchall():
            table_name = row[0]

            # Получаем количество записей
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                row_count = cursor.fetchone()[0]
            except:
                row_count = 0

            # Получаем зависимости
            cursor.execute("""
                SELECT DISTINCT
                    tc.table_name AS referencing_table
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                WHERE tc.constraint_type = 'FOREIGN KEY'
                    AND ccu.table_name = %s
            """, [table_name])

            dependencies = [dep[0] for dep in cursor.fetchall()]

            tables.append({
                'name': table_name,
                'row_count': row_count,
                'dependencies': dependencies,
                'has_dependencies': len(dependencies) > 0
            })

    return render(request, 'core/table_list.html', {'tables': tables})


def table_info(request):
    """Информация о структуре БД (только пользовательские таблицы)"""
    tables_info = []

    with connection.cursor() as cursor:
        # Получаем только пользовательские таблицы
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name NOT LIKE 'auth_%'
            AND table_name NOT LIKE 'django_%'
            ORDER BY table_name
        """)

        for row in cursor.fetchall():
            table_name = row[0]
            table_data = {'name': table_name, 'columns': [], 'foreign_keys': []}

            # Получаем количество записей
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                table_data['row_count'] = cursor.fetchone()[0]
            except:
                table_data['row_count'] = 0

            # Получаем информацию о колонках
            cursor.execute("""
                SELECT 
                    column_name,
                    data_type,
                    is_nullable,
                    column_default,
                    character_maximum_length
                FROM information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, [table_name])

            for col in cursor.fetchall():
                col_info = {
                    'name': col[0],
                    'type': col[1],
                    'null': col[2] == 'YES',
                    'default': col[3],
                    'key': ''
                }

                # Определяем тип ключа
                cursor.execute("""
                    SELECT constraint_type
                    FROM information_schema.key_column_usage kcu
                    JOIN information_schema.table_constraints tc
                        ON kcu.constraint_name = tc.constraint_name
                    WHERE kcu.table_name = %s AND kcu.column_name = %s
                """, [table_name, col[0]])

                key_result = cursor.fetchone()
                if key_result:
                    if 'PRIMARY' in key_result[0]:
                        col_info['key'] = 'PRI'
                    elif 'FOREIGN' in key_result[0]:
                        col_info['key'] = 'MUL'

                table_data['columns'].append(col_info)

            # Получаем foreign keys
            cursor.execute("""
                SELECT
                    kcu.column_name,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name = %s
            """, [table_name])

            for fk in cursor.fetchall():
                table_data['foreign_keys'].append({
                    'column': fk[0],
                    'ref_table': fk[1],
                    'ref_column': fk[2]
                })

            tables_info.append(table_data)

    return render(request, 'core/table_info.html', {'tables_info': tables_info})


def get_table_columns(request):
    """AJAX endpoint для получения колонок таблицы"""
    table_name = request.GET.get('table')
    columns = []

    if table_name:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, [table_name])

            columns = [row[0] for row in cursor.fetchall()]

    return JsonResponse({'columns': columns})