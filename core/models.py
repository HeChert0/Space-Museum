# core/models.py
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Visitor(models.Model):
    visitor_id = models.AutoField(primary_key=True, db_column='visitor_id')
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    citizenship = models.CharField(max_length=100)
    ticket_type = models.CharField(max_length=50)
    visit_date = models.DateField()
    review = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'visitor'
        managed = False  # Не даем Django менять структуру существующей БД

    def str(self):
        return self.full_name


class SpaceMission(models.Model):
    mission_id = models.AutoField(primary_key=True, db_column='mission_id')
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    crew = ArrayField(models.CharField(max_length=255), blank=True, null=True, default=list)
    goal = models.CharField(max_length=200)

    class Meta:
        db_table = 'space_mission'
        managed = False

    def str(self):
        return self.title


class Exhibition(models.Model):
    exhibition_id = models.AutoField(primary_key=True, db_column='exhibition_id')
    title = models.CharField(max_length=255)
    theme = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    class Meta:
        db_table = 'exhibition'
        managed = False

    def str(self):
        return self.title


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True, db_column='employee_id')
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    qualification = models.CharField(max_length=100)

    class Meta:
        db_table = 'employee'
        managed = False

    def str(self):
        return self.full_name


class Exhibit(models.Model):
    exhibit_id = models.AutoField(primary_key=True, db_column='exhibit_id')
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    mission_id = models.ForeignKey(SpaceMission, on_delete=models.SET_NULL, null=True, blank=True,
                                   db_column='mission_id', related_name='exhibits')

    class Meta:
        db_table = 'exhibit'
        managed = False

    def str(self):
        return self.title


class Excursion(models.Model):
    excursion_id = models.AutoField(primary_key=True, db_column='excursion_id')
    title = models.CharField(max_length=255)
    date = models.DateField()
    language = models.CharField(max_length=50)
    ticket_num = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, db_column='employee_id')

    class Meta:
        db_table = 'excursion'
        managed = False

    def str(self):
        return self.title

# В models.py - исправленные модели связующих таблиц
class ExcursionVisitor(models.Model):
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, db_column='excursion_id')
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, db_column='visitor_id')

    class Meta:
        db_table = 'excursion_visitor'
        managed = False
        unique_together = (('excursion', 'visitor'),)

class ExhibitionEmployee(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, db_column='exhibition_id')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='employee_id')

    class Meta:
        db_table = 'exhibition_employee'
        managed = False
        unique_together = (('exhibition', 'employee'),)


class ExhibitionExcursion(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'exhibition_excursion'
        unique_together = ('exhibition', 'excursion')


class ExhibitionExhibit(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)

    class Meta:
        db_table = 'exhibition_exhibit'
        unique_together = ('exhibition', 'exhibit')