from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from indexer.models import Block, Transaction, Account
from ..custom_fields import BiggerIntegerField

# Create your tests here.


class BlockModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.account = Account.objects.create(
            hash='0x61c808d82a3ac53231750dadc13c777b59310bd9',
            account_type='EOA')

        cls.block_1 = Block.objects.create(
            hash='0xc0f4906fea23cf6f3cce98cb44e8e1449e455b28d684dfa9ff65426495584de6',
            parent_block=None,
            difficulty=49824742724615,
            extra_data='0xe4b883e5bda9e7a59ee4bb99e9b1bc',
            gas_limit=4712388,
            gas_used=21000,
            logs_bloom='0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            miner=cls.account,
            nonce='0x3b05c6d5524209f1',
            number=2000000,
            receipt_root='0x84aea4a7aad5c5899bd5cfc7f309cc379009d30179316a2a7baa4a2ea4a438ac',
            sha3_uncles='0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
            size=650,
            state_root='0x96dbad955b166f5119793815c36f11ffa909859bbfeb64b735cca37cbf10bef1',
            timestamp=timezone.make_aware(datetime.fromtimestamp(1470173578)),
            total_difficulty=44010101827705409388,
            transactions_root='0xb31f174d27b99cdae8e746bd138a01ce60d8dd7b224f7c60845914def05ecc58',
            transaction_count=100
        )

        cls.block_2 = Block.objects.create(
            hash='0xc0f4906fea23cf6f3cce98cb44e8e1449e455b28d684dfa9ff65426495584de6',
            parent_block=cls.block_1,
            difficulty=49824742724615,
            extra_data='0xe4b883e5bda9e7a59ee4bb99e9b1bc',
            gas_limit=4712388,
            gas_used=21000,
            logs_bloom='0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            miner=cls.account,
            nonce='0x3b05c6d5524209f1',
            number=2000000,
            receipt_root='0x84aea4a7aad5c5899bd5cfc7f309cc379009d30179316a2a7baa4a2ea4a438ac',
            sha3_uncles='0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
            size=650,
            state_root='0x96dbad955b166f5119793815c36f11ffa909859bbfeb64b735cca37cbf10bef1',
            timestamp=timezone.make_aware(
                datetime.fromtimestamp(1470173578)),
            total_difficulty=44010101827705409388,
            transactions_root='0xb31f174d27b99cdae8e746bd138a01ce60d8dd7b224f7c60845914def05ecc58',
            transaction_count=100
        )

    def test_parent_block_field_is_block(self):
        self.assertIsInstance(self.__class__.block_2.parent_block, Block)

    def test_parent_block_is_previousu_block(self):
        pass

    def test_difficulty_uses_BiggerIntegerField(self):
        self.assertIsInstance(Block._meta.get_field(
            'difficulty'), BiggerIntegerField)

    def test_total_difficulty_uses_BiggerIntegerField(self):
        self.assertIsInstance(Block._meta.get_field(
            'total_difficulty'), BiggerIntegerField)


class TransactionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.from_account = Account.objectscreate(
            hash='0xA1E4380A3B1f749673E270229993eE55F35663b4',
            account_type='eoa')

        cls.to_account = Account.objectscreate(
            hash='0x5DF9B87991262F6BA471F09758CDE1c0FC1De734',
            account_type='eoa')

        cls.miner = Account.objectscreate(
            hash='0x61c808d82a3ac53231750dadc13c777b59310bd9',
            account_type='EOA')

        cls.block = Block.objects.create(
            hash='0xc0f4906fea23cf6f3cce98cb44e8e1449e455b28d684dfa9ff65426495584de6',
            difficulty=49824742724615,
            parent_block=None,
            extra_data='0xe4b883e5bda9e7a59ee4bb99e9b1bc',
            gas_limit=4712388,
            gas_used=21000,
            logs_bloom='0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            miner=cls.miner,
            nonce='0x3b05c6d5524209f1',
            number=2000000,
            receipt_root='0x84aea4a7aad5c5899bd5cfc7f309cc379009d30179316a2a7baa4a2ea4a438ac',
            sha3_uncles='0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
            size=650,
            state_root='0x96dbad955b166f5119793815c36f11ffa909859bbfeb64b735cca37cbf10bef1',
            timestamp=timezone.make_aware(datetime.fromtimestamp(1470173578)),
            total_difficulty=44010101827705409388,
            transactions_root='0xb31f174d27b99cdae8e746bd138a01ce60d8dd7b224f7c60845914def05ecc58',
            transaction_count=100
        )

        cls.transaction = Transaction.objects.create(
            block=cls.block,
            from_address=cls.from_account,
            gas=21000,
            gas_price=None,
            hash='0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
            input='0x',
            max_fee_per_gas=2000000000,
            max_priority_fee_per_gas=1000000000,
            nonce=0,
            to_address=cls.to_account,
            transaction_index=0,
            value=31337,
        )


class AccountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.account = Account.objects.create(
            hash='0x61c808d82a3ac53231750dadc13c777b59310bd9',
            account_type='eoa'
        )

    def test_miner_max_length(self):
        self.assertEqual(42, Account._meta.get_field('hash').max_length)
