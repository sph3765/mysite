from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice, Employee
from django.template import loader 
from django.shortcuts import render, get_object_or_404 
from django.urls import reverse 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_employee_list = Employee.objects.all(); 
    context = {
        'latest_question_list': latest_question_list,
        'latest_employee_list' : latest_employee_list, 
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    return render(request, 'polls/detail.html', {'question':question})

def detailEmployee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'polls/detailEmployee.html', {'employee': employee})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def addEmployee(request, passedFirstName, passedLastName):
    newEmployee = Employee(firstName=passedFirstName, lastName=passedLastName)
    newEmployee.save()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_employee_list = Employee.objects.all(); 
    context = {
        'latest_question_list': latest_question_list,
        'latest_employee_list' : latest_employee_list, 
    }
    return render(request, 'polls/index.html', context)
