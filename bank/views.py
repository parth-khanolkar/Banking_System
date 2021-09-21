from bank.models import Transact
from bank.forms import TransactionForm
from bank.models import History
from bank.models import Deposit
from bank.forms import ActionForm
from bank.models import User
from django.shortcuts import redirect, render


# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def WithdrawPage(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        fm = ActionForm(request.POST, instance = pi)
        if fm.is_valid():
            unm = fm.cleaned_data['username']
            eid = fm.cleaned_data['email_id']
            cnt = fm.cleaned_data['contact']
            amt = fm.cleaned_data['amount']
            if amt <= pi.balance:
                reg = Deposit(username=unm, email_id=eid, contact=cnt, amount=amt)
                reg.save()
                bal = int(amt)
                pi.balance -= bal
                pi.save()
                act = "Withdraw"
                sts = "Success"
                hst = History(username=unm, email_id=eid, contact=cnt, amount=amt, action=act, status=sts)
                hst.save()
                return redirect('Users')
            else:
                at = "Insufficient Balance!"
                act = "Withdraw"
                sts = "Failed"
                hst = History(username=unm, email_id=eid, contact=cnt, amount=amt, action=act, status=sts)
                hst.save()
                return render(request, 'withdraw.html', {"form" : fm, "status": at})
    else:
        pi = User.objects.get(pk = id)
        fm = ActionForm(instance = pi)
    return render(request, 'withdraw.html', {"form" : fm})

def DepositPage(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        fm = ActionForm(request.POST, instance = pi)
        if fm.is_valid():
            unm = fm.cleaned_data['username']
            eid = fm.cleaned_data['email_id']
            cnt = fm.cleaned_data['contact']
            amt = fm.cleaned_data['amount']
            reg = Deposit(username=unm, email_id=eid, contact=cnt, amount=amt)
            reg.save()
            act = "Deposit"
            sts = "Success"
            hst = History(username=unm, email_id=eid, contact=cnt, amount=amt, action=act, status=sts)
            hst.save()
            bal = int(amt)
            pi.balance += bal
            pi.save()
            return redirect('Users')
    else:
        pi = User.objects.get(pk = id)
        fm = ActionForm(instance = pi)
    return render(request, 'deposit.html', {"form" : fm})


def HistoryPage(request):
    data = History.objects.all()
    return render(request, 'history.html', {"data" : data})

def TransferPage(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        fm = TransactionForm(request.POST, instance = pi)
        if fm.is_valid():
            unm = fm.cleaned_data['username']
            eid = fm.cleaned_data['email_id']
            cnt = fm.cleaned_data['contact']
            amt = fm.cleaned_data['amount']
            rev = fm.cleaned_data['receiver']
            if amt <= pi.balance:
                reg = Transact(username=unm, email_id=eid, contact=cnt, amount=amt, receiver=rev)
                reg.save()
                bal = int(amt)
                pi.balance -= bal
                pi.save()
                us = User.objects.get(username = rev)
                us.balance += bal
                us.save()
                act = "Transfer"
                sts = "Success"
                hst = History(username=unm, email_id=eid, contact=cnt, amount=amt, action=act, status=sts)
                hst.save()
                return redirect('Users')
            else:
                at = "Insufficient Balance!"
                act = "Transfer"
                sts = "Failed"
                hst = History(username=unm, email_id=eid, contact=cnt, amount=amt, action=act, status=sts)
                hst.save()
                return render(request, 'transfer.html', {"form" : fm, "status": at})
    else:
        pi = User.objects.get(pk = id)
        fm = TransactionForm(instance = pi)
    return render(request, 'transfer.html', {"form" : fm})
    

def UsersPage(request):
    data=User.objects.all()
    return render(request, 'users.html',{"data":data})
