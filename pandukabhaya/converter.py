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
        self.font = None
        self.singles = {}
        self.combos = {}
        self.regex_pattern = None

        self._load_mapping()

    def _load_mapping(self):
        """
        Loads the JSON mapping file and sets up the mappings.
        """
        if not os.path.exists(self.mapping_file):
            raise FileNotFoundError(f"Mapping file '{self.mapping_file}' not found.")

        with open(self.mapping_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.font = data.get("font")
        mappings = data["mappings"]

        # Build a regex pattern that matches combos first, then singles
        all_mappings = {**mappings.get("combos", {}), **mappings.get("singles", {})}
        self.regex_pattern = re.compile(
            "|".join(
                re.escape(key) for key in sorted(all_mappings, key=len, reverse=True)
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
