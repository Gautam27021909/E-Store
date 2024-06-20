from rest_framework import serializers
from .models import Register
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
        extra_kwargs = {
            'fname': {'required': True},
        }
        
    username = serializers.CharField( required=True, validators = [UniqueValidator(queryset= Register.objects.all())])
    email = serializers.EmailField( required=True, validators = [UniqueValidator(queryset= Register.objects.all())])
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    def create(self, validated_data):
        user = Register.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            fname=validated_data['fname'],
            pno=validated_data['pno'],
            password= validated_data['password'],
            
        )

        # user.set_password(validated_data['password'])
        user.save()

        return user