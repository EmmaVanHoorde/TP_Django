from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.

#ef validate_image(fieldfile_obj):

def avatar_filename(instance, filename):
    fname, dot, extension = filename.rpartition('.')
    slug = instance.user.username
    path='gallery/'
    return '%s%s.%s' % (path, slug, extension)

class Member(models.Model):

    user = models.OneToOneField(
        User,
        verbose_name="utilisateur"
    )
    avatar = models.ImageField(
        verbose_name="avatar member",
        # upload_to=avatar_filename,
        # validators=[validate_image],
        null=True,
        blank=True
    )
    settings = models.ForeignKey(
        'Setting',
        verbose_name= "Paramètres",
        null=True,
        blank=True
    )
    class Meta:
        app_label = "todo"
    def __str__(self):
        return str(self.user.username)

class Parano(models.Model):
    created_by = models.ForeignKey(
        "Member",
        verbose_name="Crée par",
        related_name="%(app_label)s_%(class)s_modificator"
    )
    modified_by = models.ForeignKey(
        "Member",
        verbose_name="Modifié par",
        related_name="%(app_label)s_%(class)s_creator"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Crée le",
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Modifié le",
    )
    class Meta:
        abstract = True
        app_label = "todo"

class Setting(Parano, models.Model):
    notify_mail = models.BooleanField(
        verbose_name="Notifications par Email ?",
        default=True,
        blank=True
    )
    notify_sms = models.BooleanField(
        verbose_name="Notifications par sms ?",
        default=True,
        blank=True
    )
    class Meta:
        app_label = "todo"

# class Group(Parano, models.Model):
#     name = CharField(
#         verbose_name="",
#     )


class Task(Parano, models.Model):
    status_choices = (
        (None, '---'),
    )
    name = models.CharField(
        max_length=60,
        verbose_name="Nom"
    )
    assigned_to = models.ForeignKey(
        Member,
        verbose_name="Assigné à",
        related_name="tasks_assigned",
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        null=True,
        blank=True
    )
    due_date = models.DateTimeField(
        verbose_name="Fin prévue le",
        null=True,
        blank=True,
        default= timezone.now() + timedelta(1)
    )
    completed = models.BooleanField(
        verbose_name="Tache terminée ? ",
        default=False,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=None,
        null=True,
        blank=True
    )
    # list = models.ForeignKey(
    #     Group,
    #     verbose_name="Liste",
    #     related_name="tasks"
    # )

    class Meta:
        app_label = "todo"
        ordering = ['-created_at']

    # def __str__(self):
    #     return str(self.name)
    #
    # def get_absolute_url(self):
    #     return reverse_lazy('todo:tasks:retrieve', kwargs={'pk': self.id})
