from dataclasses import dataclass


@dataclass
class Damage:
	physical: int
	magical: int
	fire: int
	cold: int
	poison: int
	electric: int
	time: int
