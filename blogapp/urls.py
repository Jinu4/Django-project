from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun, name='fun'),
    path('post/', views.post, name='post'),
    path('update/<int:id>', views.update, name='update'),
    path('single/<int:id>', views.single, name='single'),
    path('delete/<int:id>', views.delete, name='delete')
]
