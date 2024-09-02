from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import datetime

# Create your views here.

# Commit: List all tasks
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request,'list_tasks.html', {"tasks" : tasks})

# Commit: Convert value to float with default
def number_float (value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

# Commit: Create a new task
def create_tasks(request):

    if request.method == 'POST':
        budget_edit = number_float(request.POST.get('budget_edit', ''))
        budget = number_float(request.POST.get('budget', ''))
        payment = number_float(request.POST.get('payment',''))
        title = request.POST.get('title')
        date = request.POST.get('date') or None  

        budget_edit = budget - payment

        task = Task(title=title, payment=payment, date=date, budget=budget, budget_edit=budget_edit)
        task.save()
        return redirect('/tasks/')

# Commit: Edit an existing task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        budget_edit = number_float(request.POST.get('budget_edit', ''))
        budget = number_float(request.POST.get('budget', ''))
        payment = number_float(request.POST.get('payment', ''))
        title = request.POST.get('title')
        date = request.POST.get('date') or None  

        budget_edit = budget - payment

        # Actualiza los campos de la instancia existente
        task.title = title
        task.payment = payment
        task.date = date
        task.budget = budget
        task.budget_edit = budget_edit
        task.save()
        
        return redirect('/tasks/')
    return render(request, 'edit_task.html', {'task': task})

# Commit: Delete a task
def delete_task(reques, task_id):
    delete_task =Task.objects.get(id=task_id)
    delete_task.delete()
    return redirect('/tasks/')