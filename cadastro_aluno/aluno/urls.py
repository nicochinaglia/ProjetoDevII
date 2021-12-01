from django.urls import path

from . import views

urlpatterns = [
    path('', views.AlunoList.as_view(), name='aluno_list'),
    path('view/<int:pk>', views.AlunoView.as_view(), name='aluno_view'),
    path('new', views.AlunoCreate.as_view(), name='aluno_new'),
    path('view/<int:pk>', views.AlunoView.as_view(), name='aluno_view'),
    path('edit/<int:pk>', views.AlunoUpdate.as_view(), name='aluno_edit'),
    path('delete/<int:pk>', views.AlunoDelete.as_view(), name='aluno_delete'),
]