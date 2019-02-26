from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:employee_id>/', views.detailEmployee, name='detailEmployee'), 
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
]