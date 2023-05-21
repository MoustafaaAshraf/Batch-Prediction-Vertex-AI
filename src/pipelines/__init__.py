from pathlib import Path

from jinja2 import Template


def generate_query(input_file: Path, **replacements) -> str:
    """Dynamically render a query and replace placeholders using Jinja.

    Args:
        input_file (Path): Input file containing the query to be read.
        replacements: Keyword arguments to use to replace placeholders.

    Returns:
        str: Replaced content of the input file
    """
    with open(input_file, "r") as f:
        q_template = f.read()

    return Template(q_template).render(replacements)
