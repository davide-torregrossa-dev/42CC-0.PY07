from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]

FACTORY_NAMES: dict[type[CreatureFactory], str] = {
    FlameFactory: "Flameling",
    AquaFactory: "Aquabub",
    HealingCreatureFactory: "Healing",
    TransformCreatureFactory: "Transform",
}


def label(opponent: Opponent) -> str:
    factory, strategy = opponent
    factory_name = FACTORY_NAMES.get(type(factory), type(factory).__name__)
    strategy_name = type(strategy).__name__.removesuffix("Strategy")
    return f"({factory_name}+{strategy_name})"


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]
            try:
                fighter_a = factory_a.create_base()
                fighter_b = factory_b.create_base()
            except Exception as error:
                print(f"Factory error, aborting tournament: {error}")
                return
            print()
            print("* Battle *")
            print(fighter_a.describe())
            print(" vs.")
            print(fighter_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(fighter_a)
                strategy_b.act(fighter_b)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def run(index: int, title: str, opponents: list[Opponent]) -> None:
    if index > 0:
        print()
    print(f"Tournament {index} ({title})")
    print(" [ " + ", ".join(label(o) for o in opponents) + " ]")
    battle(opponents)


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    run(0, "basic", [(flame, normal), (healing, defensive)])
    run(1, "error", [(flame, aggressive), (healing, defensive)])
    run(
        2,
        "multiple",
        [(aqua, normal), (healing, defensive), (transform, aggressive)],
    )


if __name__ == "__main__":
    main()
