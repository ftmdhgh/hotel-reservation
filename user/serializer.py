#create, retreve, update, delete (CRUD)
from django.contrib.auth import get_user_model

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'f_name', 'l_name')
        extra_kwargs = {
            'password': {'min_length': 8, 'write_only' : True, 'required': True}
        }