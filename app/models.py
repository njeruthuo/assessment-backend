from django.db import models

# Create your models here.


class Asset(models.Model):
    """
    You can add all the fields required by a car
    """
    name = models.CharField(max_length=200)
    reg = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class StatusChoices(models.TextChoices):
    ACTIVE = 'Active', 'Active'
    YARD = 'Yard', 'Yard'
    GARAGE = 'Garage', 'Garage'


class Status(models.Model):

    vehicle = models.OneToOneField(Asset, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=StatusChoices.choices)

    def __str__(self) -> str:
        return f'{self.vehicle.name} - {self.status}'

    class Meta:
        verbose_name_plural = 'Statuses'

        """Indexing a db helps in querying large databases"""
        indexes = [models.Index(fields=['vehicle']),
                   models.Index(fields=['status']),
                   models.Index(fields=['status', 'vehicle'])]
