from __future__ import annotations

import logging
from random import Random
from typing import TYPE_CHECKING
from .ordered import (
    OrderedCrosser,
)

if TYPE_CHECKING:
    from typing import (
        Optional,
    )
    from ....models import (
        PlannedTrip,
    )

logger = logging.getLogger(__name__)


class RandomizedCrosser(OrderedCrosser):

    def __init__(self, randomized_size: int = 3, seed: int = 56, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.randomized_size = randomized_size
        self.random = Random(seed)

    def get_planned_trip(self) -> Optional[PlannedTrip]:
        if len(self.ranking) == 0:
            return None

        candidates = list()
        for sub_ranking in self.ranking.values():
            if len(sub_ranking) == 0:
                continue
            for current in sub_ranking.values():
                if len(candidates) != 0:
                    best = self.objective.best_planned_trip(candidates[-1], current)
                    if not best != candidates[-1]:
                        break

                if self.randomized_size < len(candidates):
                    candidates.pop()
                candidates.append(current)
            candidates.sort(key=lambda pt: self.objective.planned_trip_scoring_function(pt))
        if len(candidates) == 0:
            return None
        best = self.random.choice(candidates)
        return best
