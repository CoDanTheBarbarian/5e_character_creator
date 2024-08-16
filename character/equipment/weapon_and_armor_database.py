                                # below is what each of these keys is expecting for a value
weapon_type = "weapon type"   # <-- a string 'simple' or 'martial'
damage_die = "damage die"   # <-- a tuple containing the individual die rolls for damage (multiple values means multiple rolls)
damage_type = "damage type"     # <-- a string representing damage type
core_attribute = "core attribute"    # <-- a tuple containing which ability_mod gets added to attack rolls with this weapon (multiple values means use the one that's higher)
weapon_properties = "weapon properties"     #  <-- a list of strings representing keys from the weapon properties dictionary

melee_weapon_stats = {
    'club': {weapon_type: 'simple', 
             damage_die: (4,), 
             damage_type: 'bludgeoning', 
             core_attribute: ('strength',), 
             weapon_properties: ['light']}, 
    'greatclub': {weapon_type: 'simple', 
                  damage_die: (8,), 
                  damage_type: 'bludgeoning', 
                  core_attribute: ('strength',), 
                  weapon_properties: ['two handed']}, 
    'mace': {weapon_type: 'simple', 
             damage_die: (6,), 
             damage_type: 'bludgeoning', 
             core_attribute: ('strength',), 
             weapon_properties: []}, 
    'sickle': {weapon_type: 'simple', 
               damage_die: (4,), 
               damage_type: 'slashing', 
               core_attribute: ('strength',), 
               weapon_properties: ['light']}, 
    'flail': {weapon_type: 'martial', 
              damage_die: (8,), 
              damage_type: 'bludgeoning', 
              core_attribute: ('strength',), 
              weapon_properties: []}, 
    'glaive': {weapon_type: 'martial', 
               damage_die: (10,), 
               damage_type: 'slashing', 
               core_attribute: ('strength',), 
               weapon_properties: ['heavy', 'reach', 'two handed']}, 
    'great axe': {weapon_type: 'martial', 
                  damage_die: (12,), 
                  damage_type: 'slashing', 
                  core_attribute: ('strength',), 
                  weapon_properties: ['heavy', 'two handed']}, 
    'great sword': {weapon_type: 'martial', 
                    damage_die: (6, 6), 
                    damage_type: 'slashing', 
                    core_attribute: ('strength',), 
                    weapon_properties: ['heavy', 'two handed']}, 
    'halberd': {weapon_type: 'martial', 
                damage_die: (10,), 
                damage_type: 'slashing', 
                core_attribute: ('strength',), 
                weapon_properties: ['heavy', 'reach', 'two handed']}, 
    'lance': {weapon_type: 'martial', 
              damage_die: (12,), 
              damage_type: 'piercing', 
              core_attribute: ('strength',), 
              weapon_properties: ['reach', 'special:']}, 
    'maul': {weapon_type: 'martial', 
             damage_die: (6, 6), 
             damage_type: 'bludgeoning', 
             core_attribute: ('strength',), 
             weapon_properties: ['heavy', 'two handed']}, 
    'morning star': {weapon_type: 'martial', 
                     damage_die: (8,), 
                     damage_type: 'piercing', 
                     core_attribute: ('strength',), 
                     weapon_properties: []}, 
    'pike': {weapon_type: 'martial', 
             damage_die: (10,), 
             damage_type: 'piercing', 
             core_attribute: ('strength',), 
             weapon_properties: ['heavy', 'reach', 'two handed']}, 
    'rapier': {weapon_type: 'martial', 
               damage_die: (8,), 
               damage_type: 'piercing', 
               core_attribute: ('strength', 'dexterity'), 
               weapon_properties: ['finesse']}, 
    'scimitar': {weapon_type: 'martial', 
                 damage_die: (6,), 
                 damage_type: 'slashing', 
                 core_attribute: ('strength', 'dexterity'), 
                 weapon_properties: ['finesse', 'light']}, 
    'short sword': {weapon_type: 'martial', 
                    damage_die: (6,), 
                    damage_type: 'piercing', 
                    core_attribute: ('strength', 'dexterity'), 
                    weapon_properties: ['finesse', 'light']}, 
    'war pick': {weapon_type: 'martial', 
                 damage_die: (8,), 
                 damage_type: 'piercing', 
                 core_attribute: ('strength',), 
                 weapon_properties: []}, 
    'whip': {weapon_type: 'martial', 
             damage_die: (4,), 
             damage_type: 'slashing', 
             core_attribute: ('strength', 'dexterity'), 
             weapon_properties: ['finesse', 'reach']}
}

