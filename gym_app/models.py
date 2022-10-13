from django.db import models

class MembershipPlan(models.Model):
    name = models.CharField(max_length = 100)
    stripe_product_id = models.CharField(max_length = 150)

    def __str__(self):
        return self.name


class MembershipPlanPrice(models.Model):
    membership_plan = models.ForeignKey(MembershipPlan, on_delete = models.CASCADE)
    price = models.IntegerField()
    stripe_price_id = models.CharField(max_length = 150)
