from django.db import models
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

from numconv import NumConv


class ShortLink(models.Model):
    """
    Short Link model
    """

    original_url = models.URLField(_('Original URL'), unique=True)
    hash = models.CharField(_(' URL Hash'), max_length=50, null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('ShortLink')
        verbose_name_plural = _('ShortLinks')

    def get_absolute_url(self):
        return reverse('shortener:go', args=[self.hash])

    def __unicode__(self):
        return "({}) {}".format(self.id, self.original_url)


def update_hash(sender, instance, **kwargs):
    if not instance.hash:
        instance.hash = NumConv(64).int2str(instance.id)
        instance.save()

post_save.connect(update_hash, sender=ShortLink, dispatch_uid="update_hash_link")
