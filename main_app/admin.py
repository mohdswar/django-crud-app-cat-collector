from django.contrib import admin
from .models import Cat, Feeding, Toy  # Import the Toy model

admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)  # Register the Toy model