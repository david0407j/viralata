from django.shortcuts import render


def cores(request):
    return render(request, "cores/home.html")
