from django.core.management.base import BaseCommand, CommandError
from ...tasks import index_blockchain


class Command(BaseCommand):
    help = 'Starts indexing the blockchain'

    def add_arguments(self, parser):
        parser.add_argument('start_block', nargs='?', type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Started indexing ...'))
        index_blockchain.delay(options['start_block'])
        self.stdout.write(self.style.SUCCESS('Finished indexing :)'))
