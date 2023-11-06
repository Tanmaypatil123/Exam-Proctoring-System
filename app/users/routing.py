from django.urls import path
from users.consumers import ConnectUser

websocket_urlpatterns =[

    path('ws/wsc/',ConnectUser.as_asgi())
]