range = "range"   # <-- a tuple pair of integers representing weapon range, first nummber is normal range, second is long range. 

ranged_weapon_stats = {
    'light crossbow': {weapon_type: 'simple', 
                       damage_die: (8,), 
                       damage_type: 'piercing', 
                       core_attribute: ('dexterity',), 
                       weapon_properties: ['ammunition', 'ranged', 'loading', 'two handed'], 
                       range: (80, 320)}, 
    'dart': {weapon_type: 
             'simple', damage_die: (4,), 
             damage_type: 'piercing', 
             core_attribute: ('dexterity',), 
             weapon_properties: ['finesse', 'thrown'], 
             range: (20, 60)}, 
    'short bow': {weapon_type: 'simple', 
                  damage_die: (6,), 
                  damage_type: 'piercing', 
                  core_attribute: ('dexterity',), 
                  weapon_properties: ['ammunition', 'ranged', 'two handed'], 
                  range: (80, 320)}, 
    'sling': {weapon_type: 'simple', 
              damage_die: (4,), 
              damage_type: 'bludgeoning', 
              core_attribute: ('dexterity',), 
              weapon_properties: ['ammunition', 'ranged'], 
              range: (80, 320)}, 
    'blow gun': {weapon_type: 'martial', 
                 damage_die: (1,), 
                 damage_type: 'piercing', 
                 core_attribute: ('dexterity',), 
                 weapon_properties: ['ammunition', 'ranged', 'loading'], 
                 range: (25, 100)}, 
    'hand crossbow': {weapon_type: 'martial', 
                      damage_die: (6,), 
                      damage_type: 'piercing', 
                      core_attribute: ('dexterity',), 
                      weapon_properties: ['ammunition', 'ranged', 'light', 'loading'], 
                      range: (30, 120)}, 
    'heavy crossbow': {weapon_type: 'martial', 
                       damage_die: (10,), 
                       damage_type: 'piercing', 
                       core_attribute: ('dexterity',), 
                       weapon_properties: ['ammunition', 'ranged', 'heavy', 'loading', 'two handed'], 
                       range: (100, 400)}, 
    'long bow': {weapon_type: 'martial', 
                 damage_die: (8,), 
                 damage_type: 'piercing', 
                 core_attribute: ('dexterity',), 
                 weapon_properties: ['ammunition', 'ranged', 'heavy', 'two handed'], 
                 range: (150, 600)}, 
    'net': {weapon_type: 'martial', 
            damage_die: (8,), 
            damage_type: 'piercing', 
            core_attribute: ('dexterity',), 
            weapon_properties: ['special:', 'thrown'], 
            range: (5, 15)},
    'dagger': {weapon_type: 'simple', 
               damage_die: (4,), 
               damage_type: 'piercing', 
               core_attribute: ('strength', 'dexterity'), 
               weapon_properties: ['finesse', 'light', 'thrown'], 
               range: (20, 60)}, 
    'handaxe': {weapon_type: 'simple', 
                damage_die: (6,), 
                damage_type: 'slashing', 
                core_attribute: ('strength',), 
                weapon_properties: ['light', 'thrown'], 
                range: (20, 60)}, 
    'javelin': {weapon_type: 'simple', 
                damage_die: (6,), 
                damage_type: 'piercing', 
                core_attribute: ('strength',), 
                weapon_properties: ['thrown'], 
                range: (30, 120)}, 
    'light hammer': {weapon_type: 'simple', 
                     damage_die: (4,), 
                     damage_type: 'bludgeoning', 
                     core_attribute: ('strength',), 
                     weapon_properties: ['light', 'thrown'], 
                     range: (20, 60)}
    }

versatile_die = "two handed damage die"

versatile_melee_weapon_stats = {
    'quarterstaff': {weapon_type: 'simple', 
                     damage_die: (6,), 
                     damage_type: 'bludgeoning', 
                     core_attribute: ('strength',), 
                     weapon_properties: ['versatile'], 
                     versatile_die: (8,)}, 
    'battle axe': {weapon_type: 'martial', 
                   damage_die: (8,), 
                   damage_type: 'slashing', 
                   core_attribute: ('strength',), 
                   weapon_properties: ['versatile'], 
                   versatile_die: (10,)}, 
    'long sword': {weapon_type: 'martial', 
                   damage_die: (8,), 
                   damage_type: 'slashing', 
                   core_attribute: ('strength',), 
                   weapon_properties: ['versatile'], 
                   versatile_die: (10,)}, 
    'warhammer': {weapon_type: 'martial', 
                  damage_die: (8,), 
                  damage_type: 'bludgeoning', 
                  core_attribute: ('strength',), 
                  weapon_properties: ['versatile'], 
                  versatile_die: (10,)}
    }

