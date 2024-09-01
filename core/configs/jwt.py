from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    'TOKEN_OBTAIN_SERIALIZER': 'stackoverflow_clone.apps.users.serializers.MyTokenObtainPairSerializer',
}
