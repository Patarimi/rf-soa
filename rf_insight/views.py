from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "rf_insight/index.html", context)
