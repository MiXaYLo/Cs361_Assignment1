from django.conf.urls import url

from .views import all_entries, get_entries

urlpatterns = [
    url(r'^$', all_entries),
    #url(r'^blog/create/$', create_entry),
    url(r'^(?P<entry_id>[0-9])', get_entries)
]
