from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    return render(request, "mychat/home.html")


def room(request, chat_room):
    user_name = request.GET.get("username")
    room_details = Room.objects.get(name=chat_room)
    context = {"chat_room": chat_room, "room_details": room_details, "user_name": user_name}
    return render(request, "mychat/room.html", context)


def check_view(request):
    chat_room = request.POST['room_name']
    username = request.POST["username"]

    if Room.objects.filter(name=chat_room).exists():
        return redirect(f"./{chat_room}/?username={username}")
    else:
        new_room = Room.objects.create(name=chat_room)
        new_room.save()
        return redirect(f"./{chat_room}/?username={username}")

    # return render(request, "mychat/home.html")
    # return redirect(f"/{chat_room}/?username={username}")


def send(request):
    message = request.POST["message"]
    username = request.POST["username"]
    room_id = request.POST["room_id"]

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse("Message sent successfully")


def get_messages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
