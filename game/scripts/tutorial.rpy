label tutorial:

    show screen player_money

    "Your money is on the top-left."

    show screen player_stats

    "Your stats are on the bottom-left."
    "When {b}Health{/b} reaches 0, you lose."
    "{b}Energy{/b} allows you to play cards."
    "Click {b}View Deck{/b} to see your cards."

    $ card = Card(action={"attack": {"value": 3}}, cost=1, name="Punch")
    show screen card(card)

    "The {b}Energy{/b} cost of the card is on the top-left."
    "The action is written in the card description."

    hide screen card

    $ levels.start()

    "The enemy’s stats are above."
    "Hover over the enemy’s name to see its upcoming action."

    $ deck.draw_cards(player.draw_cards)

    "You draw cards at the start of each turn."
    "Drag the card to the {i}enemy{/i} or to your {i}stats{/i} to play it."

    show screen player_end_tutorial
    call screen player_hand
