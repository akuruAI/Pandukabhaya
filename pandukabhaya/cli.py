import argparse
from converter import Converter

def main():
    parser = argparse.ArgumentParser(description="Convert text using custom mappings.")
    parser.add_argument(
        "mapping", 
        type=str, 
        help="The name of the mapping file (without .json extension) located in the 'mappings' directory."
    )
    parser.add_argument(
        "text", 
        type=str, 
        help="The text to convert using the specified mapping."
    )
    args = parser.parse_args()

    try:
        converter = Converter(args.mapping)
        converted_text = converter.convert(args.text)
        print(converted_text)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
