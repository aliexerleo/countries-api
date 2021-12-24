from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from apps.country.models import Country


# Serializers
from api.serializers import CountrySerializer

class CountryViewSet(ViewSet):

    def list(self, request):
        serializer = Country.objects.all()
        serializer = CountrySerializer(serializer, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def create(self, request):
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    def retrieve(self, request, pk: int):
        instance = CountrySerializer(Country.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=instance.data)

    def update(self, request, pk: int):
        pass

    def destroy(self, request, pk: int):
        instance = Country.objects.get(pk=pk)
        instance.delete()
        messages= {
            'messages': 'country was deleted'
        }
        return Response(status=status.HTTP_204_NO_CONTENT, data=messages)