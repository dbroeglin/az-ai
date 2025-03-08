import logging

import typer
from rich.console import Console
from rich.logging import RichHandler
from rich.markdown import Markdown
from rich.table import Table

import az_ai.logs
from az_ai import util

util.load_dotenv_from_azd()


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

MARKDOWN = """
# This is an h1

## This is an h2

Rich can do a pretty *decent* job of rendering markdown.

[a link](https://github.com)
1. This is a list item
2. This is another list item

* This is a bullet list item
* This is another bullet list item

```python
print("This is a code block")
```

- [ ] This is a todo item
- [x] This is a completed todo item
"""

app = typer.Typer()
console = Console()

app.add_typer(az_ai.logs.app, name="logs", help="Show logs from the currently running Azure Container Apps Replica")


@app.command()
def hello():
    typer.echo("Hello World!")


@app.command()
def coucou():
    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)
    md = Markdown(MARKDOWN)
    console.print(md)
    from rich import print
    from rich.text import Text
    from rich.tree import Tree

    text_filename = Text("coincoin", "green")
    text_filename.highlight_regex(r"\..*$", "bold red")
    text_filename.stylize("link file://coincoin")
    tree = Tree("Rich Tree")
    tree.add("[red]Red").add("[green]Green").add("[blue]Blue")
    tree.add("coucou")
    tree.label = "root"
    tree.add(Text("🐍 ") + text_filename)

    print(tree)
