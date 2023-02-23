from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from products.models import Products, Category


# Create your views here.

def category_for_all(request):
    categories = Category.objects.all()
    return {'categories': categories}


class CategoryView(View):
    def get(self, request, category_name):
        category = Category.objects.filter(name=category_name)
        products = Products.objects.filter(category=category)
        return render(request, "category.html", {"category": category, 'products': products})


class IndexView(View):
    def get(self, request):
        products = Products.objects.all()
        return render(request, "index.html", {'products': products})


