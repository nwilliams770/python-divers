class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        result = [None] * len(deck)

        ignore_none = False
        while sorted_deck:
            for i, value in enumerate(result):
                if value is None:
                    if not ignore_none:
                        result[i] = sorted_deck.pop(0)
                    ignore_none = not ignore_none

        return result