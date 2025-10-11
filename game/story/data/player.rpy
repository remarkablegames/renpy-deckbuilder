default player = Player(
    health=15,
    energy=3,
)


init python:
    class Player(RPGCharacter):
        def __init__(self, **kwargs) -> None:
            super().__init__(**kwargs)

        def end_turn(self) -> None:
            """
            End player turn.
            """
            deck.discard_hand()
            renpy.hide_screen("player_end_turn")
            renpy.jump("enemy_turn")
