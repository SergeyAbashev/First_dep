from timeit import default_timer

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# Create your views here.


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'timer': default_timer()
        }
        return render(request, 'shop-index.html', context=context)


class ProductListView(ListView):
    pass