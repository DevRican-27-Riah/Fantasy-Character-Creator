import random

# Fantasy Character Creator
# Rule-based AI assignment

PERSONALITY_RULES = {
    "1": ("Loyal", "dependability and protecting friends"),
    "2": ("Brave", "courage and determination"),
    "3": ("Intelligent", "strategic thinking and problem-solving"),
    "4": ("Compassionate", "empathy and helping others"),
    "5": ("Ambitious", "determination and achieving goals"),
}

ABILITY_OPTIONS = {
    "1": "Elemental Magic",
    "2": "Healing Magic",
    "3": "Shadow Magic",
    "4": "Weapon Mastery",
    "5": "Nature Magic",
}

ABILITY_RULES = {
    "Elemental Magic": "Controls fire, water, earth, and air.",
    "Healing Magic": "Restores health and helps injured allies.",
    "Shadow Magic": "Uses shadows to conceal movement and create illusions.",
    "Weapon Mastery": "Provides advanced combat skills and weapon precision.",
    "Nature Magic": "Controls plants and channels the forces of nature.",
}

ALIGNMENT_RULES = {
    "1": ("Heroic", "Protecting others and doing what is right."),
    "2": ("Neutral", "Following a personal code and considering the consequences of actions."),
    "3": ("Villainous", "Gaining influence or power to achieve personal goals."),
}

CLASS_RULES = {
    # Two-ability combinations
    frozenset(["Elemental Magic", "Healing Magic"]): "Arcane Medic",
    frozenset(["Elemental Magic", "Shadow Magic"]): "Umbral Tempest",
    frozenset(["Elemental Magic", "Weapon Mastery"]): "Elemental Spellblade",
    frozenset(["Elemental Magic", "Nature Magic"]): "Primal Elementalist",
    frozenset(["Healing Magic", "Shadow Magic"]): "Soul Warden",
    frozenset(["Healing Magic", "Weapon Mastery"]): "Battle Cleric",
    frozenset(["Healing Magic", "Nature Magic"]): "Verdant Healer",
    frozenset(["Shadow Magic", "Weapon Mastery"]): "Shadowblade",
    frozenset(["Shadow Magic", "Nature Magic"]): "Wildshade Ranger",
    frozenset(["Weapon Mastery", "Nature Magic"]): "Warden Knight",
    # Three-ability combinations
    frozenset(["Elemental Magic", "Healing Magic", "Shadow Magic"]): "Twilight Arcanist",
    frozenset(["Elemental Magic", "Healing Magic", "Weapon Mastery"]): "Arcane Battlemage",
    frozenset(["Elemental Magic", "Healing Magic", "Nature Magic"]): "Primal Sage",
    frozenset(["Elemental Magic", "Shadow Magic", "Weapon Mastery"]): "Duskstorm Duelist",
    frozenset(["Elemental Magic", "Shadow Magic", "Nature Magic"]): "Umbral Druid",
    frozenset(["Elemental Magic", "Weapon Mastery", "Nature Magic"]): "Elemental Vanguard",
    frozenset(["Healing Magic", "Shadow Magic", "Weapon Mastery"]): "Nightfall Reaper",
    frozenset(["Healing Magic", "Shadow Magic", "Nature Magic"]): "Spirit Grove Keeper",
    frozenset(["Healing Magic", "Weapon Mastery", "Nature Magic"]): "Verdant Paladin",
    frozenset(["Shadow Magic", "Weapon Mastery", "Nature Magic"]): "Thornshadow Ranger",
    # Four-ability combinations
    frozenset(["Elemental Magic", "Healing Magic", "Shadow Magic", "Weapon Mastery"]): "Riftblade",
    frozenset(["Elemental Magic", "Healing Magic", "Shadow Magic", "Nature Magic"]): "Primal Archmage",
    frozenset(["Elemental Magic", "Healing Magic", "Weapon Mastery", "Nature Magic"]): "Elemental Warden",
    frozenset(["Elemental Magic", "Shadow Magic", "Weapon Mastery", "Nature Magic"]): "Stormshade Ranger",
    frozenset(["Healing Magic", "Shadow Magic", "Weapon Mastery", "Nature Magic"]): "Shadowbloom Guardian",
    # Five-ability combination
    frozenset(["Elemental Magic", "Healing Magic", "Shadow Magic",
               "Weapon Mastery", "Nature Magic"]): "Mythic Weaver",
}


