from dataclasses import dataclass
from Options import (Choice, OptionList, NamedRange, 
    StartInventoryPool,
    PerGameCommonOptions, DeathLinkMixin)

class Character(Choice):
    """Rebecca: Rising Rookie (Wesker is weird...) also the only choice"""
    display_name = "Character to Play"
    option_rebecca = 0
    default = 0

class Difficulty(Choice):
    """Normal: Only set up atm
       Hard: Not unlocked at start currently not randomized
       Easy: currently not randomized; You can pick Normal here, but some items will not be randomized
       """
    display_name = "Difficulty to Play On"
    option_normal = 0
    option_hard = 1
    default = 0

class BonusStart(Choice):
    """Some players might want to start with a little help in the way of a few extra heal items and packs of ammo. 

    False: Normal, don't start with extra heal items and packs of ammo.
    True: Start with those helper items.
    WARNING. This is currently not functional"""
    display_name = "Bonus Start"
    option_false = 0
    option_true = 1
    default = 0

class AllowProgressionInLab(Choice):
    """If any progression gets placed in the Treatment Facility, it can cause some lengthy BK. 
    This option seeks to avoid that.

    False: (Default) The only progression in Treatment Facility -- and the final fight area(s) -- will be any static progression items that are placed there by RE0.
    True: Progression can be placed in Laboratory and the final fight area(s). This can, but won't always, lead to some BK.

    NOTE - This option only affects *YOUR* Laboratory. Your progression can still be in someone else's Laboratory if they have this option enabled."""
    display_name = "Allow Progression in Laboratory"
    option_false = 0
    option_true = 1
    default = 0







    

# making this mixin so we can keep actual game options separate from AP core options that we want enabled
# not sure why this isn't a mixin in core atm, anyways
@dataclass
class StartInventoryFromPoolMixin:
    start_inventory_from_pool: StartInventoryPool

@dataclass
class RE0Options(StartInventoryFromPoolMixin, DeathLinkMixin, PerGameCommonOptions):
    character: Character
    difficulty: Difficulty
    bonus_start: BonusStart
    allow_progression_in_lab: AllowProgressionInLab
    #early_weapon_for_chris: EarlyWeaponforChris




