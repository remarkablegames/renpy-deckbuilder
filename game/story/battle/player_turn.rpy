label player_turn:

    $ deck.draw_cards(player.draw_cards)

    show screen player_end_turn

    jump player_hand


label player_hand:

    python:
        for enemy in enemies.enemies:
            if renpy.showing(enemy.image) and enemy.health <= 0:
                enemies.hide(enemy)

    if enemies.dead():
        jump win

    if player.health <= 0:
        jump lose

    call screen player_hand


screen player_hand():
    draggroup:
        for enemy in enemies.enemies:
            if enemy.health > 0:
                drag:
                    drag_name enemy.id
                    draggable False
                    droppable True
                    idle_child Solid((0, 0, 0, 0), xsize=enemy.width, ysize=enemy.height)
                    selected_idle_child f"enemies/{enemy.image} hover.png"
                    xalign enemies.xalign_position(enemy) yalign Enemies.YALIGN

        for card in deck.hand:
            drag:
                as draggable
                drag_name card.id
                dragged ondrag
                droppable False
                drag_raise False
                pos card.get_pos()

                use card_frame(card, draggable)

        drag:
            drag_name player.id
            draggable False
            droppable True
            selected_idle_child Solid((255, 255, 255, 100), xsize=312, ysize=235)
            yalign 1.0

            frame:
                background Solid((0, 0, 0, 0))
                xysize 312, 235


init python:
    def ondrag(drags, drop) -> None:
        drag = drags[0]
        card_id = drag.drag_name
        card = deck.get_card(card_id)

        if not drop:
            drag.snap(card.get_xpos(), card.get_ypos(), 0.2)
            return

        character_id = drop.drag_name
        if player.id == character_id:
            card.use(player)
        elif character_id:
            enemy = enemies.get(character_id)
            card.use(enemy)

        # snap unused card back
        if card in deck.hand:
            drag.snap(card.get_xpos(), card.get_ypos(), 0.2)

        renpy.jump("player_hand")
