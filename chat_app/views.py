from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from rest_framework.parsers import JSONParser
from chat_app.forms import SignUpForm
from chat_app.models import Message
from chat_app.serializers import MessageSerializer
from django.contrib.auth import logout
from rest_framework.viewsets import ModelViewSet
from chat_app.pagination import CustomPagination



def log_in_view(request):
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
        else:
            return HttpResponse('{"error": "User does not exist"}')
    return render(request, 'templates/index.html', {})


def log_out_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'templates/reg.html', context)


def index_view(request):
    return render(request, 'templates/title.html', {})


def chat_view(request, room_name):
    return render(request, 'templates/chat.html',
                  {'room_name': room_name})


class ListMessageApiView(ModelViewSet):
    serializer_class = MessageSerializer
    pagination_class = CustomPagination

    def get_object(self):
        return get_object_or_404(Note, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return Message.objects.all().order_by('time')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
