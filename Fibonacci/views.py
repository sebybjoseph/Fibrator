from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import time

fibonacci_numbers = [1,1]

def findFibonacci(input_value):
    if input_value<1:
        return 0
    elif input_value>len(fibonacci_numbers):
        input_value -= len(fibonacci_numbers)
        for i in range(input_value):
            fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        return fibonacci_numbers[-1]
    else:
        return fibonacci_numbers[input_value-1]

def index(request):
    return render(request, 'Fibonacci/index.html')
    # return HttpResponse('Fibrator index')

def get_result(request):
    context = {}
    start_time = time.time()
    input_value = request.POST.get('input_value')
    if input_value.isnumeric():
        context["answer"] = findFibonacci(int(input_value))
    else:
        context["error"] = "Kindly enter a valid numerical input"
    time_taken = time.time() - start_time
    context["time_taken"] = "{:.20f}".format(time_taken)
    context["fibonacci_numbers"] = fibonacci_numbers
    return render(request, 'Fibonacci/index.html', context)

def clear_cache(request):
    global fibonacci_numbers
    fibonacci_numbers = [1,1]
    context = {
    "fibonacci_numbers": fibonacci_numbers
    }
    return render(request, 'Fibonacci/index.html', context)
