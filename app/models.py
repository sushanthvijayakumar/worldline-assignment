from django.db import models
# Create your models here.

CHOICES = (
    ("Vaccinated", "Vaccinated"),
    ("Not Vaccinated", "Not Vaccinated"),
)
class Record(models.Model):
    reg_no = models.CharField(max_length=200, unique=True, null=False)
    name = models.CharField(max_length=200, null=False)
    vaccine_status = models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = '1'
        )
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.reg_no 
