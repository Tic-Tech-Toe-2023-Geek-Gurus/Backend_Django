#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
# Create your views here.

def register_page(request):
    try:
        data=request.data
        serializer=reg_ser(data=data['username'])
        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.error,'message':'Something Went Wrong'})
        
        #function for model training
        return Response({'status':200,'message':'Registration Successful'})
    except Exception as e:
        print(e)

def login_page(request):
    data=request.data
    serializer=log_ser(data=data['username'])
    if not serializer.is_valid():
        return Response({'status':403,'error':serializer.error,'payload':''})
    
    #predict the user
    # if predict==1:
    #     return Response({'status':200,'message':'Valid','payload':data['username']})
    # else:
    #     return Response({'status':403,'message':'Invalid','payload':''})