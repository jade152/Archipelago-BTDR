from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BrandishTheDarkRevenantWorld

def create_all_regions(world: BrandishTheDarkRevenantWorld) -> None:
    regions = []
    
    if world.options.include_dela_sections:
        # create and append all chests in the ex areas

    if world.options.include_map_completion:
        # each location will have the required percent needed to check the location and make the completion stone functional
        # no grass-sanity like option...for now...
        
        # create and append each area's floor map completion and the reward when playing as ares
        
        if world.options.include_dela_sections: 
            # create and append each area's floor map completion and the reward when playing as dela

    world.multiworld.regions += regions

def connect_regions(world: BrandishTheDarkRevenantWorld) -> None:
    # connect all the regions to make entrances