from django.contrib import admin  
from django.urls import path  
from cardapio import views  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', views.index),  
    path('addnew',views.addnew),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  
</int:id></int:id></int:id>