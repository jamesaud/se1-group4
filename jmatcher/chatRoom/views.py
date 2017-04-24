from django.http import HttpResponse
import random
import string
from django.db import transaction
from django.shortcuts import render, redirect

from .models import Room


def chat(request):
    return render(request, "templates/chatRoom/about.html")

def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    new_room = None
    while not new_room:
        with transaction.atomic():
            # label = haikunator.haikunate()
            label = "jmatcherChat"
            # if Room.objects.filter(label=label).exists():
            #     continue
            new_room = Room.objects.create(label=label)
    return redirect(chat_room, label=label)

def chat_room(request, label):
    """
    Room view - show the room, with latest messages.
    The template for this view has the WebSocket business to send and stream
    messages, so see the template for where the magic happens.
    """
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "templates/chatRoom/room.html", {
        'room': room,
        'messages': messages,
    })