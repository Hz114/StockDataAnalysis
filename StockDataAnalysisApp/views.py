from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View


class ResultAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = request.session.get('result')
        return Response(data)

# Create your views here.
def main(request):
    return render(request, 'main.html')
