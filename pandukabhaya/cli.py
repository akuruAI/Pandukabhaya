import argparse
from pandukabhaya import Converter


def main():
    parser = argparse.ArgumentParser(description="Convert text using custom mappings.")
    parser.add_argument(
        "mapping",
        type=str,
        help="The name of the mapping file (without .json extension) located in the 'mappings' directory.",
    )
    parser.add_argument(
        "-t",
        "--text",
        type=str,
        help="The text to convert using the specified mapping. Cannot be used with --input-file.",
        required=False,
    )
    parser.add_argument(
        "-i",
        "--input-file",
        type=str,
        help="The path to a text file to convert using the specified mapping. Cannot be used with --text.",
        required=False,
    )
    parser.add_argument(
        "-o",
        "--output-file",
        type=str,
        help="The path to save the converted text. If not provided, output will be printed to the console.",
        required=False,
    )
    args = parser.parse_args()

    if not args.text and not args.input_file:
        parser.error("Either --text or --input-file must be provided.")
    if args.text and args.input_file:
        parser.error("--text and --input-file cannot be used together.")

    try:
        converter = Converter(args.mapping)

        if args.input_file:
            with open(args.input_file, "r", encoding="utf-8") as infile:
                input_text = infile.read()
        else:
            input_text = args.text

        converted_text = converter.convert(input_text)

        if args.output_file:
            with open(args.output_file, "w", encoding="utf-8") as outfile:
                outfile.write(converted_text)
        else:
            print(converted_text)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
