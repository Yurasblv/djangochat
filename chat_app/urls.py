from django.urls import path
from chat_app.views import log_in_view, register_view, chat_view, index_view,log_out_view, ListMessageApiView

urlpatterns = [

    path('', log_in_view, name='login'),
    path('logout/',log_out_view,name='logout'),
    path('register/', register_view, name='register'),
    path('chat/', index_view, name='chat'),
    path('chat/<room_name>/', chat_view, name='room_chat'),
    path('api/data/', ListMessageApiView.as_view(({'get': 'list'})), name='messages_api')
]
