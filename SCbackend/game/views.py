from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PVPGameStats, PVCGameStats
from user_profile.models import User
from .serializers import PVPGameStatsSerializer, PVCGameStatsSerializer

class PVPGameStatsView(APIView):

    def post(self, request, *args, **kwargs):
        winner_wallet_address = request.data.get('winner_wallet_address')
        loser_wallet_address = request.data.get('loser_wallet_address')

        winner = User.objects.get(wallet_address=winner_wallet_address)
        loser = User.objects.get(wallet_address=loser_wallet_address)

        winner.add_points(1)
        loser.add_points(-1)

        winner.save()
        loser.save()

        game_stats = PVPGameStats.objects.create()
        game_stats.winner.add(winner)
        game_stats.loser.add(loser)

        serializer = PVPGameStatsSerializer(game_stats)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PVCGameStatsView(APIView):

    def post(self, request, *args, **kwargs):
        player_wallet_address = request.data.get('player_wallet_address')
        is_winner = request.data.get('is_winner')

        player = User.objects.get(wallet_address=player_wallet_address)

        if is_winner:
            player.add_points(1)
        else:
            player.add_points(-1)

        player.save()

        game_stats = PVCGameStats.objects.create(player=player, is_winner=is_winner)

        serializer = PVCGameStatsSerializer(game_stats)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

