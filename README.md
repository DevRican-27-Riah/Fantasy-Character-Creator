# Fantasy-Character-Creator

A rule-based AI program written in Python. It builds a fantasy character from the user's choices and applies predefined IF-THEN rules to decide the character's strengths, class, motivation, and backstory. It uses no machine learning, so every result can be traced back to a specific rule.

## What it does

- Names the character (your own name or a generated fantasy name)
- Assigns strengths based on one or more personality traits
- Assigns a class based on a combination of 2 to 5 abilities (26 possible classes)
- Sets a motivation based on alignment (Heroic, Neutral, or Villainous)
- Builds a short backstory from the character's traits, abilities, and alignment
- Lets you edit the character afterward, then recalculates the class, motivation, and backstory
- Validates input and asks again when a choice is invalid

## How to run

1. Install Python 3 (https://www.python.org/downloads/).
2. Download `fantasy_character_creator.py` from this repository.
3. Open a terminal in the folder with the file and run:

```
fantasy_character_creator.py
```

On some systems the command is `python3 character_creator.py`.

## Requirements

No third-party packages are needed. The program uses only Python's standard library (`random`). See `requirements.txt`.

## Files

| File | Description |
| --- | --- |
| `fantasy_character_creator.py
` | The program |
| `requirements.txt` | Dependencies (none beyond Python 3) |
| Project document (PDF or Word) | Three project ideas, the rules and logic, three test results, and a reflection |

## Example

Choosing the traits Loyal, abilities Shadow Magic and Weapon Mastery, and a Villainous alignment produces the class **Shadowblade** and a backstory that includes loyalty, discovering shadow powers, and a drive for power.