def ask_personalities():
    """Ask for one or more traits; re-prompt until at least one is valid."""
    print()
    print("Choose your character's personality traits:")
    for number, (trait, _) in PERSONALITY_RULES.items():
        print(number + ". " + trait)
    print("Enter at least one choice, separated by commas.")
    print("Example: 1, 2, 3")

    traits = []
    strengths = []
    while len(traits) == 0:
        choices = input("Choose your traits: ").split(",")
        for choice in choices:
            choice = choice.strip()
            if choice in PERSONALITY_RULES:
                trait, strength = PERSONALITY_RULES[choice]
                if trait not in traits:
                    traits.append(trait)
                    strengths.append(strength)
            else:
                print("Ignoring invalid choice:", choice)
        if len(traits) == 0:
            print("Please choose at least one valid personality trait.")
    return traits, strengths


def ask_abilities():
    """Ask for abilities; re-prompt until at least two different ones are valid."""
    print()
    print("Choose your character's abilities:")
    for number, ability in ABILITY_OPTIONS.items():
        print(number + ". " + ability)
    print("Enter at least 2 different choices, separated by commas.")
    print("Example: 1, 5")

    chosen = []
    while len(chosen) < 2:
        choices = input("Choose your abilities: ").split(",")
        for choice in choices:
            choice = choice.strip()
            if choice in ABILITY_OPTIONS:
                ability = ABILITY_OPTIONS[choice]
                if ability not in chosen:
                    chosen.append(ability)
            else:
                print("Ignoring invalid choice:", choice)
        if len(chosen) < 2:
            print("You must choose at least two different abilities.")
    return chosen


def ask_alignment():
    """Ask for an alignment; re-prompt until the choice is 1, 2, or 3."""
    print()
    print("Choose your character's alignment:")
    print("1. Heroic")
    print("2. Neutral")
    print("3. Villainous")

    choice = input("Choose 1, 2, or 3: ").strip()
    while choice not in ALIGNMENT_RULES:
        print("Invalid choice. Please choose 1, 2, or 3.")
        choice = input("Choose 1, 2, or 3: ").strip()
    return ALIGNMENT_RULES[choice]


def find_class(abilities):
    return CLASS_RULES.get(frozenset(abilities), "Unclassified Adventurer")


def build_backstory(personalities, abilities, alignment):
    details = []
    if "Loyal" in personalities:
        details.append(
            "They once stood by a trusted ally during a dangerous situation, "
            "proving that their loyalty would never waver."
        )
    if "Shadow Magic" in abilities:
        details.append(
            "They discovered their ability to move unseen through the shadows "
            "while exploring a mysterious, forgotten place."
        )
    if alignment == "Heroic":
        details.append("They are driven to protect those who cannot protect themselves.")
    elif alignment == "Neutral":
        details.append(
            "They follow a personal code and make decisions based on their own principles."
        )
    else:
        details.append("They seek greater influence and power to achieve their goals.")
    return " ".join(details)


def show_profile(name, personalities, strengths, abilities, character_class,
                 alignment, motivation, backstory):
    print()
    print("===================================")
    print("       FINAL CHARACTER PROFILE")
    print("===================================")
    print("Name:", name)
    print("Personality:", ", ".join(personalities))
    print("Strengths:", ", ".join(strengths))
    print("Abilities:", ", ".join(abilities))
    print("Class:", character_class)
    print()
    print("Ability Effects:")
    for ability in abilities:
        print("-", ability + ":", ABILITY_RULES[ability])
    print()
    print("Alignment:", alignment)
    print("Motivation:", motivation)
    print()
    print("Backstory:")
    print(backstory)


