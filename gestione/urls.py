from django.urls import path

from . import views

hahdler404 = 'assoc.views.handler404'
hahdler500 = 'assoc.views.handler500'


app_name = 'gestione'
urlpatterns = [


    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    # URl Members
    path('members/', views.list_members, name='members'),
    path('add_member/', views.add_member, name='add_member'),
    path('update_member/<int:pk>', views.update_member, name='update_member'),
    path('members/<int:pk>/', views.member_record, name='record'),
    path('delete_member/<int:pk>/', views.delete_member, name='delete_member'),

    # URL Departments
    path('departments/', views.list_departments, name='departments'),
    path('departments/<int:pk>/', views.department_record, name='department_record'),
    path('add_department/', views.add_department, name='add_department'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),
    path('update_department/<int:pk>/', views.update_department, name='update_department'),


    # URl Cities
    path('cities/', views.list_cities, name='cities'),
    path('cities/<int:pk>/', views.city_record, name='city_record'),
    path('add_city/', views.add_city, name='add_city'),
    path('delete_city/<int:pk>/', views.delete_city, name='delete_city'),
    path('update_city/<int:pk>/', views.update_city, name='update_city'),



    # URl Districts
    path('districts/', views.list_districts, name='districts'),
    path('districts/<int:pk>/', views.district_record, name='district_record'),
    path('add_district/', views.add_district, name='add_district'),
    path('member_record_by_district/<int:pk>/', views.member_record_by_district, name='member_record_by_district'),
    path('delete_district/<int:pk>/', views.delete_district, name='delete_district'),
    path('update_district/<int:pk>/', views.update_district, name='update_district'),


    # URL Settings
    path('settings/', views.settings, name='settings'),


]