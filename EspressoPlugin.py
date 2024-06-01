from PluginInterface import PluginInterface

class EspressoPlugin(PluginInterface):
    def run(self, coffee_machine, **kwargs):
        coffee_machine.grind_beans()
        coffee_machine.heat_water()
        print("Brewing an espresso...")