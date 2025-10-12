default levels = Levels()


init python:
    from json import load


    class Levels:
        battle = False
        level = 0
        levels = load(renpy.file("story/data/levels.json"))


        def get(self) -> dict:
            """
            Get level data.
            """
            try:
                return self.levels[str(self.level)]
            except KeyError:
                return self.generate()


        def generate(self) -> dict:
            """
            Generate random enemies.
            """
            level = {"enemies": []}
            names = Enemies.NAMES.copy()
            random = renpy.random.random()

            enemies_count = 1
            if self.level > 13 and random < 0.1:
                enemies_count = 5
            if self.level > 8 and random < 0.2:
                enemies_count = 4
            elif self.level > 5 and random < 0.3:
                enemies_count = 3
            elif self.level > 3 and random < 0.5:
                enemies_count = 2

            while enemies_count > 0:
                enemy_name = renpy.random.choice(names)
                names.remove(enemy_name)
                attack_min = round(self.level * (1 + renpy.random.random())) + 1
                heal_min = round(self.level * (1 + renpy.random.random())) + 1

                level["scene"] = "bg plain"

                level["enemies"].append({
                    "name": enemy_name,
                    "health": round(5 * (self.level + 1) * (1 + renpy.random.random())),
                    "attack_min": attack_min,
                    "attack_max": attack_min + self.level + 1,
                    "heal_min": heal_min,
                    "heal_max": heal_min + self.level + 1,
                })

                enemies_count -= 1

            return level


        def start(self) -> None:
            """
            Start level.
            """
            self.battle = True
            level = self.get()

            player.energy = player.energy_max
            player.moves = player.moves_max

            if self.level >= 0:
                renpy.scene()
                renpy.show(level["scene"])
                renpy.with_statement(dissolve)

            enemies.generate(level["enemies"])
            enemies.show()

            deck.shuffle()


        def end(self) -> None:
            """
            End level.
            """
            self.battle = False


        def next(self, level=0) -> None:
            """
            Increment level.
            """
            if level:
                self.level = level
            else:
                self.level += 1


        def restart(self) -> None:
            """
            Restart level.
            """
            self.level = 0
            deck = Deck()
            player = Player()
