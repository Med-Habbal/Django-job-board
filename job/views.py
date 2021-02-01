from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .filters import JobFilter
from .forms import ApplyForms, JobForm
from .models import Job


# Create your views here.

def Job_list(request):
    #Pour récupérer toutes les Jobs
    job_list = Job.objects.all()
    #filters
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs
    #pagination
    paginator = Paginator(job_list, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = {'jobs':page_obj, 'myfilter':myfilter,'counts':job_list}#templates name
    return render(request,'job/job_list.html',context)

def Job_detail(request, slug):
    job_detail = get_object_or_404(Job, slug=slug)

    if request.method=='POST':
        forms = ApplyForms(request.POST, request.FILES)
        if forms.is_valid():
            myform = forms.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        forms = ApplyForms()
    context = {'job':job_detail, 'forms': forms}
    return render(request,'job/job_detail.html',context)



@login_required
def add_job(request):

    if request.method=='POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    return render(request,'job/add_job.html',{'form1':form})