# ---------------------------------------------------------------
# Welcome and naming
# ---------------------------------------------------------------
print("===================================")
print("      FANTASY CHARACTER CREATOR")
print("===================================")
print("Welcome! Let's create a fantasy character.")
print()

print("How would you like to name your character?")
print("1. Enter my own name")
print("2. Generate a fantasy name")

name_choice = input("Choose 1 or 2: ").strip()
while name_choice not in ["1", "2"]:
    print("Invalid choice. Please choose 1 or 2.")
    name_choice = input("Choose 1 or 2: ").strip()

if name_choice == "1":
    character_name = input("Enter your character's name: ").strip()
    while character_name == "":
        print("Character name cannot be blank.")
        character_name = input("Enter your character's name: ").strip()
else:
    first_names = ["Elarion", "Vaelis", "Nymera"]
    last_names = ["Stormborn", "Nightfall", "Dawnkeeper"]
    character_name = random.choice(first_names) + " " + random.choice(last_names)

print("Character name:", character_name)

# ---------------------------------------------------------------
# Personality, abilities, class, alignment
# ---------------------------------------------------------------
personalities, strengths = ask_personalities()
print("Personalities:", ", ".join(personalities))
print("Strengths:", ", ".join(strengths))

abilities = ask_abilities()
print("Abilities:", ", ".join(abilities))
print()
print("Your character's ability effects:")
for ability in abilities:
    print("-", ability + ":", ABILITY_RULES[ability])

character_class = find_class(abilities)
print()
print("Your character's class:", character_class)

alignment, motivation = ask_alignment()
print("Alignment:", alignment)
print("Motivation:", motivation)

# ---------------------------------------------------------------
# Backstory and first profile
# ---------------------------------------------------------------
character_backstory = build_backstory(personalities, abilities, alignment)

print()
print("===================================")
print("       CHARACTER BACKSTORY")
print("===================================")
print(character_name + "'s Story:")
print(character_backstory)

show_profile(character_name, personalities, strengths, abilities,
             character_class, alignment, motivation, character_backstory)

# ---------------------------------------------------------------
# Edit menu
# ---------------------------------------------------------------
while True:
    print()
    print("===================================")
    print("       EDIT YOUR CHARACTER")
    print("===================================")
    print("1. Change character name")
    print("2. Change personality traits")
    print("3. Change abilities")
    print("4. Change alignment")
    print("5. Finish character creation")

    edit_choice = input("Choose 1-5: ").strip()

    if edit_choice == "1":
        new_name = input("Enter your new character name: ").strip()
        while new_name == "":
            print("Name cannot be blank.")
            new_name = input("Enter your new character name: ").strip()
        character_name = new_name
        print("Name updated!")

    elif edit_choice == "2":
        personalities, strengths = ask_personalities()
        print("Personalities updated:", ", ".join(personalities))
        print("Strengths updated:", ", ".join(strengths))

    elif edit_choice == "3":
        abilities = ask_abilities()
        character_class = find_class(abilities)
        print("Abilities updated:", ", ".join(abilities))
        print("New character class:", character_class)
        print("Ability effects:")
        for ability in abilities:
            print("-", ability + ":", ABILITY_RULES[ability])

    elif edit_choice == "4":
        alignment, motivation = ask_alignment()
        print("Alignment updated:", alignment)
        print("Motivation updated:", motivation)

    elif edit_choice == "5":
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

# ---------------------------------------------------------------
# Final profile
# ---------------------------------------------------------------
character_backstory = build_backstory(personalities, abilities, alignment)
show_profile(character_name, personalities, strengths, abilities,
             character_class, alignment, motivation, character_backstory)

print()
print("===================================")
print("     CHARACTER CREATION COMPLETE")
print("===================================")
print("Happy adventuring!")