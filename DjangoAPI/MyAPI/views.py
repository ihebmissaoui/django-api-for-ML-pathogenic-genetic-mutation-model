from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import pathogenics
from .serializers import pathogenicSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

class PathogenicView(viewsets.ModelViewSet):
    queryset = pathogenics.objects.all()
    serializer_class = pathogenicSerializers

@api_view(["POST"])
def predictPathogenic(request):
    try:

        return JsonResponse({"prediction" :"Pathogenic"})

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)