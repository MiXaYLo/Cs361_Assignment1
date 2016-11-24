from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import my_entries



def all_entries(request):
    return render(request, "my_entries.html", {"entries": my_entries})

def get_entries(request,entry_id):
    try:
        return HttpResponse("<h3>"+my_entries[int(entry_id)][0]+"</h3>"+ '<br />' + my_entries[int(entry_id)][1])
    except IndexError:
        raise  Http404("We don't have any.")

