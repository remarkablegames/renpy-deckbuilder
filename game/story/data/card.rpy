init python:
    from uuid import uuid4


    class Card:
        label_description_yalign = 0.5
        label_name_ypos = 5
        width = 250
        height = 350
        offset = 80


        def __init__(self, **kwargs) -> None:
            self.id = str(uuid4())
            self.cost = kwargs.get("cost", 0)
            self.action = kwargs.get("action", {})
            self.value = kwargs.get("value", 0)

            image = kwargs.get("image", "card")
            self.image = f"cards/{image}.png"
            self.name = image.capitalize()

            if renpy.variant("mobile") or renpy.variant("touch"):
                self.label_description_ypos = 0.5


        def label_size(self, label: str) -> str:
            """
            Get label size.
            """
            size = 1.0
            length = len(label)

            if length < 5:
                size = 0.95
            elif length < 15:
                size = 0.9
            elif length < 25:
                size = 0.85
            elif length < 35:
                size = 0.8
            else:
                size = 0.75

            if renpy.variant("mobile") or renpy.variant("touch"):
                size -= 0.15

            return f"{{size=*{size}}}" if not size == 1.0 else ""


        def label_name(self) -> str:
            """
            Name label.
            """
            return self.label_size(self.name) + "{color=[colors.label]}{b}{k=-2}" + self.name


        def label_cost(self) -> str:
            """
            Cost label.
            """
            return self.label_size(str(self.cost)) + emojis.get(self.cost)


        def label_description(self) -> str:
            """
            Description label.
            """
            label = ""
            color = "{color=[colors.label]}"

            for action, data in self.action.items():
                value = data["value"]

                if not value:
                    continue

                label += action.capitalize()
                label += f" {value}"

                if data.get("times", 1) > 1:
                    label += f" ×{data.get('times')}"

                if data.get("stun"):
                    label += " Stun"

                if data.get("all"):
                    label += " All"

                if action == "turns":
                    label += " once per battle"

                label += "\n"

            label = label.rstrip('\n')

            return self.label_size(label) + color + label


        @staticmethod
        def label_upgrade(action: str, value=1) -> str:
            """
            Upgrade label.
            """
            if action == "all":
                return f"Select a card to apply effects to {{b}}{{color=[colors.note]}}all{{/color}}{{/b}} enemies:"
            elif action == "cost":
                return f"Select a card to decrease {{b}}{{color=[colors.note]}}cost{{/color}}{{/b}} by {emojis.get(1)}:"
            elif action == "stun":
                return f"Select a card to {{b}}{{color=[colors.note]}}stun{{/color}}{{/b}} an enemy:"
            elif action == "times":
                return f"Select a card to increase action by 1 {{b}}{{color=[colors.note]}}time{{/color}}{{/b}}:"
            else:
                return f"Select a card to increase {{b}}{{color=[colors.note]}}{action}{{/color}}{{/b}} by {{b}}{value}{{/b}}:"


        def upgrade(self, action: str, value=1) -> None:
            """
            Upgrade card.
            """
            if action in ["all", "stun"]:
                self.action["attack"][action] = True
            elif action == "cost" and self.cost > 0:
                self.cost -= 1
            elif action == "times":
                action = self.action.get("attack") if self.action.get("attack") else self.action.get("heal")
                action["times"] = action.get("times", 1)
                action["times"] += 1
            else:
                if self.action.get(action):
                    self.action[action]["value"] += value
                else:
                    self.action[action] = {"value": value}


        def get_xpos(self) -> int:
            """
            Calculate x-position.
            """
            x = config.screen_width / 2
            x -= (self.width + self.offset * (len(deck.hand) - 1)) / 2
            x += deck.hand.index(self) * self.offset
            return int(x)


        def get_ypos(self) -> int:
            """
            Calculate y-position.
            """
            return config.screen_height - self.height


        def get_pos(self):
            """
            Calculate xy-position.
            """
            return self.get_xpos(), self.get_ypos()


        def use(self, target) -> None:
            """
            Use card.
            """
            if player.energy < self.cost:
                return

            player.energy -= self.cost
            is_enemy = target != player

            energy = self.action.get("energy")
            if energy:
                renpy.sound.queue("sound/powerup.ogg")
                player.energy += energy["value"]

            draw = self.action.get("draw")
            if draw:
                deck.draw_cards(draw["value"])

            heal = self.action.get("heal")
            if heal:
                for _ in range(heal.get("times", 1)):
                    target.heal(heal["value"])

            attack = self.action.get("attack")
            if attack:
                for _ in range(attack.get("times", 1)):
                    if is_enemy and attack.get("all"):
                        targets = enemies.alive()
                    else:
                        targets = [target]
                    for target in targets:
                        target.hurt(attack["value"])
                        if is_enemy:
                            if attack.get("stun"):
                                target.stunned = True
                            renpy.show(target.image, at_list=[shake], layer=LAYER_ENEMIES)
                        else:
                            renpy.invoke_in_thread(renpy.with_statement, vpunch)

            deck.discard_card(self)


        @staticmethod
        def generate(count=1) -> list:
            """
            Generate card(s).
            """
            cards = []

            for _ in range(count):
                card = Card(
                    cost=renpy.random.randint(1, 3),
                    action={
                        renpy.random.choice(["attack", "draw", "energy", "heal"]): {
                            "value": renpy.random.randint(1, 6)
                        },
                    },
                )
                cards.append(card)

            return cards
