from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import my_entries

def all_entries(request):

    if request.method == "POST":
        entry = my_entries.objects.create(body=request.POST.get("body_name"),
                            header=request.POST.get("header_name"),
                            owner=request.user)

        entry.tags.add(*request.POST.getlist("tag_names"))


    return render(request, "my_entries.html", {"entries": my_entries.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all()})


def get_entries(request, e_id):
    try:
        entry = my_entries.objects.get(id=e_id)
        if request.user.id != entry.owner.id:
            raise PermissionDenied
        return render(request, "detailed_entries.html", {"entry":entry})
    except my_entries.DoesNotExist:
        raise Http404("We don't have any.")