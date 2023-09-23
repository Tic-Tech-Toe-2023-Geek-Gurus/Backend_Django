from rest_framework import serializers
from .models import *

class reg_ser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

    def validate(self,data):
        username=data['username']
        if User.objects.filter(username=username).count>0:
            raise serializers.ValidationError('Username Already Exist')
        
class log_ser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

    def validate(self,data):
        username=data['username']
        user=User.objects.filter(username=username)

        if user is None:
            raise serializers.ValidationError('Invalid Username')