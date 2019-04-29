from django.shortcuts import render
from django.http import HttpResponse

from todo.models import ListModel

# Create your views here.
def index(request):
    todo_list = ListModel.objects.all()

    if request.method == 'POST':
        get_text = request.POST.get('to_do')
        l = ListModel()
        l.text = get_text
        l.save()

    context = { 'list': todo_list }
    return render(request, 'index.html', context)

def edit_todo(request, id):
    todo_list = ListModel.objects.all()
    data = ()
    if request.method == 'POST':
        get_id = request.GET.get('id')
        get_text = request.POST.get('to_do')
        edit_todo = ListModel.objects.get(pk=get_id)
        edit_todo.text = get_text
        edit_todo.save()
    
    context = { 'list': todo_list }
    return JsonResponse(context, safe=False)

def delete_todo(request, pk):
    if request.method == 'POST':
        delete_todo = ListModel.objects.get(pk=get_id)
        delete_todo.delete()
        return render(request, 'index.html')