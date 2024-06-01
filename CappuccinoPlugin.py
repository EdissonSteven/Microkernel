from PluginInterface import PluginInterface

class CappuccinoPlugin(PluginInterface):
    def run(self, coffee_machine, **kwargs):
        coffee_machine.grind_beans()
        coffee_machine.heat_water()
        print("Brewing a cappuccino...")
        print("Frothing milk...")