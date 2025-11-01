init python:
    from uuid import uuid4


    class RPGCharacter():
        def __init__(self, **kwargs) -> None:
            self.id = str(uuid4())
            self.name = kwargs.get("name", "")

            image = kwargs.get("image", self.name.lower())
            if image:
                self.image_name = image
                width, height = renpy.image_size(f"images/enemies/{image} hover.png")
                self.width = width
                self.height = height

            self.health = self.health_max = kwargs.get("health", 0)
            self.energy = self.energy_max = kwargs.get("energy", 0)

            self.attack = 0
            self.attack_min = kwargs.get("attack_min", 0)
            self.attack_max = kwargs.get("attack_max", 0)
            self.attack_multiplier = kwargs.get("attack_multiplier", 1)

            self.heal = 0
            self.heal_min = kwargs.get("heal_min", 0)
            self.heal_max = kwargs.get("heal_max", 0)

            self.actions = kwargs.get("actions", [])

            self.stunned = False


        def action(self, key: str, value=None):
            """
            Get first action.
            """
            return next(iter(self.actions), {}).get(key, value)


        def image(self, state="") -> str:
            """
            Get image name.
            """
            if state:
                pass
            elif not player.turns:
                state = "idle"
            elif self.action("attack", 0) > 0:
                state = "attack"
            elif self.action("heal", 0) > 0:
                state = "heal"
            else:
                state = "idle"
            return f"{self.image_name} {state}"


        def say(self) -> str:
            """
            Get say.
            """
            if self.stunned:
                return f"{self.name} is stunned!"

            return self.action("say", "").format(name=self.name)


        def hurt(self, value: int) -> None:
            """
            Attack character.
            """
            if not value:
                return
            renpy.sound.queue("sound/punch.ogg", relative_volume=0.5)
            self.health -= value


        def recover(self, value: int, overheal=False) -> None:
            """
            Heal character.
            """
            if not value:
                return
            renpy.sound.queue("sound/potion.ogg", relative_volume=0.5)
            if not overheal and self.health + value >= self.health_max:
                self.health = self.health_max
            else:
                self.health += value


        def stun(self, stunned: bool) -> None:
            """
            Stun character.
            """
            self.stunned = bool(self.stunned or stunned)
