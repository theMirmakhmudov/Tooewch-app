from django.db import models
from django.utils import timezone

class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    user_id = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.phone})"


class Procedure(models.Model):
    PROCEDURE_CHOICES = [
        ('tish_davolash', 'Tish davolash'),
        ('tish_oldirish', 'Tish oldirish'),
        ('tish_qoyish', 'Tish qo‘yish'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='procedures')
    procedure_type = models.CharField(max_length=50, choices=PROCEDURE_CHOICES)
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_procedure_type_display()} - {self.patient.full_name} - {self.date}"


class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.amount} so'm - {self.date}"


class ReminderLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reminders')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Eslatma: {self.patient.full_name} - {self.sent_at.strftime('%Y-%m-%d %H:%M')}"
