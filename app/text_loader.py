import click


class TextLoader:
    def load_bulk_text(self):
        click.echo("Enter text (empty line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        return "\n".join(lines)
