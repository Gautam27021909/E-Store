from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return render(request, 'login.html', {'user': user})
        return render(request, 'login.html')
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        # return Response({
        #     "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
        #     "message": "User registered successfully.",
        # }, status=status.HTTP_201_CREATED)
        
        
        
def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(reqest):
    return render(reqest, 'contact.html')

def my_account(request):
    return render(request, "my-account.html")

def product_detail(request):
    return render(request, 'product-detail.html')

def product_list(request):
    return render(request, 'product-list.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def login(request):
    
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def forgot(request):
    return render(request, "forgot.html")

def otp(request):
    return render(request, "otp.html")

def login1(request):
    return render(request, "login1.html")