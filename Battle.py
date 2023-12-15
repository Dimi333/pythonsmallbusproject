""" Riadenie bitiek """

from Damage import Damage
from Mobile import Mobile


class Battle:
	amount: Damage
	dealer: Mobile
	target: Mobile

	def __init__(self, damage: Damage, dealer: Mobile, target: Mobile):
		self.amount = damage
		self.dealer = dealer
		self.target = target

	def deal(self):
		self.target.damage(self.amount.physical)
