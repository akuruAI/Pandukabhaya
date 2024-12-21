import unittest
import json
from pandukabhaya import Converter
import os


class TestConverter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load test cases from the JSON file
        with open("tests/test_cases.json", "r", encoding="utf-8") as file:
            cls.test_data = json.load(file)

    def test_conversions(self):
        self.maxDiff = None
        for mapping_data in self.test_data:
            mapping_file = mapping_data["mapping"]
            test_cases = mapping_data["test_cases"]

            # Ensure the mapping file exists
            mapping_path = os.path.join(
                os.path.dirname(__file__), "../pandukabhaya/mappings", mapping_file
            )
            self.assertTrue(
                os.path.exists(mapping_path), f"Mapping file {mapping_file} not found."
            )

            # Initialize the converter with the current mapping
            converter = Converter(mapping_file.replace(".json", ""))

            for input_text, expected_output in test_cases:
                with self.subTest(mapping=mapping_file, input=input_text):
                    converted_text = converter.convert(input_text)
                    self.assertEqual(
                        converted_text,
                        expected_output,
                        f"Failed on mapping: {mapping_file}, input: {input_text}",
                    )


if __name__ == "__main__":
    unittest.main()
