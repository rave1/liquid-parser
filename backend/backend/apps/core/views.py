from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from core.models import Liquid
from core.serializers import LiquidSerializer
from core.utils import parse_liquid

# Create your views here.


class LiquidViewSet(viewsets.ModelViewSet):
    queryset = Liquid.objects.all()
    serializer_class = LiquidSerializer
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        url = request.data['url']
        data = parse_liquid(url)
        print(data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
