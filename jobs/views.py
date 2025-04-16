from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form})

def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('job_list')
    return render(request, 'jobs/job_form.html', {'form': form})

def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})
