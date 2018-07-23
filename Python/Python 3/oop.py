# #
# oop.py
#
# Leonardo Vencovsky (https://github.com/LeoVen)
#
# 23/07/2018
#
# #

# SOLID
# S - Single responsibility principle
# O - Open/closed principle
# L - Liskov substitution principle
# I - Interface segregation principle
# D - Dependency inversion principle

# Getters and Setters
# Private attributes and methods
# Static method

from random import random, randint


class ItemAttack:

	def __init__(self, damage, crit_chance):
		self.damage = damage
		self.crit_chance = crit_chance


class ItemDefense:

	def __init__(self, protection):
		self.protection = protection


class Soldier:

	def __init__(self, name, health, item_attack, item_defense):
		self.name = name
		self.__health = health # private attribute
		self.item_attack = item_attack
		self.item_defense = item_defense

	# Getter
	@property
	def name(self):
		return self.__name.title()

	# Setter
	@name.setter
	def name(self, name):
		self.__name = name

	# Private method
	def __attack(self):
		r = random()
		if r < self.item_attack.crit_chance:
			return self.item_attack.damage * 2
		return self.item_attack.damage

	def defend(self, attacker):
		damage = attacker.__attack() - self.item_defense.protection
		damage = 0 if damage < 0 else damage
		self.__health -= damage

	def print(self):
		print("{} status:".format(self.name))
		print("Health : {}".format(self.__health))
		print("Weapon : [ {} / {} ]".format(self.item_attack.damage, self.item_attack.crit_chance))
		print("Defense: {}".format(self.item_defense.protection))
		print(" ")

	def is_alive(self):
		return self.__health > 0

	def is_dead(self):
		return self.__health <= 0 
	
	@staticmethod
	def class_name():
		return "Soldier"


def battle(soldier_1, soldier_2):

	i = 0

	while soldier_1.is_alive() and soldier_2.is_alive() > 0 and i < 100:
		soldier_1.print()
		soldier_2.print()

		#print("Press enter to attack")
		#input()

		soldier_1.defend(soldier_2)
		soldier_2.defend(soldier_1)

		i += 1

	print("+--------------------------------------------------+")
	print("|                      Results                     |")
	print("+--------------------------------------------------+")
	print(" ")

	soldier_1.print()
	soldier_2.print()

	if ( ( soldier_1.is_dead() and soldier_2.is_dead() ) or i >= 100):
		print("+--------------------------------------------------+")
		print("|                       Draw                       |")
		print("+--------------------------------------------------+")
	elif(soldier_1.is_dead() and soldier_2.is_alive()):
		print("+--------------------------------------------------+")
		print("|                     Victory!                     |")
		print("+--------------------------------------------------+")
		print("{} {} won!".format(Soldier.class_name(), soldier_2.name))
	elif (soldier_1.is_alive() and soldier_2.is_dead()):
		print("+--------------------------------------------------+")
		print("|                     Victory!                     |")
		print("+--------------------------------------------------+")
		print("{} {} won!".format(Soldier.class_name(), soldier_1.name))


def main():
	print("OOP learning")

	attack_items = [ItemAttack(15, 0.5), ItemAttack(30, 0.15), ItemAttack(10, 0.9), ItemAttack(20, 0.3), ItemAttack(40, 0.1)]
	defense_items = [ItemDefense(10), ItemDefense(15), ItemDefense(20), ItemDefense(25), ItemDefense(30)]

	length = len(attack_items) - 1

	soldier_1 = Soldier("julius caesar", randint(50, 100), attack_items[randint(0, length)], defense_items[randint(0, length)])
	soldier_2 = Soldier("alexander", randint(50, 100), attack_items[randint(0, length)], defense_items[randint(0, length)])

	battle(soldier_1, soldier_2)


if __name__ == '__main__':
	main()
