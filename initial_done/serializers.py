from rest_framework import serializers
from .models import User_part

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User_part
        fields = ['id','first_name','last_name','email','password1']

