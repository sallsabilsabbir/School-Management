from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import schoolInfo
from .serializers import schoolInfoSerializer

# Create your views here.


@api_view(["GET", "POST","PUT","DELETE"])
def schoolInfo_create(request, pk=None):

    if request.method == "GET":
        id = pk
        if id is not None:
            try:
                schInfo = schoolInfo.objects.get(id=id)
                serializer = schoolInfoSerializer(schInfo)
                return Response(serializer.data)
            except schoolInfo.DoesNotExist:
                return Response([], status=status.HTTP_200_OK)

        schInfo = schoolInfo.objects.all()
        serializer = schoolInfoSerializer(schInfo, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = schoolInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Insert Successfully"})
        return Response(serializer.errors)

    if request.method == "PUT":
        id = pk
        schInfo = schoolInfo.objects.get(pk = id)
        serializer = schoolInfoSerializer(schInfo, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Update Data Successfully"})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        id = pk
        schInfo = schoolInfo.objects.get(pk = id)
        schInfo.delete()
        return Response({"msg":"Delete Successfully"})