from django.shortcuts import render, HttpResponse , HttpResponsePermanentRedirect

def home(request):
    return render(request, "index.html")
