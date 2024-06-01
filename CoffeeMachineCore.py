class CoffeeMachineCore:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin
        print(f"Registered plugin: {self.plugins}")    
        
    def execute(self, name, **kwargs):
        if name in self.plugins:
            return self.plugins[name].run(self, **kwargs)
        else:
            print(f"No plugin registered under the name: {name}")
            return None

    def power_on(self):
        print("Coffee machine powered on.")

    def power_off(self):
        print("Coffee machine powered off.")

    def grind_beans(self):
        print("Grinding beans...")

    def heat_water(self):
        print("Heating water...")

    def brew_coffee(self):
        print("Brewing coffee...")