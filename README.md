
# D&D 5e Character Sheet Generator

Do you love rolling up new characters, but hate how long it takes? Let this CLI tool do the hard work for you! Simply make your choices and in minutes you have a complete editable character sheet. Take the manual calculations out of deriving your characters stat bonus' so you can enjoy the decision making of character creation and be table ready in mere moments.

## Preface

This is a supplementary product for Dungeons & Dragons and will not provide you with information in the Player's Handbook about how to play the game. For each choice you make it is assumed you understand what that choice means. Current functionality is limited to level one characters. Delivers an experience Rules as Written.

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



https://github.com/user-attachments/assets/cd4ea4d7-41ff-4db2-b796-8c3136edc3cb



Demo character sheet result:

![Gimli Page 1](https://github.com/user-attachments/assets/21e1fc09-2eca-4646-8557-300d4a426aab)

![Gimli Page 2](https://github.com/user-attachments/assets/f52e84a9-822f-42ea-aa15-8842424a843d)


## Roadmap

- Implement a GUI that displays both the CLI process and a preview of the output PDF

- Add a database for spells

- Add implementation for level up

- Refactor into a Go web app with support for users to login and save and retrieve character sheets from a database
