
from django.shortcuts import render

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
def recept(request, name_recipe):
    recipe = name_recipe
    servings = int(request.GET.get('serving', 1))
    if servings == 1:
        context = {
            'recipe': DATA[f'{recipe}']
        }
        return render(request, 'calculator/index.html', context)
    else:
        for key, values in DATA[f'{recipe}'].items():
            DATA[f'{recipe}'][key] = values * servings
        context = {'recipe': DATA[f'{recipe}']
        }
    return render(request, 'calculator/index.html', context)





