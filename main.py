from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

me = Menu()
cofemaker = CoffeeMaker()
money = MoneyMachine()

while True:
  choice = input(f"What would you like ({me.get_items()}): ").lower()

  if choice == "off":
    break
  elif choice == "report":
    cofemaker.report()
    money.report()
  else:
    choice_info = me.find_drink(choice)
    if choice_info != None and cofemaker.is_resource_sufficient(choice_info) and money.make_payment(choice_info.cost):
        cofemaker.make_coffee(choice_info)
