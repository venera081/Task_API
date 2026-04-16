from django.db import models

class Notification(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notitfications"
        