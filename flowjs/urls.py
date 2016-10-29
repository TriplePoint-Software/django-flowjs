from django.conf.urls import patterns, url
from views import upload, check_state


# JSON REQUESTS
urlpatterns = patterns('',
                       url(r'^upload/$', upload),
                       url(r'^state/$', check_state),
)
