from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE
    )
    is_online = models.BooleanField(_("is_online"))
    following = models.ManyToManyField(
        User,
        verbose_name=_("following"),
        blank=True,
        related_name="followings"
    )
    friends = models.ManyToManyField(
        User,
        verbose_name=_("friends"),
        blank=True,
        related_name="my_friends"
    )        
    bio = models.CharField(_("bio"), max_length=50,blank=True,null=True)
    date_of_birth = models.DateField(_("date_of_birth"))
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    image = models.ImageField(_("image"), upload_to="profile_pics",default="default.jpg",blank=True,null=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})

STATUS_CHOICES =(
    ('send','send'),
    ('accepted','accepted'),
)

class Relationship(models.Model):
    sender = models.ForeignKey(
        Profile,
        verbose_name=_("sender"),
        on_delete=models.CASCADE,
        related_name="friend_sender"   
    )
    receiver = models.ForeignKey(
        Profile,
        verbose_name=_("receiver"),
        on_delete=models.CASCADE,
        related_name="friend_receiver"   
    )
    status = models.CharField(_("status"), max_length=8,choices=STATUS_CHOICES)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("Relationship")
        verbose_name_plural = _("Relationships")

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

    def get_absolute_url(self):
        return reverse("Relationship_detail", kwargs={"pk": self.pk})
