from django.urls import path
from csvfile.views import UploadFileView,check_user
from csvfile import views
from django.conf.urls import url, include

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    url('checkuser/(?P<pk>[0-9]+)',views.check_user,name='check-user')

]