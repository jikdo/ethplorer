from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from indexer.models import Block, Transaction
from ..custom_fields import BiggerIntegerField

# Create your tests here.


class BlockModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.block = Block.objects.create(
            hash='0xc0f4906fea23cf6f3cce98cb44e8e1449e455b28d684dfa9ff65426495584de6',
            difficulty=49824742724615,
            extra_data='0xe4b883e5bda9e7a59ee4bb99e9b1bc',
            gas_limit=4712388,
            gas_used=21000,
            logs_bloom='0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            miner='0x61c808d82a3ac53231750dadc13c777b59310bd9',
            nonce='0x3b05c6d5524209f1',
            number=2000000,
            parent_hash='0x57ebf07eb9ed1137d41447020a25e51d30a0c272b5896571499c82c33ecb7288',
            receipt_root='0x84aea4a7aad5c5899bd5cfc7f309cc379009d30179316a2a7baa4a2ea4a438ac',
            sha3_uncles='0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
            size=650,
            state_root='0x96dbad955b166f5119793815c36f11ffa909859bbfeb64b735cca37cbf10bef1',
            timestamp=timezone.make_aware(datetime.fromtimestamp(1470173578)),
            total_difficulty=44010101827705409388,
            transactions_root='0xb31f174d27b99cdae8e746bd138a01ce60d8dd7b224f7c60845914def05ecc58',
        )

    def test_miner_max_length(self):
        self.assertEqual(42, Block._meta.get_field('miner').max_length)

    def test_difficulty_uses_BiggerIntegerField(self):
        self.assertIsInstance(Block._meta.get_field('difficulty'), BiggerIntegerField)
        
    def test_total_difficulty_uses_BiggerIntegerField(self):
        self.assertIsInstance(Block._meta.get_field('total_difficulty'), BiggerIntegerField)