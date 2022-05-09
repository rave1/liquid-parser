from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework import viewsets
from rest_framework import views
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from userauth.serializers import UserSerializer, LoginSerializer, ProfileSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        data = serializer.data
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# class LoginView(views.APIView):
#     # This view should be accessible also for unauthenticated users.

#     def post(self, request, format=None):
#         serializer = LoginSerializer(data=self.request.data,
#             context={ 'request': self.request })
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return Response(None, status=status.HTTP_202_ACCEPTED)

class ProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        instance = User.objects.get(email=request.user.email)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
