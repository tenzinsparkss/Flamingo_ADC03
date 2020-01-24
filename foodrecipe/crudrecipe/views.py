from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Cookbook
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def upload_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crudrecipe:recipe_list')
    return render(request, "crudrecipe/upload_recipe.html", {"form":form})

def recipe_list(request):
    recipe =  Cookbook.objects.all()
    if request.GET:
        query = request.GET['q']
        recipe = get_data_queryset(str(query))
    return render(request, 'crudrecipe/recipe_list.html', {'recipes':recipe})

def delete_recipe(request, pk):
    recipe = Cookbook.objects.get(pk = pk)
    recipe.delete()
    return redirect('crudrecipe:recipe_list')

def get_data_queryset(query=None):
    queryset=[]
    queries= query.split(" ")
    for q in queries:
        recipes= Cookbook.objects.filter(
               Q(name__icontains=q) |
               Q(title__icontains=q)
            )
            

        for recipe in recipes:
            queryset.append(recipe)

    return list(set(queryset))

def api_data(request):
    recipe = Cookbook.objects.all()
    if request.method == "GET":
        dict_type = {"recipes": list(recipe.values("title", "username"))}
        return JsonResponse(dict_type)

@csrf_exempt
def update_api_data(request, pk):
    recipe = Cookbook.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"name":recipe.name, "title": recipe.title})

    else:
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        recipe.title = update_data['title']
        recipe.name = update_data['username']
        recipe.save()

        return JsonResponse({"message": "Successfully completed!!"})



# Create your views here.