veratile_ranged_weapon_stats = {
    'trident': {weapon_type: 'martial', 
                damage_die: (6,), 
                damage_type: 'piercing', 
                core_attribute: ('strength',), 
                weapon_properties: ['thrown', 'versatile'], 
                range: (20, 60), 
                versatile_die: (8,)}, 
    'spear': {weapon_type: 'simple', 
              damage_die: (6,), 
              damage_type: 'piercing', 
              core_attribute: ('strength',), 
              weapon_properties: ['thrown', 'versatile'], 
              range: (20, 60), 
              versatile_die: (8,)}}

# separate class from weapons

armor_type = "armor type"
ac = "ac"
dex_mod = "dex mod"
dex_max = "dex max"
stealth_penalty = "disadvantage on stealth"
strength_min = "strength requirement"

armor_stats = {
    "padded": {armor_type: "light",
               ac: 11,
               dex_mod: True,
               dex_max: None,
               stealth_penalty: True,
               strength_min: None},
    "leather": {armor_type: "light",
               ac: 11,
               dex_mod: True,
               dex_max: None,
               stealth_penalty: False,
               strength_min: None},
    "studded leather": {armor_type: "light",
               ac: 12,
               dex_mod: True,
               dex_max: None,
               stealth_penalty: False,
               strength_min: None},
    "hide": {armor_type: "medium",
               ac: 12,
               dex_mod: True,
               dex_max: 2,
               stealth_penalty: False,
               strength_min: None},
    "chain shirt": {armor_type: "medium",
               ac: 13,
               dex_mod: True,
               dex_max: 2,
               stealth_penalty: False,
               strength_min: None},
    "scale mail": {armor_type: "medium",
               ac: 14,
               dex_mod: True,
               dex_max: 2,
               stealth_penalty: True,
               strength_min: None},
    "breastplate": {armor_type: "medium",
               ac: 14,
               dex_mod: True,
               dex_max: 2,
               stealth_penalty: False,
               strength_min: None},
    "half plate": {armor_type: "medium",
               ac: 15,
               dex_mod: True,
               dex_max: 2,
               stealth_penalty: True,
               strength_min: None},
    "ring mail": {armor_type: "heavy",
               ac: 14,
               dex_mod: False,
               dex_max: None,
               stealth_penalty: True,
               strength_min: None},
    "chain mail": {armor_type: "heavy",
               ac: 16,
               dex_mod: False,
               dex_max: None,
               stealth_penalty: True,
               strength_min: 13},
    "splint": {armor_type: "heavy",
               ac: 17,
               dex_mod: False,
               dex_max: None,
               stealth_penalty: True,
               strength_min: 15},
    "plate": {armor_type: "heavy",
               ac: 18,
               dex_mod: False,
               dex_max: None,
               stealth_penalty: True,
               strength_min: 15},
    "shield": {armor_type: "shield",
               ac: 2,
               dex_mod: False,
               dex_max: None,
               stealth_penalty: False,
               strength_min: None},
}

weapon_property_descriptions = {
    "ammunition": "Ammunition: requires ammo to use, one ammo per use.",
    "finesse": "Finesse: choose whether to use strength or dex modifier for attack and damage rolls",
    "heavy": "Heavy: small and tiny creatures have disacvantage on attack rolls",
    "light": "Light: ideal for two weapon fighting",
    "loading": "Loading: you can fire only one piece of ammo when you use an action, bonus action or reaction, regardless of how many attacks you have.",
    "rangeged": "Rangeged: rangeged weapon, with normal and long rangege. When attacking beyond normal rangege you have disadvantage",
    "reach": "Reach: add 5 feet to your reach while using this weapon",
    "special": "Special:",
    "thrown": "Thrown: throw this weapon for a rangeged attack, using same modifier as a melee attack with this weapon.",
    "two handed": "Two Handed: requires two hands to wield",
    "versatile": "Versatile: can be used with one or two hands, rolling a different damage die for each option"
}

