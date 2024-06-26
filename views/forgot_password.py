from django.views import View
from django.shortcuts import render, redirect


class (View):
    def get(self, request):
        return render(request, 'blog-detail.html')