init python:
    from uuid import uuid4


    class RPGCharacter():
        def __init__(self, **kwargs) -> None:
            self.id = str(uuid4())

            self.name = kwargs.get("name", "")
            self.image = kwargs.get("image", self.name.replace(" ", "_").lower())

            if self.name == "Girl":
                self.width = 228
                self.height = 1000
            else:
                self.width = 211
                self.height = 1000

            self.health = self.health_max = kwargs.get("health", 0)
            self.energy = self.energy_max = kwargs.get("energy", 0)

            self.attack = 0
            self.attack_min = kwargs.get("attack_min", 0)
            self.attack_max = kwargs.get("attack_max", 0)
            self.attack_multiplier = kwargs.get("attack_multiplier", 1)

            self.heal_value = 0
            self.heal_min = kwargs.get("heal_min", 0)
            self.heal_max = kwargs.get("heal_max", 0)

            self.stunned = False


        def turn_rng(self) -> None:
            """
            Generate random numbers for turn.
            """
            self.attack = round(renpy.random.randint(self.attack_min, self.attack_max) * self.attack_multiplier)
            self.heal_value = renpy.random.randint(self.heal_min, self.heal_max)


        def hurt(self, value: int) -> None:
            """
            Attack character.
            """
            renpy.sound.queue("sound/punch.ogg", relative_volume=0.5)
            self.health -= value


        def heal(self, value: int, overheal=False) -> None:
            """
            Heal character.
            """
            renpy.sound.queue("sound/potion.ogg", relative_volume=0.5)
            if not overheal and self.health + value >= self.health_max:
                self.health = self.health_max
            else:
                self.health += value
