from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PVPGameStats, PVCGameStats
from .serializers import PVPGameStatsSerializer, PVCGameStatsSerializer

class PVPGameStatsView(APIView):
    def get(self, request, *args, **kwargs):
        games = PVPGameStats.objects.all()
        serializer = PVPGameStatsSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PVPGameStatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PVCGameStatsView(APIView):
    def get(self, request, *args, **kwargs):
        games = PVCGameStats.objects.all()
        serializer = PVCGameStatsSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PVCGameStatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

