from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Maktab, Oquvchi, Oqituvchi, Gurux
from .serializers import MaktabSerializer, OquvchiSerializer,OqituvchiSerializer, GuruxSerializer

# Create your views here.


