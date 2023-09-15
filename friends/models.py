from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import transaction

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
    
    def add_friend(self,account):
        if not account in self.friend.all():
            self.friend.add(account)
            self.save()
    
    def remove_friend(self,account):
        if account in self.friend.all():
            self.friend.remove(account)
            self.save()
            
    def unfriend(self,remove):
        remover_friends_list = self
        remover_friends_list.remove_friend(remove)
        
        friends_list = FriendList.objects.get(user=remove)
        friends_list.remove_friend(self.user)
        
    def is_mutual_friends(self,friend):
        if friend in self.friend.all():
            return True
        return False

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
    
    @transaction.atomic
    def accept(self):
        # Update the receiver's friend list
        receiver_friend_list, _ = FriendList.objects.get_or_create(user=self.receiver)
        receiver_friend_list.add_friend(self.sender)

        # Update the sender's friend list
        sender_friend_list, _ = FriendList.objects.get_or_create(user=self.sender)
        sender_friend_list.add_friend(self.receiver)

        # Deactivate the friend request
        self.is_active = False
        self.save()

    def decline(self):
        self.is_active = False
        self.save()
    
    def cancel(self):
        self.is_active = False
        self.save()
    
    def get_absolute_url(self):
        return reverse("FriendRequest_detail", kwargs={"pk": self.pk})

