from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

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
    books_list=Book.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def add_todo(request):
    form=request.POST
    text=form["todo_text"]
    todo=ToDo(text=text)
    todo.save()
    return redirect(test)



def add_book(request):
    form=request.POST
    text=form["book_text"]
    subtitle=form["book.subtitle"] 
    description=form["book.description"]
    price=form["book.price"]
    genre=form["book.genre"]
    author=form["book.author"]
    year=form["book.year"]
    book=Book(text=text, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(books)

def delete_todo(request, id):
    todo=ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

