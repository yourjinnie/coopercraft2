from django.views import View
from django.shortcuts import render, redirect


class Cart(View):
    def get(self, request):
        return render(request, 'cart.html')