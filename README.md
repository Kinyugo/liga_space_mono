# Liga Space Mono

Ligaturized Space Mono but without the "fi" and "fl" ligatures. Based on [ToxicFrog's](https://github.com/ToxicFrog/Ligaturizer) Liga Space Mono.

It also contains a script in `scripts/liga_remover` that can remove ligatures from fonts using `fontforge`.

## Usage

```bash
git clone https://github.com/Kinyugo/liga_space_mono.git

cd liga_space_mono

sudo mkdir -p /usr/share/fonts/custom_fonts

sudo cp -r fonts /usr/share/fonts/custom_fonts/liga_space_mono
```
