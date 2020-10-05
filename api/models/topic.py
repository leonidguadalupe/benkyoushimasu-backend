from django.db import models
from django.utils import timezone

from .base import BaseModel

class Topic(BaseModel):
    """
    Topics are generally things that can be studied in Japanese.
    """
    GENERAL = 'general'
    GRAMMAR = 'grammar'
    KANJI = 'kanji'
    KATAKANA = 'katakana'
    HIRAGANA = 'hiragana'
    VOCABULARY = 'vocabulary'
    COMPOUNDING = 'compounding'

    TOPIC_TYPES =(
        (GRAMMAR,GRAMMAR),
        (KANJI, KANJI),
        (KATAKANA, KATAKANA),
        (HIRAGANA, HIRAGANA),
        (VOCABULARY, VOCABULARY),
        (COMPOUNDING, COMPOUNDING)

    )

    topic_type = models.CharField(choices=TOPIC_TYPES, default='general', max_length=120)
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)

    # reading can be a phoneme if used in terms as hiragana or katakana topic
    reading = models.ManyToManyField('Reading', blank=True, related_name='topic_reading')
    source = models.ForeignKey(
        'Source',
        null=True, default=None, on_delete=models.CASCADE,
        related_name='topics', blank=True
    )

    # Flags for topics
    show_furigana = models.BooleanField(default=False)

    class Meta:
        verbose_name = "branch"
        verbose_name_plural = "branches"
        ordering = ['name', 'code']
        unique = ['code']
