from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    nome = models.CharField(max_length=20, blank=False, null=False)
    slug = models.SlugField(max_length=20, unique=True, blank=True, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.nome}"

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=False)
    picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.user.username} ({self.role.nome})"
