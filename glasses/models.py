from django.db import models

class Eyewear(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    frame_material = models.CharField(max_length=100)
    lens_material = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='eyewear_images/', blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Glasses"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.brand} - {self.name} ({self.price} $.)"


# Create your models here.
