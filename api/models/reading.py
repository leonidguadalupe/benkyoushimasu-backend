from django.db import models

from .base import BaseModel

class Reading(BaseModel):
    KUNYOMI = 'kunyomi'
    ONYOMI = 'onyomi'
    VOCABULARY = 'vocabulary'

    READING_TYPES=(
        (KUNYOMI, KUNYOMI),
        (ONYOMI, ONYOMI),
        (VOCABULARY, VOCABULARY)
    )

    reading_type = models.CharField(choices=READING_TYPES, default='vocabulary', max_length=64)
    pronunciation = models.CharField(max_length=128, unique=True)
    furigana = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = "reading"
        verbose_name_plural = "readings"
        ordering = ['reading_type', 'pronunciation']

    def __unicode__(self):
        return u'%s' % (self.pronunciation)