from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from django.db.models import Sum, F, ExpressionWrapper, fields
from django.db.models.functions import TruncMonth, TruncDay
from user_profile.models import User
from game.models import PVPGameStats, PVCGameStats
from .serializers import TopUsersSerializer

class DailyTopUsersView(APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)

        # Calculate the daily score for each user
        daily_score_expression = ExpressionWrapper(
            Sum('pvpgamestats__winner', filter=PVPGameStats.objects.filter(game_date__date=yesterday)) +
            Sum('pvcgamestats__is_winner', filter=PVCGameStats.objects.filter(game_date__date=yesterday)),
            output_field=fields.FloatField()
        )

        users = User.objects.annotate(daily_score=daily_score_expression)
        top_users = users.order_by('-daily_score')[:10]

        # Get the current user's position and score
        current_user = users.filter(wallet_address=request.user.wallet_address).first()

        serializer = TopUsersSerializer({'users': top_users, 'current_user': current_user})
        return Response(serializer.data, status=status.HTTP_200_OK)

class MonthlyTopUsersView(APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.now().date()
        first_day_of_month = today.replace(day=1)

        # Calculate the monthly score for each user
        monthly_score_expression = ExpressionWrapper(
            Sum('pvpgamestats__winner', filter=PVPGameStats.objects.filter(game_date__date__gte=first_day_of_month)) +
            Sum('pvcgamestats__is_winner', filter=PVCGameStats.objects.filter(game_date__date__gte=first_day_of_month)),
            output_field=fields.FloatField()
        )

        users = User.objects.annotate(monthly_score=monthly_score_expression)
        top_users = users.order_by('-monthly_score')[:10]

        # Get the current user's position and score
        current_user = users.filter(wallet_address=request.user.wallet_address).first()

        serializer = TopUsersSerializer({'users': top_users, 'current_user': current_user})
        return Response(serializer.data, status=status.HTTP_200_OK)

