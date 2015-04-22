from django.db import models


class Event(models.Model):

    label = models.CharField(
        max_length=100,
    )

    start_date = models.DateTimeField()

    end_date = models.DateTimeField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['label']


class AccountGroup(models.Model):

    label = models.CharField(
        max_length=100,
    )

    class Meta:
        ordering = ['label']


class Account(models.Model):

    event = models.ForeignKey(
        Event,
    )

    username = models.CharField(
        max_length=32,
    )

    groups = models.ManyToManyField(
        AccountGroup,
        blank=True,
    )

    class Meta:
        ordering = ['username']


class TermGroup(models.Model):

    label = models.CharField(
        max_length=100,
    )

    class Meta:
        ordering = ['label']


class Term(models.Model):

    event = models.ForeignKey(
        Event,
    )

    string = models.CharField(
        max_length=100,
    )

    groups = models.ManyToManyField(
        TermGroup,
        blank=True,
    )

    class Meta:
        ordering = ['string']


class Tweet(models.Model):

    event = models.ForeignKey(
        Event,
    )

    content = models.TextField()

    link = models.URLField()

    account = models.ForeignKey(
        Account,
    )


class TermMatch(models.Model):

    tweet = models.ForeignKey(
        Tweet,
    )

    term = models.ForeignKey(
        Term,
    )
