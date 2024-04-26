from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('create_recommendation/', views.CreateRecommendation, name='create_recommendation'),
    path('my_recipes/', views.recipes_page, name='my_recipes'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]