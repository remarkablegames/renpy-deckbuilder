<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/renpy-deckbuilder/master/game/gui/window_icon.png" alt="Ren'Py Deckbuilder">
</p>

# Ren'Py Deckbuilder

![release](https://img.shields.io/github/v/release/remarkablegames/renpy-deckbuilder)
[![build](https://github.com/remarkablegames/renpy-deckbuilder/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/renpy-deckbuilder/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/renpy-deckbuilder/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/renpy-deckbuilder/actions/workflows/lint.yml)

🃏 Ren'Py Deckbuilder Template.

Play the game on:

- [remarkablegames](https://remarkablegames.org/renpy-deckbuilder)

Or download:

- [Mac](https://github.com/remarkablegames/renpy-rpg/releases/latest/download/mac.zip)
- [Windows](https://github.com/remarkablegames/renpy-rpg/releases/latest/download/pc.zip)

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)

### Audio

- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)
- Pixabay
  - [Heal Up](https://pixabay.com/sound-effects/heal-up-39285/)
  - [Health Pickup](https://pixabay.com/sound-effects/health-pickup-6860/)
  - [Heartbeat 01 - BRVHRTZ](https://pixabay.com/sound-effects/heartbeat-01-brvhrtz-225058/)
  - [Punch Sound Effects](https://pixabay.com/sound-effects/punch-sound-effects-28649/)
  - [card mixing](https://pixabay.com/sound-effects/card-mixing-48088/)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/renpy-deckbuilder.git
cd renpy-deckbuilder
```

Rename the project:

```sh
git grep -l "Ren'Py Deckbuilder" | xargs sed -i '' -e "s/Ren'Py Deckbuilder/My Game/g"
```

```sh
git grep -l 'renpy-deckbuilder' | xargs sed -i '' -e 's/renpy-deckbuilder/my-game/g'
```

Replace the assets:

- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`
- [ ] [`icon.icns`](https://anyconv.com/png-to-icns-converter/)
- [ ] [`icon.ico`](https://anyconv.com/png-to-ico-converter/)
- [ ] `web-icon.png`
- [ ] `web-presplash.webp`

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
