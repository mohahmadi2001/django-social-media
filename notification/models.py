from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        (1,"Like"),
        (2,"Follow"),
        (3,"Comment"),
        (4,"Reply"),
        (5,"Like-Comment"),
        (6,"Like-Reply")
    )
    post = models.ForeignKey(
        "blog.Post",
        verbose_name=_("post"),
        on_delete=models.CASCADE,
        related_name="post_notifications"   
    )
    sender = models.ForeignKey(
        User,
        verbose_name=_("sender"), 
        on_delete=models.CASCADE,
        related_name="notify_senders"
    )
    receiver = models.ForeignKey(
        User,
        verbose_name=_("receiver"), 
        on_delete=models.CASCADE,
        related_name="notify_receivers"
    )
    text_preview = models.CharField(_("text_preview"), max_length=120)
    is_seen = models.BooleanField(_("is_seen"),default=False)
    date = models.DateTimeField(_("notify_date"), auto_now_add=True)
    notification_type = models.IntegerField(_("notify_type"),choices=NOTIFICATION_TYPES)
    
    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    def __str__(self):
        return f"{self.id}-{self.sender}-{self.receiver}-{self.notification_type}"

    def get_absolute_url(self):
        return reverse("Notification_detail", kwargs={"pk": self.pk})
