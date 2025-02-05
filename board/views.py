from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Response
from datetime import datetime

def index(request):
    latest_thread_list = Thread.objects.order_by('-pub_date')
    return render(request, "board/index.html", {"latest_thread_list": latest_thread_list})

def create_thread(request):
    if request.method == "POST":
        thread_text = request.POST.get("thread_text", "")
        if thread_text:
            thread = Thread(thread_text=thread_text, pub_date=datetime.now())
            thread.save()
            return redirect("board:detail", thread_id=thread.id)
    return redirect("board:index")

def detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    responses = thread.response_set.all()
    return render(request, "board/detail.html", {"thread": thread, "responses": responses})

def tweet(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == "POST":
        response_text = request.POST.get("response_text", "")
        name_text = request.POST.get("name_text", "")
        if response_text and name_text:
            response = Response(thread=thread, response_text=response_text, name_text=name_text, tweet_date=datetime.now())
            response.save()
            return redirect("board:detail", thread_id=thread.id)
    return render(request, "board/detail.html", {"thread": thread})

def delete_thread(request):
    if request.method == "POST":
        thread_id = request.POST.get("thread_id")
        thread = get_object_or_404(Thread, pk=thread_id)
        thread.delete()
        return redirect("board:index")
    latest_thread_list = Thread.objects.order_by('-pub_date')
    return render(request, "board/index.html", {"latest_thread_list": latest_thread_list})