from django.views import View
from django.shortcuts import render,redirect

class Index(View):
    def get(self,request):

        return render(request,'index.html')