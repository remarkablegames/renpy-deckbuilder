label shop:

    show screen player_deck(0, 1.0)

    python:
        config.menu_include_disabled = True
        cost_base = max(wins, 3)
        cost_reward = cost_base
        cost_buy_card = cost_base
        cost_upgrade_card = cost_base * 2
        cost_remove_card = cost_base * 3

    menu:
        "What do you want to do?"

        "Buy a card (-$[cost_buy_card])
        {tooltip}Add 1 card to your deck" if money >= cost_buy_card:
            $ money -= cost_buy_card
            $ config.menu_include_disabled = False
            call screen add_card

        "Upgrade a card (-$[cost_upgrade_card])
        {tooltip}Upgrade 1 card in your deck" if money >= cost_upgrade_card:
            python:
                money -= cost_upgrade_card
                config.menu_include_disabled = False
                upgrade_card_type = renpy.random.choice(
                    ["all"] * 1 +
                    ["attack"] * 6 +
                    ["cost"] * 1 +
                    ["draw"] * 3 +
                    ["energy"] * 3 +
                    ["heal"] * 3 +
                    ["stun"] * 1 +
                    ["times"] * 1 +
                    []
                )
                upgrade_card_value = renpy.random.randint(1, 3)
            call screen upgrade_card

        "Remove a card (-$[cost_remove_card])
        {tooltip}Remove 1 card from your deck" if money >= cost_remove_card:
            $ money -= cost_remove_card
            $ config.menu_include_disabled = False
            call screen remove_card

        "Get reward (-$[cost_reward])
        {tooltip}Upgrade a stat" if money >= cost_reward:
            $ money -= cost_reward
            $ rewards += 1
            $ config.menu_include_disabled = False
            jump reward

        "Battle":
            $ config.menu_include_disabled = False
            hide screen player_deck
            jump battle


screen add_card():

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        text "Add 1 card to your deck:"

        null height 25

        hbox:
            spacing 25

            for card in Card.generate(3):
                button:
                    action [Function(deck.cards.append, card), Jump("shop")]
                    use card_frame(card)

        null height 25

        frame:
            xalign 0.5
            textbutton "Pass":
                action Jump("shop")


screen upgrade_card():

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        text Card.label_upgrade(upgrade_card_type, upgrade_card_value)

        null height 25

        hbox:
            spacing 25

            for card in deck.get_cards(3, upgrade_card_type):
                button:
                    action [Function(card.upgrade, upgrade_card_type, upgrade_card_value), Jump("shop")]
                    use card_frame(card)

        null height 25

        frame:
            xalign 0.5
            textbutton "Pass":
                action Jump("shop")


screen remove_card():

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
                        action [Function(deck.cards.remove, card), Jump("shop")]
                        use card_frame(card)

        null height 50

        frame:
            xalign 0.5
            textbutton "Pass":
                action Jump("shop")
