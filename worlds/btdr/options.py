from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class IncludeDelaSections(Toggle):
    """
    Includes Dela's section of the game. 
    It's unlock will need to be found in the Multiworld.
    """

    display_name = "Include Dela Sections"

class IncludeMapCompletion(Toggle):
    """
    Includes map completion of each floor and it's rewards as locations.
    """

    display_name = "Include Map Completion"

class MapCompletionPercentRequired(Range):
    """
    How much the map of each floor needs to be completed.
    This option requires 'Include Map Completion' to work.
    Please note, the map percentage in the game is precisely down the hundredths of a percent, the options don't properly reflect that.
    E.G. '5000' will require 50.00% map completion in-game.
    """

    display_name = "Map Completion Percent Required"
    
    range_start = 1
    range_end = 10000

    default = 5000

@dataclass
class BrandishTheDarkRevenantOptions(PerGameCommonOptions):
    include_dela_sections: IncludeDelaSections
    include_map_completion: IncludeMapCompletion
    map_completion_percent_required: MapCompletionPercentRequired