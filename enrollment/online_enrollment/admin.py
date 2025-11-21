from django.contrib import admin
from .models import Account, Student, School, Stud_fam, Address

@admin.register(Account)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

@admin.register(Student)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'program')


@admin.register(School)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('program', 'subject')


@admin.register(Stud_fam)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('guardian', 'occupation')


@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('province', 'municipality')




