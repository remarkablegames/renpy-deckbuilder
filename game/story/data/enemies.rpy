default enemies = Enemies()


init python:
    class Enemies:
        # Names that are mapped to their respective images.
        # E.g., name "Boy 1" -> image "boy_1".
        NAMES = ["Boy", "Girl", "Guy"]

        # Enemy yalign position in battle.
        YALIGN = 1.0


        def __init__(self) -> None:
            self.enemies = []
            self.count = 0


        def generate(self, enemies: list) -> None:
            """
            Generate enemies.
            """
            self.enemies = []
            self.count = len(enemies)

            for enemy in enemies:
                self.enemies.append(RPGCharacter(**enemy))


        def show(self) -> None:
            """
            Show enemies.
            """
            for index, enemy in enumerate(self.enemies):
                xalign_position = self.xalign_position(enemy)
                renpy.show_screen(f"enemy_stats{index}", enemy, xalign_position)
                renpy.show(enemy.image, at_list=[position(xalign_position)], layer=LAYER_ENEMIES)

            renpy.with_statement(dissolve)


        def hide(self, enemy: RPGCharacter) -> None:
            """
            Hide enemy.
            """
            renpy.hide(enemy.image, layer=LAYER_ENEMIES)
            renpy.hide_screen(f"enemy_stats{enemies.index(enemy)}")
            renpy.transition(dissolve, layer=LAYER_ENEMIES)


        def get(self, enemy_id: str) -> RPGCharacter:
            """
            Get enemy by id.
            """
            return find(self.enemies, {"id": enemy_id})


        def index(self, enemy: RPGCharacter) -> int:
            """
            Get enemy index.
            """
            return self.enemies.index(enemy)


        def alive(self) -> list:
            """
            Get alive enemies.
            """
            return list(filter(lambda enemy: enemy.health > 0, self.enemies))


        def dead(self) -> bool:
            """
            Whether enemies are dead.
            """
            return not bool(len(self.alive()))


        def xalign_position(self, enemy: RPGCharacter) -> float:
            """
            Get enemy xalign position.
            """
            count = self.count
            index = self.enemies.index(enemy)

            if count == 1:
                xalign_position = 0.5

            elif count == 2:
                if index == 0:
                    xalign_position = 0.25
                elif index == 1:
                    xalign_position = 0.75

            elif count == 3:
                if index == 0:
                    xalign_position = 0.1
                elif index == 1:
                    xalign_position = 0.5
                elif index == 2:
                    xalign_position = 0.9

            elif count == 4:
                if index == 0:
                    xalign_position = 0.05
                elif index == 1:
                    xalign_position = 0.35
                elif index == 2:
                    xalign_position = 0.65
                elif index == 3:
                    xalign_position = 0.95

            elif count == 5:
                if index == 0:
                    xalign_position = 0
                elif index == 1:
                    xalign_position = 0.25
                elif index == 2:
                    xalign_position = 0.5
                elif index == 3:
                    xalign_position = 0.75
                elif index == 4:
                    xalign_position = 1.0

            return xalign_position


        def turn(self) -> None:
            """
            Enemy turn.
            """
            for enemy in self.alive():
                if enemy.stunned:
                    narrator(f"{enemy.name} is stunned!")
                    continue

                enemy.turn_rng()

                if enemy.heal_value and enemy.health < enemy.health_max and renpy.random.random() < 0.5:
                    narrator(f"{enemy.name} healed {enemy.heal_value} health.")
                    enemy.heal(enemy.heal_value)
                else:
                    narrator(f"{enemy.name} dealt {enemy.attack} damage to you.")
                    renpy.with_statement(vpunch)
                    player.hurt(enemy.attack)

                    if player.health <= 0:
                        renpy.jump("lose")

            self.end_turn()


        def end_turn(self) -> None:
            """
            Enemy end turn.
            """
            for enemy in self.alive():
                enemy.stunned = False
