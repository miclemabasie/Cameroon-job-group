from django.shortcuts import render, HttpResponseRedirect
from .models import Job
from django.contrib.auth.decorators import login_required
from .forms import JobCreateForm
from django.urls import reverse

# Job list View
# Job detail view
# Job create view
# Job update view
# Job Delete View

# CRUD


def list_view(request):
    job_list = Job.objects.all()
    template_name = "list.html"
    context = {
        "jobs": job_list,
        "job_list": "active",
    }

    return render(request, template_name, context)


@login_required
def job_create_view(request):
    form = JobCreateForm(request.POST or None)
    template_name = "create.html"
    if request.method == "POST":
        if form.is_valid():
            print(request.POST)
            # Create the job

            # title = form.cleaned_data.get("title")
            # description = form.cleaned_data.get("description")
            # qualifications = form.cleaned_data.get("qualifications")
            # min_salary = form.cleaned_data.get("min_salary")
            # max_salary = form.cleaned_data.get("max_salary")
            # application_details = form.cleaned_data.get("application_details")
            # job = Job.objects.create(
            #     user=request.user,
            #     title=title,
            #     description=description,
            #     qualifications=qualifications,
            #     min_salary=min_salary,
            #     max_salary=max_salary,
            #     application_details=application_details,
            # )
            # job.save()

            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return HttpResponseRedirect("/jobs/")

    context = {
        "form": form,
        "create": "active",
    }
    return render(request, template_name, context)
