from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
class Encnender(Command):
    def execute(self)-> None:
        print("El robot esta encendiendo...")

class Apagar(Command):
    def execute(self) -> None:
        print("El robot esta apagandoce...")

class Hablar(Command):
    def execute(self) -> None:
        print("EL robot esta hablando")

class Dormir(Command):

    def execute(self) -> None:
        print("El robot esta Durmiendo...")

class Robot:
    def encender(self, comando):
        self.comando_encender = comando

    def apagar(self, comando):
        self.comando_apagar = comando

    def hablar(self, comando):
        self.comando_hablar = comando

    def dormir(self, comando):
        self.comando_dormir = comando