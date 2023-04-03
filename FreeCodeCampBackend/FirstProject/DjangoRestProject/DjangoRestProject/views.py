from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_app.serializers import StudentSerializer
from rest_app.models import Student


class TestView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # for simplicity we are using dict as a data set
        # normally data will be et from database

        query_set = Student.objects.all()
        serializer = StudentSerializer(query_set, many=True)

        data = {
            "username": "admin",
            "years_active": 10
        }
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

