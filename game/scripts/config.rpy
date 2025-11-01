# Should the user be allowed to rollback the game? If set to False, the user cannot interactively rollback.
define config.rollback_enabled = False


init python:
    LAYER_ENEMIES = "enemies"
    renpy.add_layer(LAYER_ENEMIES, below="screens")

    MUSIC_CHANNEL_UI="ui"
    renpy.music.register_channel(MUSIC_CHANNEL_UI, "sound", loop=False)


    def tooltip_custom_text_tag(tag, argument):
        return [(renpy.TEXT_TAG, "tooltip")]

    config.custom_text_tags["tooltip"] = tooltip_custom_text_tag


# Edit images: game/scripts/utils/images.rpy
# Edit levels: game/scripts/data/levels.json
