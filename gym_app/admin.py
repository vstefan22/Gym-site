from django.contrib import admin
from .models import MembershipPlan, MembershipPlanPrice


admin.site.register(MembershipPlan)
admin.site.register(MembershipPlanPrice)
