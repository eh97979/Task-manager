from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse


from task.models import Tasks
# Create your views here.


# def index(request):
#     tasks = Tasks.objects.order_by()
#     data = {'tasks':tasks}
#     return render(request, 'task/index.html', context=data)


class TasksView(generic.ListView):
    model = Tasks
    template_name = 'task/index.html'
    context_object_name = 'task'
    ordering = ['pk']
    # def get_queryset(self):
    #     return Tasks.objects.filter(its_done=False)


def add_task(request):
    if len(request.POST['addtask']) <200 and len(request.POST['addtask']) >0:
        text_to_add = Tasks(task_text=request.POST['addtask'])
        text_to_add.save()
        return HttpResponseRedirect(reverse('task:index'))
    else:
        return HttpResponseRedirect(reverse('task:index'))


def remove_all_task(request):
    Tasks.objects.filter().delete()
    return HttpResponseRedirect(reverse('task:index'))


def remove_1_task(request, task_pk):
    remove_task = get_object_or_404(Tasks, pk=task_pk)
    remove_task.delete()
    return HttpResponseRedirect(reverse('task:index'))


def done_task(request, task_pk):
    task_chosen = get_object_or_404(Tasks, pk=task_pk)
    task_chosen.its_done=True
    task_chosen.save()
    return HttpResponseRedirect(reverse('task:index'))


