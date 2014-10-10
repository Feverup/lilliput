from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


class ShortLink(models.Model):
    """
    Short Link model
    """

    original_url = models.URLField(_('Original URL'), max_length=2000, unique=True)
    hash = models.CharField(_(' URL Hash'), max_length=50, null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('ShortLink')
        verbose_name_plural = _('ShortLinks')

    def get_absolute_url(self):
        if self.hash:
            return reverse('shortener:go', args=[self.hash])
        else:
            return ""

    def __unicode__(self):
        return "({}) {}".format(self.id, self.original_url)
