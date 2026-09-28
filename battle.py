from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    try:
        base = factory.create_base()
        evolved = factory.create_evolved()
    except Exception as error:
        print(f"Factory error: {error}")
        return
    for creature in (base, evolved):
        print(creature.describe())
        print(creature.attack())
    print()



def test_battle(first: CreatureFactory, second: CreatureFactory) -> None:
    print("Testing battle")
    try:
        fighter_a = first.create_base()
        fighter_b = second.create_base()
    except Exception as error:
        print(f"Factory error: {error}")
        return
    print(fighter_a.describe())
    print("         vs.")
    print(fighter_b.describe())
    print("         fight!!!")
    print(fighter_a.attack())
    print(fighter_b.attack())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    test_factory(aqua)
    test_battle(flame, aqua)


if __name__ == "__main__":
    main()