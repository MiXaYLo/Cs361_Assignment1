from django.conf.urls import url

from .views import all_entries, get_entries,show_all_entries,show_all_entries_from_user

urlpatterns = [
    url(r'^$', all_entries),
    url(r'^(?P<e_id>[0-9]+)', get_entries),
    url(r'^all/$', show_all_entries),
    url(r'^all/user/(?P<userId>[0-9]+)$', show_all_entries_from_user),
]
