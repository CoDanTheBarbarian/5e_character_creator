
# D&D 5e Character Creator

Do you love rolling up new characters, but hate doing math? Let this CLI tool do it for you! Each choice you can make for your character has been serialized. Any choice you can make is numbered so choosing is as simple as entering a valid number. After entering your choices for your character this program will populate a form fillable pdf template with all your stats calculated and automatically entered for you and save it in the project directory. The resulting pdf remains unflattened so you can manually enter information like your appearance and backstory.

## Preface

This is a supplementary product for Dungeons & Dragons and will not provide you with information in the Player's Handbook. For each choice you make it is assumed you understand what that choice means. Current functionality is limited to level one characters.

## Installation

1. Clone the repository to your workspace:

```bash
  git clone https://github.com/CoDanTheBarbarian/5e_character_creator
```

2. If you don't already have fillpdf installed, do that now:
```bash
  pip install fillpdf
```

## Usage

Upon program start you will be prompted to enter your charcter name. This will also be the title of the output character sheet.
Each subsequent prompt expects a number response corresponding to one of the listed choices.

## Demo

https://github.com/user-attachments/assets/8552103f-4dfb-400c-8487-396251df5f88

Demo character sheet result:
![Karlach Demo PDF](https://github.com/user-attachments/assets/1ec3fe9d-6a51-43a4-8007-7ee24d51fbc9)

![Karlach Demo Sheet (2)](https://github.com/user-attachments/assets/7122dd30-a669-4c20-96e1-47f568e31e38)

## Roadmap

- Implement a GUI that displays both the CLI process and a preview of the output PDF

- Complete the database information for Races and Classes

- Add a database for spells

- Add implementation for level up

- Refactor into a Go web app with support for users to login and save and retrieve character sheets from a database