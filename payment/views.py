from django.shortcuts import render, redirect, reverse, get_object_or_404
from items.models import Items, Votes
from django.contrib.auth.models import User
from accounts.models import Profile
from django.conf import settings
from .forms import MakePaymentForm, OrderForm
from .models import Transaction
from django.contrib import messages
from django.utils import timezone
import stripe

stripe.api_key = settings.STRIPE_SECRET


def checkout(request, pk):
    item = get_object_or_404(Items, pk=pk)
    votes_number = request.session.get('votes_number', 'votes_number')
    price = 5
    total = 0
    total += votes_number * price
    request.session['total'] = total
    return render(request, 'checkout.html', {
        'votes_number': votes_number,
        'item': item,
        'price': price,
        'total': total
    })


def adding_vote(request, pk):
    item = get_object_or_404(Items, pk=pk)
    votes_number = request.session.get('votes_number', 'votes_number')
    if votes_number > 0:
        votes_number += 1
    request.session['votes_number'] = votes_number
    return redirect('checkout', pk=item.pk)


def removing_vote(request, pk):
    item = get_object_or_404(Items, pk=pk)
    votes_number = request.session.get('votes_number', 'votes_number')
    if votes_number > 1:
        votes_number -= 1
    request.session['votes_number'] = votes_number
    return redirect('checkout', pk=item.pk)


def cancel_vote(request, pk):
    item = get_object_or_404(Items, pk=pk)
    feature_session = request.session.pop('feature', 'item.id')
    request.session['feature'] = item.id
    return redirect('item_detail', pk=item.pk)


def payment(request, pk):
    item = get_object_or_404(Items, pk=pk)
    profile = get_object_or_404(Profile, username=request.user)
    votes_number = request.session.get('votes_number', 'votes_number')
    total = request.session.get('total', 'total')
    if request.method == 'POST':
        order_form = OrderForm(request.POST, request.FILES, instance=profile)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            user_details = order_form.save(commit=False)
            user_details.updated_date = timezone.now()
            user_details.save()
            transaction = Transaction(
                payment_details=user_details,
                feature=item,
                votes_number=votes_number,
                total_paid=total
            )
            transaction.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency='EUR',
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'])
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined! Please try again or try with different card')
            if customer.paid:
                messages.success(request, 'You have successfully paid! Thanks for voting!')
                request.session.pop('feature', 'item.id')

                votes = Votes.objects.filter(voted_item=item)
                user = User.objects.get(username=request.user)
                upvoted = False
                for vote in votes:
                    if str(vote.user) == str(user) and str(vote.voted_item) == str(item):
                        upvoted = True
                if upvoted is False:
                    vote = Votes(
                        voted_date=timezone.now(),
                        user=user,
                        voted_item=item
                    )
                    vote.votes_number = vote.votes_number + votes_number
                    vote.save()
                    item.votes = item.votes + votes_number
                    item.save()
                elif upvoted is True:
                    vote.votes_number = vote.votes_number + votes_number
                    vote.save()
                    item.votes = item.votes + votes_number
                    item.save()

                return redirect('item_detail', pk=item.pk)
            else:
                messages.error(request, 'We were unable to validate a payment with this card!')
        else:
            messages.error(request, 'We were unable to take a payment with this card!')
    else:
        order_form = OrderForm(instance=profile)
        payment_form = MakePaymentForm()
    return render(request, 'payment.html', {
        'item': item,
        'total': total,
        'votes_number': votes_number,
        'order_form': order_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE
    })
