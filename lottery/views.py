from annoying.decorators import render_to
from lottery.models import Ticket
from django import forms


class TicketForm(forms.Form):
    number = forms.CharField(max_length=50)


@render_to('lottery/index.html')
def index(request):
    result = None
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            tickets = Ticket.objects.filter(number=form.cleaned_data['number'])
            if tickets:
                result = tickets[0]
    else:
        form = TicketForm()
    return {'form': form, 'result': result}
