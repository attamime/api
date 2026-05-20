from django.urls import path, include
from . import views
from . views import studentListView,creat,edit_stu,delete_stud

urlpatterns = [
    path('', studentListView.as_view(), name='home'),
    path('add/', creat.as_view(), name='add'),
    path('edit/<int:pk>/',edit_stu.as_view(), name='edit'),
    path('api/', views.studentlistcreate.as_view(), name='api-student-list-create'),
    path('delete/<int:pk>/',delete_stud.as_view(), name='delete'),
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
]