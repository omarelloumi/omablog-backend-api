from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_img",blank=True,null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    CATEGORY = (
                ("Frontend", "Frontend"),
                ("Backend", "Backend"),
                ("Fullstack", "Fullstack"),
                ("Design", "Design"),
                ("Blockchain", "Blockchain")
        )

    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="blogs", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    category = models.CharField(max_length=255, choices=CATEGORY, null=True)
    featured_image = models.ImageField(upload_to="blog_img", blank=True, null=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        num = 1

        while Blog.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{num}'
            num += 1
        self.slug = slug

        if not self.published_at and not self.is_draft:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)