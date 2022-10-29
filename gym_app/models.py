from distutils.command.upload import upload
from django.db import models

class MembershipPlan(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True, upload_to = 'images/')
    stripe_product = models.CharField(max_length = 150)

    def __str__(self):
        return self.name


class MembershipPlanPrice(models.Model):
    membership_plan = models.ForeignKey(MembershipPlan, related_name='plan', on_delete = models.CASCADE)
    price = models.IntegerField(null = False, blank = False)
    stripe_price = models.CharField(max_length = 150)
