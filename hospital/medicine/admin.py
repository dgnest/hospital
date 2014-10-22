from django.contrib import admin
from .models import Medicine
from .models import MedicinePerConsultation


admin.site.register(Medicine)
admin.site.register(MedicinePerConsultation)
