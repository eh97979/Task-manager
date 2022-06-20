from django.shortcuts import render
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
    
    def get_queryset(self):
        return Tasks.objects.filter(its_done=False)

def add_task(request):
    text_to_add = Tasks(task_text=request.POST['addtask'])
    text_to_add.save()
    return HttpResponseRedirect(reverse('task:index'))


def remove_all_task(request):
    Tasks.objects.filter().delete()
    return HttpResponseRedirect(reverse('task:index'))


def remove_1_task(request, pk):
    remove_task = Tasks.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('task:index'))

