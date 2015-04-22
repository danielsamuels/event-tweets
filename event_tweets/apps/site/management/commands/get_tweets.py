from django.core.management.base import BaseCommand
from django.db.models import Q
from django.utils.timezone import now

from ...models import Event

import os
from twython import Twython

twitter = Twython(
    os.environ.get('APP_KEY'),
    os.environ.get('APP_SECRET'),
    os.environ.get('OAUTH_TOKEN'),
    os.environ.get('OAUTH_TOKEN_SECRET')
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Get all active jobs.
        events = Event.objects.filter(
            Q(start_date__lte=now()),
            Q(end_date__isnull=True) | Q(end_date__gt=now())
        )

        for event in events:
            # Get the accounts.
            for account in event.account_set.all():
                # Get the tweets. We need to go back in time, as well as forwards.

                # Go backwards.
                timeline = twitter.get_user_timeline(
                    screen_name=account.username,
                    count=200,
                    trim_user=True,
                    exclude_replies=True,
                    contributor_details=False,
                    include_rts=False,
                )

                for tweet in timeline:
                    print tweet
