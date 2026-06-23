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
    This option requires 'Include Map Completion' to work
    """

    display_name = "Map Completion Percent Required"
    
    range_start = 1
    range_end = 100

    default = 50

@dataclass
class BrandishTheDarkRevenantOptions(PerGameCommonOptions):
    include_dela_sections: IncludeDelaSections
    include_map_completion: IncludeMapCompletion
    map_completion_percent_required: MapCompletionPercentRequired