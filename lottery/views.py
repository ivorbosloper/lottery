from annoying.decorators import render_to, ajax_request
from lottery.models import Ticket
from django import forms
from annoying.functions import get_object_or_None


class TicketForm(forms.Form):
    number = forms.CharField(max_length=50)


@render_to('lottery/index.html')
def index(request):
    result = None
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            result = get_object_or_None(Ticket, number=form.cleaned_data['number'])
    else:
        form = TicketForm()
    return {'form': form, 'result': result}


@ajax_request
def jsonf(request):
    result = get_object_or_None(Ticket, number=request.GET['number'])
    if result:
        return {'ticket': str(result)}
    return {}
