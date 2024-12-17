# Pandukabhaya

Pandukabhaya is an ASCII to Unicode text converter. Currently, it only supports the 'FM Abhaya' ASCII Sinhala font, but other font mappings will be added in the future. Pandukabhaya is written as a generic text conversion tool that uses JSON mappings to transform text. Therefore, it can be used to convert any text given the mapping.

## Name
The most famous Sinhala ASCII font is 'FM Abhaya' named after King Abhaya (474 BCE to 454 BCE). The tool is named after his nephew, who was named after King Abhaya and King Panduvasdeva. Pandukabhaya accended to the throne replacing Abhaya (technically Tissa succeeded to the throne right after Abhaya. But we chose the most notable successor 😀)

## Features

- A iteratively generated mapping file for 'FM Abhaya' font.
- Loads mappings from JSON files for flexibility.
- Command-line interface for quick and easy usage.

## Folder Structure and Explanations
```
PANDUKABHAYA/
├── mappings/
│   └── fm_abhaya.json
├── pandukabhaya/
│   ├── cli.py
│   └── converter.py
├── scripts/
│   ├── generation.ipynb
│   ├── prep.ipynb
└── tests/
    ├── test_cases.json
    └── test_converter.py
```

* `mappings/`: Contains mapping files.
* `pandukabhaya/`: Core package directory containing the simple code modules (cli.py, converter.py)
* `scripts/`: Contains Jupyter notebooks and mapping files for data analysis, preparation, and generation processes.
    * prep.ipynb - Cleans and corrects the UCSC mapping file.
    * generation.ipynb - Using improved UCSC mappings as a guide, generates mappings iteratively
* `tests/`: Contains unit test scripts and test data to ensure code quality and functionality.


## Usage

### As a CLI Tool
```bash
pandukabhaya <mapping_name> <text>
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