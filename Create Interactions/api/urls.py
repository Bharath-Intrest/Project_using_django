from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_pg,name='login_pg'),
    path('<int:lst_id>/',views.home1,name='home'),
    path('<str:dyn>/student/',views.student,name='student'),
    path('<str:dynamic>/course_details/',views.course_details,name='course_details'),
    path('<str:dyn3>/course_details/course/',views.course_pg,name='course_pg'),
]
