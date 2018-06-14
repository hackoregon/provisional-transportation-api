from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^slides/safetyhotline/(?P<date_filter>\d+)', views.safetyhotline),
    url(r'^slides/safetyhotline/', views.safetyhotline),
    url(r'^slides/crashes/(?P<date_filter>\d+)', views.crash),
    url(r'^slides/crashes/', views.crash),
]
urlpatterns = format_suffix_patterns(urlpatterns)
