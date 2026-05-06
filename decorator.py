from abc import ABC, abstractmethod

# 1. Абстрактный компонент – интерфейс, общий для всех декорируемых объектов
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# 2. Конкретный компонент – исходный объект, который мы будем декорировать
class ConcreteComponent(Component):
    def operation(self) -> str:
        import os
        # Базовое поведение (очень простое, без логики)
        return "BaseOperation, SUPER_SECRET_ENV IS: " + str(os.getenv('SUPER_SECRET_KEY'))  

# 3. Абстрактный декоратор – содержит ссылку на компонент и делегирует ему вызов
class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component  # Обёрнутый объект

    def operation(self) -> str:
        # Делегирование базовому компоненту (может быть переопределено в наследниках)
        return self._component.operation()

# 4. Конкретный декоратор A – добавляет поведение ДО вызова базовой операции
class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        # Добавляем "обёртку" с одной стороны
        return f"DecoratorA({self._component.operation()})"

# 5. Конкретный декоратор B – добавляет поведение ПОСЛЕ вызова базовой операции
class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        # Можно добавить логику до, после или вокруг вызова
        # Здесь добавим только после
        return f"{self._component.operation()}[DecoratorB]"

# 6. Конкретный декоратор C – комбинирует добавления с обеих сторон
class ConcreteDecoratorC(Decorator):
    def operation(self) -> str:
        # Добавляем и префикс, и суффикс
        return f"Pre_{self._component.operation()}_Post"
    