from django.urls import path
from . import views
from . import api
app_name = 'jobs'

urlpatterns = [
    path('',views.Job_list, name='job_list'),
    path('add',views.add_job, name='add_job'),
    path('<slug:slug>',views.Job_detail, name='job_detail'),

    ## api
    path('api/list',api.job_list_api, name='job_list_api'),
    path('api/list/<int:id>',api.job_detail_api, name='job_detail_api'),
    path('api/list/v2/api',api.JoblistApi.as_view(), name='JoblistApi'),

    path('api/list/v3/<int:id>',api.JobDetail.as_view(), name='JobDetail'),
]
