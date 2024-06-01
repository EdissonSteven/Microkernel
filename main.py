from CoffeeMachineCore import CoffeeMachineCore
from EspressoPlugin import EspressoPlugin
from CappuccinoPlugin import CappuccinoPlugin
from PluginInterface import PluginInterface


def main():
    # Create the core system (microkernel)
    coffee_machine = CoffeeMachineCore()
    
    # Register plugins (extended functionalities)
    coffee_machine.register_plugin("espresso", EspressoPlugin())
#    coffee_machine.register_plugin("cappuccino", CappuccinoPlugin())
    
   
    # Use the core system
#    coffee_machine.power_on()
    
    # Execute plugins
#    coffee_machine.execute("espresso")
#    coffee_machine.execute("cappuccino")
    
    # Try to execute a non-registered plugin
#    coffee_machine.execute("latte")
    
#    coffee_machine.power_off()

if __name__ == "__main__":
    main()

