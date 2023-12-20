from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
    )
    title = models.CharField(max_length=120)
    body = models.TextField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación de la publicación.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última modificación de la publicación.")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', help_text="Estado de la publicación. Puede ser 'draft' o 'published'.")

    def __str__(self):
        return self.title
