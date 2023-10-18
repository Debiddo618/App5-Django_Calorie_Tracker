from django.shortcuts import render, redirect
from .models import Food,Consume

# Create your views here.
def index(request):
    if request.method == "POST":
        # This returns just the string name
        food_consumed = request.POST.get("food_consumed")
        # This search for the food object
        consume=Food.objects.get(name=food_consumed)
        # get the current user
        user=request.user
        # create the consume list
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
    foods = Food.objects.all()
    consumed_food=Consume.objects.filter(user=request.user)
    return render(request,"calorie_tracker/index.html",{"foods":foods,"consumed_food":consumed_food})

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect("/")
    return render(request,"calorie_tracker/delete.html")

