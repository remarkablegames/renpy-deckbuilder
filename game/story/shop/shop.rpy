label shop:

    show screen player_deck(0, 1.0)

    python:
        config.menu_include_disabled = True
        cost_base = max(wins, 3)
        cost_reward = cost_base + player.rewards_bought
        cost_card_buy = cost_base + player.cards_bought
        cost_card_upgrade = cost_base * 2 + player.cards_upgraded
        cost_card_remove = cost_base * 3 + player.cards_removed

    menu:
        "What do you want to do?"

        "Buy a card (-$[cost_card_buy])
        {tooltip}Add 1 card to your deck ([player.shop_cards] choices, {i}nonrefundable{/i})" if money >= cost_card_buy:
            python:
                config.menu_include_disabled = False
                money -= cost_card_buy
                player.cards_bought += 1
                cards = Card.generate(player.shop_cards)

            call screen card_add(cards)

        "Upgrade a card (-$[cost_card_upgrade])
        {tooltip}Upgrade 1 card in your deck ([player.shop_cards] choices, {i}nonrefundable{/i})" if money >= cost_card_upgrade:
            python:
                config.menu_include_disabled = False
                money -= cost_card_upgrade
                player.cards_upgraded += 1

                card_type = renpy.random.choice(
                    ["all"] * (1 if wins > 3 else 0) +
                    ["attack"] * 6 +
                    ["cost"] * (1 if wins > 2 else 0) +
                    ["draw"] * 3 +
                    ["energy"] * (1 if wins > 3 else 0) +
                    ["heal"] * 6 +
                    ["stun"] * (1 if wins > 1 else 0) +
                    ["times"] * (1 if wins > 3 else 0) +
                    []
                )

                if card_type in ["attack", "heal"]:
                    card_value = renpy.random.randint(1, 3)
                elif card_type in ["draw", "energy"]:
                    card_value = renpy.random.randint(1, 2)
                else:
                    card_value = 1

                cards = deck.get_cards(player.shop_cards, card_type)

            call screen card_upgrade(cards, card_type, card_value)

        "Remove a card (-$[cost_card_remove])
        {tooltip}Remove 1 card from your deck ({i}nonrefundable{/i})" if money >= cost_card_remove:
            python:
                config.menu_include_disabled = False
                money -= cost_card_remove
                player.cards_upgraded += 1

            call screen card_remove

        "Get reward (-$[cost_reward])
        {tooltip}Upgrade a stat ({i}nonrefundable{/i})" if money >= cost_reward:
            python:
                config.menu_include_disabled = False
                money -= cost_reward
                player.rewards_bought += 1
                rewards += 1

            jump reward

        "Battle":
            python:
                config.menu_include_disabled = False
                levels.next()

            hide screen player_deck

            jump battle


screen card_add(cards):

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        text "Add 1 card to your deck:"

        null height 25

        hbox:
            spacing 25

            for card in cards:
                button:
                    action [
                        Queue(MUSIC_CHANNEL_UI, "sound/draw.ogg"),
                        Function(deck.cards.append, card),
                        Jump("shop"),
                    ]
                    hover_background colors.white
                    use card_frame(card)

        null height 25
        use shop_return


screen card_upgrade(cards, card_type, card_value):

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        text Card.label_upgrade(card_type, card_value)

        null height 25

        hbox:
            spacing 25

            for card in cards:
                button:
                    action [
                        Queue(MUSIC_CHANNEL_UI, "sound/draw.ogg"),
                        Function(card.upgrade, card_type, card_value),
                        Jump("shop"),
                    ]
                    hover_background colors.white
                    use card_frame(card)

        null height 25
        use shop_return


screen card_remove():

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        viewport:
            scrollbars "horizontal"
            ysize 450

            hbox:
                spacing 25

                for card in deck.cards:
                    button:
                        action [
                            Queue(MUSIC_CHANNEL_UI, "sound/draw.ogg"),
                            Function(deck.cards.remove, card),
                            Jump("shop"),
                        ]
                        hover_background colors.white
                        use card_frame(card)

        null height 50
        use shop_return


screen shop_return():

    frame:
        xalign 0.5
        textbutton "Pass":
            action Jump("shop")
