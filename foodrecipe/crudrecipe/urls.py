from django.urls import path
from .import views


app_name = "crudrecipe"
urlpatterns = [
  
    path('recipe/', views.recipe_list,name='recipe_list'),
    path('recipe/upload/', views.upload_recipe,name='upload_recipe'),
    path('recipe/<int:pk>/', views.delete_recipe, name="delete_recipe"),
    path("api/",views.api_data, name="api_data"),
    path("change/<int:pk>/",views.update_api_data,name="update_api_data"),

]


