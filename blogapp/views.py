from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import my_entries



def get_entries(request, entry_id,):
    try:
        entry = my_entries.objects.get(id=entry_id)
        return render(request, "detailed_entry.html", {"entry": entry})
    except my_entries.DoesNotExist:
        raise Http404("We don't have any.")

def all_entries(request):

    if request.method == "POST":
        my_entries.objects.create(header=request.POST.get("header_input"),
                            body=request.POST.get("body_input"))

    return render(request, "my_entries.html", {"entries": my_entries.objects.all()})
