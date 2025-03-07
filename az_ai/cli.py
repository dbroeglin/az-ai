import typer
from azure.cli.core import get_default_cli
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

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


@app.command()
def az():
    typer.echo("az command")
    get_default_cli().invoke(["--version"])
