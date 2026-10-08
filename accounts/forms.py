from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistroClienteForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'CLIENTE'   # siempre es cliente, el usuario nunca elije 
        if commit:
            user.save()
        return user