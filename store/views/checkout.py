from django.views import View
from django.shortcuts import render, redirect


class Checkout(View):
    def get(self, request):
        return render(request, 'checkout.html')