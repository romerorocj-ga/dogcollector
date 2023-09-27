from django.shortcuts import render

dogs = [
    {"name": "Ace", "breed": "PitBull", "description": "Big Baby", "age": 7},
    {"name": "Rocket", "breed": "Corgi", "description": "Little Fur Ball", "age": 1},
    {
        "name": "Mookie",
        "breed": "French Bulldog",
        "description": "Loves to Bark",
        "age": 4,
    },
]


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def dogs_index(request):
    return render(request, "dogs/index.html", {"dogs": dogs})
