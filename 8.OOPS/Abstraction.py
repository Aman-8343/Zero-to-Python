#hiding internal details and showing only essential features

from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class lion(Animal):
    def make_sound(self):
        print("roar")


l1=lion();
l1.make_sound()