import json
import os
import re


class Converter:
    def __init__(self, mapping="fm_abhaya"):
        """
        Initializes the Converter with the given font mapping.

        :param mapping: Name of the mapping file (without extension) to load from the 'mappings' directory.
        """
        self.mapping_file = os.path.join(os.path.dirname(__file__), "mappings", f"{mapping}.json")
        self.metadata = {}
        self.singles = {}
        self.combos = {}
        self.letters_pattern = None
        self.rules_pattern = None
        self.letter_mappings = None
        self.rule_mappings = None
        self._load_mapping()

    def _load_mapping(self):
        """
        Loads the JSON mapping file and sets up the mappings.
        """
        if not os.path.exists(self.mapping_file):
            raise FileNotFoundError(f"Mapping file '{self.mapping_file}' not found.")

        with open(self.mapping_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.metadata = data.get("metadata")
        self.rule_mappings = data.get("mappings", {}).get("rules", None)
        self.singles = data.get("mappings", {}).get("singles", {})
        self.combos = data.get("mappings", {}).get("combos", {})

        # Build a regex pattern that matches combos first, then singles
        all_mappings = {**self.singles, **self.combos}
        self.letters_pattern = re.compile(
            "|".join(
                re.escape(key)
                for key in sorted(
                    all_mappings,
                    key=lambda x: len(x),
                    reverse=True,
                )
            )
        )
        self.letter_mappings = all_mappings

        if self.rule_mappings:
            self.rules_pattern = re.compile(
                "|".join(re.escape(key) for key in self.rule_mappings.keys())
            )

    def convert(self, text):
        """
        Converts the input text to unicode using the loaded mapping.

        :param text: The input string to convert.
        :return: The unicode string.
        """
        if self.rules_pattern:
            text = self.rules_pattern.sub(
                lambda x: self.rule_mappings[x.group(0)], text
            )

        return self.letters_pattern.sub(
            lambda x: self.letter_mappings[x.group(0)], text
        )


# Only for testing
if __name__ == "__main__":
    converter = Converter("fm_abhaya")
    input_text = "rkaosl"
    output_text = converter.convert(input_text)
    print(f"Converted text: {output_text}")
