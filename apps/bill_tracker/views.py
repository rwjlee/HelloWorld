from django.shortcuts import render, redirect
from apps.bill_tracker.models import Bill
from django.contrib import messages

def index(request):
    if 'user_id' not in request.session:
        return redirect('travel:login')

    context = {
        'bills': Bill.objects.filter(user_id = request.session['user_id'])
    }

    return render(request, 'bill_tracker/index.html', context)

def add_bill(request):
    if 'user_id' not in request.session:
        return redirect('travel:login')

    html_desc = request.POST['html_desc']
    html_amount = request.POST['html_amount']
    html_user = request.session['user_id']

    if len(html_desc) > 0:    
        try:
            bill = Bill.objects.create(desc = html_desc, amount = html_amount, user_id = html_user)
        except:
            messages.error(request, 'Bill cannot be added')

    else:
        messages.error(request, 'Description cannot be empty')

    return redirect('bill_tracker:index')

def delete_bill(request, bill_id):

    bill = Bill.objects.get(id = bill_id)
    bill.delete()

    return redirect('bill_tracker:index')

def edit_page(request, bill_id):
    context = {
        'bill': Bill.objects.get(id = bill_id)
    }
    return render(request, 'bill_tracker/edit_page.html', context)

def edit_bill(request):
    
    try:
        bill = Bill.objects.get(id = request.POST['html_id'])
        bill.desc = request.POST['html_desc']
        bill.amount = request.POST['html_amount']
        bill.save()
    except:
        messages.error(request, 'Bill cannot be changed')

    return redirect('bill_tracker:index')

