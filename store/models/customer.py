from django.db import  models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        return Customer.objects.filter(email=self.email).exists()

    def __str__(self):
        return self.first_name

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
