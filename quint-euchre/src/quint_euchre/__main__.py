"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Quint Euchre."""


if __name__ == "__main__":
    main(prog_name="quint-euchre")  # pragma: no cover
