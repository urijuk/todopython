from django.shortcuts import render, HttpResponse


def homepage(request):
    return HttpResponse("hello Urmat")
def test(request):
    return render(request, "test.html")