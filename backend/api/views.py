from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Application
from .serializers import ApplicationSerializer
#admin pannel 
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


#admin pannel 

@api_view(['POST'])
def admin_login(request):

    username = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None and user.is_staff:

        refresh = RefreshToken.for_user(user)

        return Response({
            "token": str(refresh.access_token),
            "message": "Login Success"
        })

    return Response({
        "error": "Invalid Credentials"
    }, status=401)