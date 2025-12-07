""" Tachyon manifold related objects """
from dataclasses import dataclass, field
from enum import Enum
from typing import List

class ManifoldSlotType(Enum):
    """ Type of slot inside a tachyon manifold """
    BOX = '.'
    SPLITTER = '^'
    ENTRY = 'S'

@dataclass
class ManifoldSlot:
    """ Slot inside a tachyon manifold """
    slot_type: ManifoldSlotType
    tachyons: int = 0

    def __repr__(self):
        if self.slot_type == ManifoldSlotType.ENTRY:
            return 'S'
        if self.slot_type == ManifoldSlotType.SPLITTER:
            return '^'
        if self.slot_type == ManifoldSlotType.BOX:
            return str(self.tachyons)

class ManifoldRow:
    """ Tachyon Manifold Row """
    def __init__(self, row: str):
        self.slots = [ManifoldSlot(ManifoldSlotType(slot)) for slot in row]
        self.length = len(self.slots)
        self.splitters_triggered = 0

    def __lt__(self, other: 'ManifoldRow') -> int:
        """ Run a manifold step from other to self and return new opened timelines """
        opened_timelines = 0
        for i, slot in enumerate(self.slots):
            if slot.slot_type == ManifoldSlotType.BOX:
                slot.tachyons += other.slots[i].tachyons
            if slot.slot_type == ManifoldSlotType.SPLITTER:
                if other.slots[i].tachyons:
                    self.splitters_triggered += 1
                    self.slots[i-1].tachyons += other.slots[i].tachyons
                    self.slots[i+1].tachyons += other.slots[i].tachyons
                    opened_timelines += other.slots[i].tachyons
        return opened_timelines

    def __repr__(self):
        return ''.join(str(slot) for slot in self.slots)

class TachyonManifold:
    """ Taychon Manifold object """

    def __init__(self, diagram: str):
        self.rows = [ManifoldRow(row) for row in diagram.splitlines()]
        self.splits = 0
        self.timelines = 0

    def start(self):
        """ Absorb a tachyon into the manifold """
        for slot in self.rows[0].slots:
            if slot.slot_type == ManifoldSlotType.ENTRY:       
                self.timelines = 1
                slot.tachyons = 1
                break

        for i in range(1, len(self.rows)):
            new_timelines = self.rows[i-1] > self.rows[i]
            self.timelines += new_timelines
            self.splits += self.rows[i].splitters_triggered