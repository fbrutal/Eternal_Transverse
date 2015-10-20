from django.db import models

# Create your models here.
class SignUp(models.Model):
    class Meta():
        db_table = 'SighUp'

    email = models.EmailField(help_text='A valid email address, please.')
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email