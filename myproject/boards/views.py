from django.shortcuts import render, get_object_or_404
from .models import Board

def home(request):
    return render(request, 'home.html')

def topics(request):
    boards = Board.objects.all()
    return render(request, 'topics.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'detail.html', {'board': board})

# Create your views here.
