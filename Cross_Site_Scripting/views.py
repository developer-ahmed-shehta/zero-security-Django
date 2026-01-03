# Cross_Site_Scripting/views.py
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import XSSComment

def stored_xss(request):
    if request.method == "POST": # here i have a vulnerability where user input is directly stored and rendered later
        XSSComment.objects.create(
            username=request.POST.get("username"),
            message=request.POST.get("message")  # RAW INPUT
        )
        return redirect("stored_xss")

    comments = XSSComment.objects.all() # i restore all comments where one of them may contain malicious script
    print(comments)
    return render(request, "Cross_Site_Scripting/stored_xss.html", {"comments": comments})

def reflected_xss(request):
    q = request.GET.get("q", "")
    return render(request, "Cross_Site_Scripting/reflected_xss.html", {"q": q})

@login_required
def xss_demo_action(request):
    request.user.profile.is_hacked = True
    request.user.profile.save()
    return HttpResponse("Action performed")
