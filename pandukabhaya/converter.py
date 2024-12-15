import json
import os
import re


class Converter:
    def __init__(self, mapping="fm_abhaya"):
        """
        Initializes the Converter with the given font mapping.

        :param mapping: Name of the mapping file (without extension) to load from the 'mappings' directory.
        """
        self.mapping_file = os.path.join("mappings", f"{mapping}.json")
        self.metadata = {}
        self.rules = {}
        self.singles = {}
        self.combos = {}
        self.regex_pattern = None
        self.mappings = None
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
        self.rules = data.get("mappings", {}).get("rules", {})
        self.singles = data.get("mappings", {}).get("singles", {})
        self.combos = data.get("mappings", {}).get("combos", {})

        # Build a regex pattern that matches rules first, then combos and last singles
        all_mappings = {**self.rules, **self.singles, **self.combos}
        self.regex_pattern = re.compile(
            "|".join(
                re.escape(key)
                for key in sorted(
                    all_mappings,
                    key=lambda x: True if x in self.rules else len(x),
                    reverse=True,
                )
            )
        )
        self.mappings = all_mappings

    def convert(self, text):
        """
        Converts the input text to unicode using the loaded mapping.

        :param text: The input string to convert.
        :return: The unicode string.
        """

        def replacer(match):
            return self.mappings[match.group(0)]

        return self.regex_pattern.sub(replacer, text)
