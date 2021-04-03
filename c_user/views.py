from .serializers import (RegisterSerializer,
                          MyTokenObtainPairSerializer, UsersSerializers,
                          UserUpdateSerializer,)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import User
from .send import send_conf_mail
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from .token import account_activation_token
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions


class RegisterView(APIView):

    def post(self, request):
        user_serializer = RegisterSerializer(data=request.data)
        try:
            if user_serializer.is_valid():
                user = user_serializer.save()
                user.is_active = False
                user.save()
                send_conf_mail(request, user)
                return Response('Email was send for confirmation', status=status.HTTP_201_CREATED)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            user = None


@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer])
def activating(request, uidb64, token):
    try:
        primary_key = force_text(urlsafe_base64_decode(uidb64))
        user = User.object.get(pk=primary_key)
    except (TypeError, ValueError, OverflowError) as e:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response('Account activated')
    else:
        return Response('Error')


class UsersView(generics.ListAPIView):
    serializer_class = UsersSerializers
    queryset = User.object.all()


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.object.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsOwner]

    def put(self, request, *args, **kwargs):
        return Response('Put method not allowed')


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny, ]

