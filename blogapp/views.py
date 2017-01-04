from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import my_entries
from .forms import BlogForm

def all_entries(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "my_entries.html", {"entries": my_entries.objects.filter(owner=request.user.id),
                                             "tags": Tag.objects.all(),
                                             "form": form})

def get_entries(request, e_id):
    try:
        entry = my_entries.objects.get(id=e_id)
        if request.user.id != entry.owner.id:
            raise PermissionDenied
        return render(request, "detailed_entries.html", {"entries": entry})
    except my_entries.DoesNotExist:
        raise Http404("We don't have any.")

@permission_required('is_superuser')
def show_all_entries(request):
    return render(request, "my_entries.html", {"entries": my_entries.objects.all()})

@permission_required('is_superuser')
def show_all_entries_from_user(request, userId):
    return render(request, "my_entries.html", {"entries": my_entries.objects.filter(owner=userId)})
