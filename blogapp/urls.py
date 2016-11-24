from django.conf.urls import url

from .views import all_entries, get_entries
urlpatterns = [
    url(r'^blog/entries/$', all_entries),
    url(r'^blog/entries/(?P<entry_id>[0-9])', get_entries)
]
