from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Room(models.Model):
    sender = models.ForeignKey(
        User,
        verbose_name=_("sender"), 
        on_delete=models.CASCADE,
        related_name="sender_room"
    )
    receiver = models.ForeignKey(
        User,
        verbose_name=_("receiver"), 
        on_delete=models.CASCADE,
        related_name="receiver_room"
    ) 
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    
    

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")

    def __str__(self):
        return f"{self.id}-{self.sender}-{self.receiver}"

    def get_absolute_url(self):
        return reverse("Room_detail", kwargs={"pk": self.pk})
    

class Chat(models.Model):
    room = models.ForeignKey(
        Room,
        verbose_name=_("room"),
        on_delete=models.CASCADE,
        related_name="chat_room"
    )
    sender = models.ForeignKey(
        User,
        verbose_name=_("sender"), 
        on_delete=models.CASCADE,
        related_name="sender_msg"
    )
    receiver = models.ForeignKey(
        User,
        verbose_name=_("receiver"), 
        on_delete=models.CASCADE,
        related_name="receiver_msg"
    ) 
    text = models.CharField(_("text"), max_length=300)
    date = models.DateTimeField(_("date"), auto_now_add=True)
    has_seen = models.BooleanField(_("has_seen"),default=False)
    

    class Meta:
        verbose_name = _("Chat")
        verbose_name_plural = _("Chats")

    def __str__(self):
        return f"{self.id}-{self.date}"

    def get_absolute_url(self):
        return reverse("Chat_detail", kwargs={"pk": self.pk})

