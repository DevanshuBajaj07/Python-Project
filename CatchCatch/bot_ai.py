# bot_ai.py

from typing import List, Any


class SimpleCatchBot:
    """
    A simple rule-based bot for CatchGame.

    decide(...) returns:
      -1 -> move left
       0 -> stay
      +1 -> move right
    """

    def __init__(self, deadzone: float = 5.0):
        # deadzone = small tolerance so bot doesn't jitter when aligned
        self.deadzone = deadzone

    def _choose_target(self, objects: List[Any]):
        """Pick which falling object to chase."""
        if not objects:
            return None

        # Prefer good / reward objects
        good_types = {"good", "bonus", "double"}
        candidates = [o for o in objects if getattr(o, "obj_type", None) in good_types]

        if not candidates:
            # If there are only bad/slow ones, just pick the lowest on screen
            candidates = objects

        # Pick the object that is lowest (largest y) => most urgent
        return max(candidates, key=lambda o: o.y)

    def decide(
        self,
        player_x: float,
        player_width: float,
        objects: List[Any],
        screen_width: int,
    ) -> int:
        """
        Decide movement direction:
          -1 for left, 0 for no move, +1 for right.
        """
        target = self._choose_target(objects)
        if target is None:
            return 0

        player_center = player_x + player_width / 2
        target_center = target.x + target.size / 2

        # If target is to the right of player center -> move right
        if player_center < target_center - self.deadzone:
            return +1
        # If target is to the left -> move left
        elif player_center > target_center + self.deadzone:
            return -1
        else:
            return 0  # close enough, don't move
