from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class FriendList(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="user"
    )
    friend = models.ManyToManyField(
        User,
        verbose_name=_("friend"),
        blank=True,
        related_name="friends",
    )
    

    class Meta:
        verbose_name = _("FriendList")
        verbose_name_plural = _("FriendLists")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("FriendList_detail", kwargs={"pk": self.pk})
    

class FriendRequest(models.Model):
    sender = models.ForeignKey(
        User,
        verbose_name=_("sender"), 
        on_delete=models.CASCADE,
        related_name="sender"
    )
    receiver = models.ForeignKey(
        User,
        verbose_name=_("receiver"), 
        on_delete=models.CASCADE,
        related_name="receiver"
    ) 
    date = models.DateTimeField(_("date"), auto_now_add=True)
    is_active = models.BooleanField(_("is active"),null=True,blank=True,default=True)
    

    class Meta:
        verbose_name = _("FriendRequest")
        verbose_name_plural = _("FriendRequests")

    def __str__(self):
        return self.sender.username

    def get_absolute_url(self):
        return reverse("FriendRequest_detail", kwargs={"pk": self.pk})

