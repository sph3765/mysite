from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice, Employee, Department
from django.template import loader 
from django.shortcuts import render, get_object_or_404 
from django.urls import reverse 

# from django import template
# import functools
# register = template.Library() 

# @register.simple_tag
# def for_each(action, l):
#     for ele in l:
#         action(ele)


def index(request):
    someVariable = "007jamesbond"
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_employee_list = Employee.objects.all(); 
    context = {
        'latest_question_list': latest_question_list,
        'latest_employee_list' : latest_employee_list, 
        'someVariable' : someVariable, 
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    return render(request, 'polls/detail.html', {'question':question})

def detailEmployee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    departmentList = Department.objects.all()
    context = {
        'employee' : employee,
        'departmentList' : departmentList, 
    }
    return render(request, 'polls/detailEmployee.html', context)

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

def addEmployee(request):
    passedFN = request.POST.get("firstname")
    passedLN = request.POST.get("lastname")
    newEmployee = Employee(firstName=passedFN, lastName=passedLN)
    newEmployee.save()

    return HttpResponseRedirect(reverse('polls:index'))


def putInDepartment(request, employee_id):
    employeeObject = get_object_or_404(Employee, pk=employee_id)
    dpName = request.POST.get("departmentName")
    newDepartment = Department(departmentName=dpName)
    try:
        newDepartment.save()
    except(KeyError):
        return render(request, 'polls/detailEmployee', {
            'polls:detailEmployee' : employeeObject.id, 
        })

    else: 
        return HttpResponseRedirect(reverse('polls:index'))
