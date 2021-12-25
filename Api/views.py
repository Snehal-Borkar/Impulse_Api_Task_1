from django.shortcuts import render
from .models import Sample_Details
from .serializers import Sample_Details_Serializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.views import APIView

class Data(APIView):
    @csrf_exempt
    def get(self, request, format=None):
        details = Sample_Details.objects.all()
        serializer = Sample_Details_Serializer(details, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        serializer = Sample_Details_Serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)