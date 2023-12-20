from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import User
from .serializers import UserSerializer

class UserAPI(CreateAPIView, ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailsAPI(UpdateAPIView, DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        print(**kwargs)
        return super().get(request, *args, **kwargs)