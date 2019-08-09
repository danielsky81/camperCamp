from django.shortcuts import render, redirect, reverse, get_object_or_404
from items.models import Items
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET

def checkout(request, pk):
    voting_session = request.session.get('voting_session', {})
    session_items = []
    price = 5
    total = 0
    for pk, votes_number in voting_session.items():
        item = get_object_or_404(Items, pk=pk)
        total += votes_number * price
        session_items.append({'pk': pk, 'votes_number': votes_number, 'item': item, 'price': price})
    return render(request, 'checkout.html', {'item': item, 'votes_number': votes_number, 'total': total, 'session_items': session_items})

def adding_vote(request, pk):
    item = get_object_or_404(Items, pk=pk)
    voting_session = request.session.get('voting_session', {})
    if voting_session[pk] > 0:
        voting_session[pk] += 1
    request.session['voting_session'] = voting_session
    return redirect('checkout', pk=item.pk)

def removing_vote(request, pk):
    item = get_object_or_404(Items, pk=pk)
    voting_session = request.session.get('voting_session', {})
    if voting_session[pk] > 1:
        voting_session[pk] -= 1
    request.session['voting_session'] = voting_session
    return redirect('checkout', pk=item.pk)

def cancel_vote(request, pk):
    item = get_object_or_404(Items, pk=pk)
    voting_session = request.session.get('voting_session', {})
    voting_session.pop(pk)
    request.session['voting_session'] = voting_session
    return redirect('item_detail', pk=item.pk)


def payment(request, pk):
    votes_number = request.session['votes_number']
    print(votes_number)
    return render(request, 'payment.html')

