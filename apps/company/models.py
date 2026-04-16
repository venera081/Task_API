from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='employees'
                                )

    def str(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

        