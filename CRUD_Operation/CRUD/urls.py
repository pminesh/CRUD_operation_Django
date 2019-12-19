from django.urls import path , include
from CRUD import views
urlpatterns = [
    path('',views.index,name='index'),
    path('show/',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
]