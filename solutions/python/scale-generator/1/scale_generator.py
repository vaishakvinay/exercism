class Scale:
    def __init__(self, tonic):
        # Preserve original for flat/sharp decision
        original = tonic

        # Normalize tonic for output
        tonic = tonic[0].upper() + tonic[1:]
        self.tonic = tonic

        # Chromatic scales
        self._sharp_scale = [
            "A", "A#", "B", "C", "C#", "D",
            "D#", "E", "F", "F#", "G", "G#"
        ]

        self._flat_scale = [
            "A", "Bb", "B", "C", "Db", "D",
            "Eb", "E", "F", "Gb", "G", "Ab"
        ]

        # Keys that must use flats (from problem table)
        flat_keys = {
            "F", "Bb", "Eb", "Ab", "Db", "Gb",
            "d", "g", "c", "f", "bb", "eb"
        }

        if original in flat_keys:
            self.scale = self._flat_scale
        else:
            self.scale = self._sharp_scale

    def chromatic(self):
        index = self.scale.index(self.tonic)
        return self.scale[index:] + self.scale[:index]

    def interval(self, intervals):
        chromatic_scale = self.chromatic()

        steps = {
            "m": 1,
            "M": 2,
            "A": 3
        }

        result = [chromatic_scale[0]]
        index = 0

        for letter in intervals:
            index = (index + steps[letter]) % 12
            result.append(chromatic_scale[index])

        return result
