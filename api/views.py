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

    def retrieve(self, request, pk: int):
        only_country = CountrySerializer(Country.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=only_country.data)

    def create(self, request):
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    def destroy(self, request, pk: int):
        only_country = CountrySerializer(Country.objects.get(pk=pk))
        return Response(status=status.HTTP_204_NO_CONTENT)

        
