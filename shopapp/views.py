from timeit import default_timer

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
# Create your views here.


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'timer': default_timer()
        }
        return render(request, 'shop-index.html', context=context)
