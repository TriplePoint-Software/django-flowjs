from django.conf.urls import url

from views import upload, check_state

app_name = 'flowjs'

# JSON REQUESTS
urlpatterns = [
    url(r'^upload/$', upload),
    url(r'^state/$', check_state),
]
