from django.shortcuts import render_to_response

from blogapp.models import my_entries
from todo.models import Todo


def index(request):
    entry = my_entries.objects.all()
    ls = Todo.objects.all()
    return render_to_response('indexg.html', {'list':entry,'ls':ls})


