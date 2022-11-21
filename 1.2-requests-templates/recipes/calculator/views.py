from django.shortcuts import render, reverse, HttpResponse
import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):
    recipes = []
    for recipe in DATA.keys():
        recipes.append(recipe)
    context = {'recipes': recipes}
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    return render(request, 'calculator/index.html', context)

def recipe_view(request, param_recipe):
    servings = int(request.GET.get('servings', 1))
    recipe = copy.deepcopy(DATA.get(param_recipe))
    if servings > 1:
        for key, val in recipe.items():
            recipe[key] = val * servings  
    context = {'recipe': recipe}
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    return render(request, 'calculator/recipe_view.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
