from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "todo.html")
def test(request):
    return render(request, "test.html")
def second(request):
    return HttpResponse("test 2 page")
def third(request):
    return HttpResponse("This is page test3")
def add(request):
    return render(request, "add.html")
def change(request):
    return render(request, "change.html")
def delete(request):
    return render(request, "delete.html")