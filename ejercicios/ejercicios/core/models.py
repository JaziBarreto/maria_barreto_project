from django.db import models

class Usuario(models.Model):
    full_name = models.CharField(max_length=145)
    age= models.IntegerField()
    weight= models.IntegerField(null=True)
    image = models.ImageField(upload_to='perfiles/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"({self.id}) {self.full_name}"
    
    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural = "Usuarios"