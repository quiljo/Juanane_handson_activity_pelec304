from django.urls import path
from . import views


urlpatterns = [
    path ('account/', views.account_view, name="student_acc"),
    path('stud_fam/', views.studfam_view, name="stud_fam"),
    path('school/', views.school_view, name="school"),
    path('student/', views.student_view, name="student"),
    path('address/', views.address_view, name="address"),
    path('success/', views.success, name = 'success'),
    # ACCOUNT
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name="logout_user"),
    path('dashboard/', views.dashboard, name='dashboard'),
]