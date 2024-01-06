from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_page, name='items_page'),  # Hier kannst du eine URL für deine leere Seite definieren
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('create/', views.item_create, name='item_create'),
    path('category/', views.items_category, name='items_category'),
    path('category/<int:category_id>/', views.category_contains, name='category_contains'),
    path('test/', views.test, name='test'),

]