from django.db import models
from users.models import Users

# Create your models here.
class Service(models.Model):
    service_name = models.CharField('Nombre de servicio', max_length=200)

    def __str__(self):
        return self.service_name



class Payment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_date = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return f"{self.user.realname} - {self.service.service_name} - {self.monto}"
