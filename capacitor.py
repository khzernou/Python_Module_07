from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability
from ex0.factory import CreatureFactory
from ex0.creature import Creature


def test_healing_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    for label in ("base", "evolved"):
        print(f" {label}:")
        if label == "base":
            creature: Creature = factory.create_base()
        else:
            creature = factory.create_evolved()
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transform_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    for label in ("base", "evolved"):
        print(f" {label}:")
        if label == "base":
            creature: Creature = factory.create_base()
        else:
            creature = factory.create_evolved()
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    test_healing_factory(healing_factory)
    print()
    transform_factory = TransformCreatureFactory()
    test_transform_factory(transform_factory)
