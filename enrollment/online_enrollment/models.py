from django.db import models


class Account(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.email}'

class Student(models.Model):
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    student_id = models.IntegerField()
    ave_grade = models.IntegerField()
   
    def __str__(self):
        return f'{self.name}'

class School(models.Model):
    program = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    prof = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    ave_grade = models.IntegerField()

    def __str__(self):
        return f'{self.program}'

class Stud_fam(models.Model):
    guardian = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    annual_inc = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.guardian}'

class Address(models.Model):
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    brgy = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal = models.IntegerField()
    def __str__(self):
        return f'{self.province}'

    

    