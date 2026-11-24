"""Print the two-line everyday-things entry for the make.fun bounty."""

from pathlib import Path


def load_entry() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8").strip()
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 2:
        raise ValueError("entry.txt must hold exactly two lines")
    return "\n".join(lines)


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
