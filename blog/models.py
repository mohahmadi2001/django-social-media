from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



# Create your models here.

class Post(models.Model):
    title = models.CharField(_("title"), max_length=10)
    content = RichTextField(_("content"),blank=True,null=True)
    date_posted = models.DateTimeField(_("post date"),auto_now_add=True)
    date_updated = models.DateTimeField(_("update date"), auto_now=True)
    author = models.ForeignKey(
        User,
        verbose_name=_("author"),
        on_delete=models.CASCADE,
        related_name="post"
    )
    likes = models.ManyToManyField(
        User,
        verbose_name=_("like"),
        blank=True,
        related_name="post_like"
    )
    saves = models.ManyToManyField(
        User,
        verbose_name=_("save"),
        blank=True,
        related_name="post_save"
    )
    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.all().count()
    
    def total_save(self):
        return self.saves.all().count()
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})


class Comment(models.Model):
    post =models.ForeignKey(
        Post,
        verbose_name=_("post"),
        on_delete=models.CASCADE,
        related_name="post_comment"    
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name="user_comment"
    )
    body = models.TextField(_("body"),max_length=200,default=" ")
    date_added = models.DateTimeField(_("comment date"), auto_now_add=True)
    likes = models.ManyToManyField(
        User, 
        verbose_name=_("like"),
        blank=True,
        related_name="like"    
    )
    reply = models.ForeignKey(
        "self",
        verbose_name=_("reply"),
        null=True,
        on_delete=models.CASCADE,
        related_name="comment_reply"
    )
    

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.name
    
    def get_comments_count(self):
        return self.id.count()
    
    def get_comments(self):
        return f"{self.user.username}-{self.body}"
    
    def total_comments_like(self):
        return self.likes.count() 
    
    def total_reply_counts(self):
        return self.reply.count()

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})


   