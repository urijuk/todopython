from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books

def homepage(request):
    return render(request, "todo.html")
def test(request):
    todo_list=ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})
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
def books(request):
    books_list=Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})
def add_todo(request):
    form=request.POST
    text=form["todo_text"]
    todo=ToDo(text=text)
    todo.save()
    return redirect(test)