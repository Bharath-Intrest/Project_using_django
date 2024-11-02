from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from . import models as mod
import base64

def login_pg(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        psw = request.POST.get('psw')
        try:
            lst = log_in.objects.get(user_name=uname)
            lst_id = lst.id
            if uname == lst.user_name and psw == lst.password1:
                return redirect('home', lst_id=lst_id)
            else:
                return HttpResponse("Username or password is incorrect")
        except log_in.DoesNotExist:
            return HttpResponse("Username or password is incorrect")

    return render(request, 'login_pg.html')

def home1(request, lst_id):
    details = home.objects.get(id=lst_id)
    img = base64.b64encode(details.user_img).decode('utf-8')
    recent_up = all_up_doc.objects.all()
    pro_img = base64.b64encode(details.user_img).decode('utf-8')
    return render(request, 'home.html', {'details': details, 'img': img, 'recent': recent_up, 'pro_img': pro_img})

def student(request,dyn):
    details = home.objects.get(id=2)
    img = base64.b64encode(details.user_img).decode('utf-8')
    pro_img = base64.b64encode(details.user_img).decode('utf-8')
    pro_d=mod.course.objects.get(id=2)
    return render(request, 'student.html', {'details': details, 'img': img, 'pro_img': pro_img,'pro_d':pro_d})

def course(request):
    return render(request, 'course.html', {'name': 'course_pg'})

# Fetch chat history
def get_chat_history(request, user1_id, user2_id):
    chats = user_chat.objects.filter(user1=user1_id, user2=user2_id).order_by('s_date_time')
    chat_data = [{
        "sender": "user1" if chat.user1 == user1_id else "user2",
        "message": chat.send or chat.receive
    } for chat in chats]
    return JsonResponse({"chats": chat_data})

# Save new chat message
def save_chat(request):
    if request.method == "POST":
        sender_id = request.POST.get("sender_id")
        receiver_id = request.POST.get("receiver_id")
        message = request.POST.get("message")

        # Save message with sender as either 'send' or 'receive'
        user_chat.objects.create(
            user1=sender_id,
            user2=receiver_id,
            send=message if sender_id else None,
            receive=message if receiver_id else None
        )
        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"}, status=400)

def course_details(request,dynamic):
    lst=mod.course.objects.all()
    return render(request,'course_details.html',{'lst':lst})

def course_pg(request,dyn3):
    lst=mod.course.objects.get(id=1)
    return render(request,'course_pg.html',{'lst':lst})
