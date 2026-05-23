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
#intern login 
from .models import Intern




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
    
    #intern data 
@api_view(['POST'])
def intern_login(request):

    email = request.data.get("email")
    password = request.data.get("password")

    try:

        intern = Intern.objects.get(
            email=email,
            password=password
        )

        return Response({

            "message": "Login successful",

            "intern": {
                "id": intern.id,
                "name": intern.name,
                "email": intern.email,
                "college_name": intern.college_name,
                "course": intern.course,
                "internship_field": intern.internship_field,
                "duration": intern.duration,
                "start_date": intern.start_date,
                "end_date": intern.end_date,
            }

        })

    except Intern.DoesNotExist:

        return Response({
            "error": "Invalid email or password"
        }, status=401)