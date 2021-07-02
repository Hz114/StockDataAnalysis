from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View

# Create your views here.
def main(request):
    return render(request, 'main.html')
