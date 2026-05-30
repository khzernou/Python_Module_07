from ex0 import FlameFactory, AquaFactory
from ex0 import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    factory_a: CreatureFactory, factory_b: CreatureFactory
) -> None:
    print("Testing battle")
    base_a = factory_a.create_base()
    base_b = factory_b.create_base()
    print(base_a.describe())
    print("vs")
    print(base_b.describe())
    print("fight!")
    print(base_a.attack())
    print(base_b.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)

    test_battle(flame_factory, aqua_factory)
