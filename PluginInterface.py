import abc


class PluginInterface(abc.ABC):
    @abc.abstractmethod
    def run(self, coffee_machine, **kwargs):
        raise NotImplementedError("Plugins must implement the run method.")