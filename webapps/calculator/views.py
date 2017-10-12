from django.shortcuts import render

# Create your views here.

#home html page
def calculator_home(request):
    context ={}
    context['current'] = 0
    context['flag'] = '0'
    context['operator'] = ''
    context['previous'] = ''
    context['previous_after'] = ''

    return render(request, 'calculator_home.html', context)

def calculator_start(request):
    context = {}
    print(request.POST.get('operator'))


    if 'calc_buttons' in request.POST and 'operator' in request.POST and 'previous' in request.POST and 'current' in request.POST and 'flag'in request.POST and 'previous_after' in request.POST:  #check if some button is presses
        if request.POST.get('calc_buttons').isdigit():
            #check if its 2nd number or 1st
            if not request.POST.get('flag') or request.POST.get('flag') == '0':
                current = request.POST.get('calc_buttons')
                prev = request.POST.get('previous')
                context['current'] = prev + current
                context['previous'] = prev + current

            else:

                #current = request.POST.get('previous') + request.POST.get('calc_buttons')
                current = request.POST.get('calc_buttons')
                prev_after = request.POST.get('previous_after')
                context['current'] = prev_after + current
                context['previous_after'] = prev_after + current
                context['previous'] = request.POST.get('previous')
                context['flag'] = request.POST.get('flag')
                context['operator'] = request.POST.get('operator')


        #if operator is pressed
        else:
            #to check if operator is only 5 of these operators, otherwise malformed
            if request.POST.get('calc_buttons') in ["+","-","x","/","="]:

                #condition to check if operator is selected before number or operator is null or not
                if not request.POST.get('previous'):

                    context['current'] = 'Error: select a number first'
                    context['flag'] = 0
                else:
                    #check if previous_after is null or not to check if it's the first opertaor or not
                    if not request.POST.get('previous_after'):
                        context['previous'] = request.POST.get('previous')
                        context['current'] = request.POST.get('current')
                        context['flag'] = 1
                        context['operator'] = request.POST.get('calc_buttons')

                    else:
                        op = request.POST.get('operator')
                        #check if numbers are actually numbers
                        try:
                            cur = int(request.POST.get('current'))
                            pre = int(request.POST.get('previous'))
                        except:
                            context['current'] = 'MALINFORMED, Invalid Number in Calculation'
                            context['flag'] = '0'
                            context['operator'] = ''
                            context['previous'] = ''
                            context['previous_after'] = ''
                            return render(request, 'calculator_home.html', context)
                        answer = calculation(op,cur,pre)
                        #to check if its equals operator or division by zero was performed, then reset everything
                        if request.POST.get('calc_buttons') == '=' or answer == 'Invalid, Division by zero':
                            context['current'] = answer
                            context['flag'] = '0'
                            context['operator'] = ''
                            context['previous'] = ''
                            context['previous_after'] = ''
                        else:
                            context['current'] = answer
                            context['previous'] = answer
                            context['operator'] = request.POST.get('calc_buttons')
                            context['flag'] = request.POST.get('flag')
            # ********************************************
            else:
                context['current'] = 'MALFORMED, Invalid Operator'
                context['flag'] = '0'
                context['operator'] = ''
                context['previous'] = ''
                context['previous_after'] = ''
                return render(request, 'calculator_home.html', context)


        return render(request, 'calculator_home.html', context)
    #condition to check if some parameter isn't passed
    else:
        context['current'] = 'MALFORMED'
        context['flag'] = '0'
        context['operator'] = ''
        context['previous'] = ''
        context['previous_after'] = ''
        return render(request, 'calculator_home.html', context)

#function to perform calculations
def calculation(op, cur, pre):
    if op == '+':
        answer = cur + pre
    elif op == '-':
        answer = pre - cur
    elif op == 'x':
        answer = pre * cur
    else:
        if int(cur) == 0:
            return 'Invalid, Division by zero'
        else:
            answer = int(pre / cur)
    return answer