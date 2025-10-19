label reward:

    if not rewards:
        jump shop

    $ reward_attack = renpy.random.randint(1, 2 + wins // 2)
    $ reward_heal = renpy.random.randint(1, 3 + wins // 2) * 2

    menu:
        "Claim your reward (remaining: [rewards]):"

        "Reroll rewards (-$[wins // 2])" if money >= wins // 2 and wins > 1:
            $ money -= wins // 2
            jump reward

        "Increase max health by {color=[colors.heal]}+[reward_heal]" if renpy.random.random() < 0.5:
            $ player.health += reward_heal
            $ player.health_max += reward_heal

        "Increase max energy by {color=[colors.energy]}+1" if renpy.random.random() < 0.1:
            $ player.energy_max += 1

        "Recover all health" if player.health < player.health_max:
            $ player.health = player.health_max

        "Pass":
            pass

    $ rewards -= 1

    jump reward
