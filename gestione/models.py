from django.db import models

# Create your models here.

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(TimestampModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class City(TimestampModel):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
        return f"{self.name} ({self.department.name})"

class District(TimestampModel):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="districts")

    def __str__(self):
        return f"{self.name} ({self.city.name})"

class Member(TimestampModel):
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="members"
    )  # Lien obligatoire avec une ville
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True, blank=True, related_name="members"
    )  # Lien facultatif avec un quartier

    def __str__(self):
        return f"{self.firstName} {self.name}"