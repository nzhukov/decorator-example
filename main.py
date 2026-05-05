from decorator import *
# здесь будет вызов кода из модуля decorator.py

# Клиентский код – использует компонент без знания о наличии/отсутствии декораторов
def client_code(component: Component) -> None:
    print(f"Результат: {component.operation()}")


if __name__ == "__main__":

    # Создаём базовый компонент
    simple = ConcreteComponent()
    print("1. Базовый компонент:")
    client_code(simple)

    # Декорируем его декоратором A
    decorator_a = ConcreteDecoratorA(simple)
    print("\n2. Компонент, обёрнутый в DecoratorA:")
    client_code(decorator_a)

    # Декорируем декоратором B (можно поверх уже декорированного)
    decorator_b = ConcreteDecoratorB(decorator_a)
    print("\n3. Компонент, обёрнутый сначала в DecoratorA, затем в DecoratorB:")
    client_code(decorator_b)

    # Декорируем декоратором C поверх всего
    decorator_c = ConcreteDecoratorC(decorator_b)
    print("\n4. Двойная обёртка (A -> B -> C):")
    client_code(decorator_c)

    # Можно также использовать другой порядок обёртки
    print("\n5. Другой порядок: B -> C -> A")
    other = ConcreteDecoratorA(ConcreteDecoratorC(ConcreteDecoratorB(simple)))

    
    client_code(other)
