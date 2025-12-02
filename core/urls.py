# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('entities/', views.entities_menu, name='entities_menu'),

    # Visitor URLs
    path('visitors/', views.visitor_list, name='visitor_list'),
    path('visitors/add/', views.visitor_add, name='visitor_add'),
    path('visitors/update/', views.visitor_update, name='visitor_update'),
    path('visitors/delete/', views.visitor_delete, name='visitor_delete'),

    # Employee URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employees/update/', views.employee_update, name='employee_update'),
    path('employees/delete/', views.employee_delete, name='employee_delete'),

    # Exhibition URLs
    path('exhibitions/', views.exhibition_list, name='exhibition_list'),
    path('exhibitions/add/', views.exhibition_add, name='exhibition_add'),
    path('exhibitions/update/', views.exhibition_update, name='exhibition_update'),
    path('exhibitions/delete/', views.exhibition_delete, name='exhibition_delete'),

    # Excursion URLs
    path('excursions/', views.excursion_list, name='excursion_list'),
    path('excursions/add/', views.excursion_add, name='excursion_add'),
    path('excursions/update/', views.excursion_update, name='excursion_update'),
    path('excursions/delete/', views.excursion_delete, name='excursion_delete'),

    # Exhibit URLs
    path('exhibits/', views.exhibit_list, name='exhibit_list'),
    path('exhibits/add/', views.exhibit_add, name='exhibit_add'),
    path('exhibits/update/', views.exhibit_update, name='exhibit_update'),
    path('exhibits/delete/', views.exhibit_delete, name='exhibit_delete'),

    # Mission URLs
    path('missions/', views.mission_list, name='mission_list'),
    path('missions/add/', views.mission_add, name='mission_add'),
    path('missions/update/', views.mission_update, name='mission_update'),
    path('missions/delete/', views.mission_delete, name='mission_delete'),

    # Special queries and backup
    path('special-queries/', views.special_queries, name='special_queries'),
    # Замените старый URL для save_database_state на эти:
    path('save-database/', views.save_database_state, name='save_database_state'),
    path('save-database/excel/', views.save_database_excel, name='save_database_excel'),
    path('save-database/sql/', views.save_database_sql, name='save_database_sql'),

    # Table management URLs
    path('table-management/', views.table_management, name='table_management'),
    path('table-add/', views.table_add, name='table_add'),
    path('table-list/', views.table_list, name='table_list'),
    path('table-info/', views.table_info, name='table_info'),
    path('get-table-columns/', views.get_table_columns, name='get_table_columns'),

]