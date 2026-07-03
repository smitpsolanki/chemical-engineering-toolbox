from config import LINE_WIDTH
import textwrap
def print_header(title):
    print()
    print("=" * LINE_WIDTH)
    print(title.center(LINE_WIDTH))
    print("=" * LINE_WIDTH)
def print_section(title):
    print()
    title = title.upper()
    print(title)
    print("-" * len(title))
def print_footer():
    print("=" * LINE_WIDTH)
def print_paragraph(text):
    wrapped_text = textwrap.fill(text, width=LINE_WIDTH)
    print(wrapped_text)
def print_result(label, value, unit=""):
    if isinstance(value, float):
        value = f"{value:,.2f}"
    if unit:
        print(f"{label:<20}: {value} {unit}")
    else:
        print(f"{label:<20}: {value}")
def print_dictionary(data):
    for key, value in data.items():
        print_result(key, value)