from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView, CreateView
from django.views import View
import stripe
from django.conf import settings
from django.core.mail import send_mail
from .models import MembershipPlan, MembershipPlanPrice
from users.models import Account, Membership
import datetime

stripe.api_key = settings.STRIPE_SECRET_KEY
class Index(TemplateView):
    template_name = 'gym_app/index.html'



class Checkout(View):
    def post(self, request, *args, **kwargs):
        price = MembershipPlanPrice.objects.get(id=self.kwargs["pk"])
        print(price.membership_plan)
        DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types  = ['card'],
            line_items = [
                {
                    'price' : price.stripe_price,
                    'quantity': 1,
                },
            ],
            mode = 'payment',
            success_url = DOMAIN + '/success/',
            cancel_url = DOMAIN,
        )
        acc_user = Account.objects.get(user = self.request.user)
        query_date = Membership.objects.filter(account = acc_user)
        for date in query_date:
            if date.date == datetime.date.today():
                return redirect('gym:index')
            else:
                user_progress =  Account.objects.get(user = self.request.user)
                user_progress.user_progress += 1
                Account.objects.filter(user = self.request.user).update(user_progress = user_progress.user_progress)
                
                Membership.objects.create(account = acc_user, date = datetime.date.today(), membership_plan = price.membership_plan)
        return redirect(checkout_session.url)

class PlanView(TemplateView):
    template_name = "gym_app/plan.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plan = MembershipPlan.objects.get(name = "Monthly Plan")
        price = MembershipPlanPrice.objects.filter(membership_plan = plan)

        context['plan'] = plan
        context['price_fields'] = price

        return context

class PlansView(ListView):
    template_name = 'gym_app/plans.html'
    model = MembershipPlan
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # gets all plans
        name_of_plans = MembershipPlan.objects.all()
        context['name_of_plans'] = name_of_plans
        
        return context

class Success(TemplateView):
    template_name = 'gym_app/success.html'

        
class CancelView(TemplateView):
    template_name = 'gym_app/cancel.html'


def send_email(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        problem_description = request.POST['problem_description']
        send_mail(
            'User problem',
            'first_name'+first_name+'last_name'+'\n'
            'problem_description'+problem_description,
            email,
            ['stefan.programming22@gmail.com'],
        )
        return render(request, 'gym_app/help.html')

    
    return render(request, 'gym_app/help.html')


class AboutView(TemplateView):
    template_name = 'gym_app/about.html'


class AccountView(TemplateView):
    template_name = 'gym_app/account.html'

