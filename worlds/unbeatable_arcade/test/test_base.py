from test.bases import WorldTestBase

from ..world import UNBEATABLEArcadeWorld

class UNBEATABLEArcadeTestBase(WorldTestBase):
    game = "UNBEATABLE Arcade"
    world: UNBEATABLEArcadeWorld