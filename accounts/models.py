from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('CLIENTE', 'Cliente'),
        ('VENDEDOR', 'Vendedor'),
    )
    
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='CLIENTE',
        verbose_name='Rol de usuario'
    )
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono')
    address = models.TextField(blank=True, null=True, verbose_name='Dirección')

    def __str__(self):
        return f"{self.username} - ({self.get_role_display()})"