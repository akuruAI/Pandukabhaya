# Pandukabhaya

Pandukabhaya is an ASCII to Unicode text converter. Currently, it only supports the 'FM Abhaya' ASCII Sinhala font, but other font mappings will be added in the future. Pandukabhaya is written as a generic text conversion tool that uses JSON mappings to transform text. Therefore, it can be used to convert any text given the mapping.

## Name
The most famous Sinhala ASCII font is 'FM Abhaya' named after King Abhaya (474 BCE to 454 BCE). The tool is named after his nephew, who was named after King Abhaya and King Panduvasdeva. Pandukabhaya accended to the throne replacing Abhaya (technically Tissa succeeded to the throne right after Abhaya. But we chose the most notable successor 😀)

## Features

- A iteratively generated mapping file for 'FM Abhaya' font.
- Loads mappings from JSON files for flexibility.
- Command-line interface for quick and easy usage.

## Installation
Package is pending release in Pypi. For now clone the repository and install from the clone.
```bash
pip install pandukabhaya
```

## Usage

### As a CLI Tool
```bash
pandukabhaya <mapping_name> -t <text>
```
```bash
pandukabhaya <mapping_name> -t <text> -o <output_file>
```
```bash
pandukabhaya <mapping_name> -i <input_file> -o <output_file>
```

### As a Python Module
```python
from pandukabhaya import Converter

converter = Converter("fm_abhaya")
output = converter.convert("rkaosl")
print(output)
```
### Run tests
```bash
python -m unittest tests.test_converter
```

## Folder Structure and Explanations
```
PANDUKABHAYA/
├── pandukabhaya/
│   ├── cli.py
│   ├── converter.py
│   └── mappings/
│       └── fm_abhaya.json
├── scripts/
│   ├── generation.ipynb
│   └── prep.ipynb
└── tests/
    ├── test_cases.json
    └── test_converter.py
```

* `pandukabhaya/`: Core package directory containing the simple code modules (cli.py, converter.py)
    * `mappings/`: Contains mapping files.
* `scripts/`: Contains Jupyter notebooks and mapping files for data analysis, preparation, and generation processes.
    * prep.ipynb - Cleans and corrects the UCSC mapping file.
    * generation.ipynb - Using improved UCSC mappings as a guide, generates mappings iteratively
* `tests/`: Contains unit test scripts and test data to ensure code quality and functionality.