import builtins
import os

import rich
import typer
from rich.console import Console

from az_ai import util

console = Console()
app = typer.Typer()


@app.command()
def tail():
    """
    Show from the currently running Azure Container Apps Replica
    """
    resource_group_name = os.environ.get("AZURE_RESOURCE_GROUP")
    console.print(f"Resource group name: {resource_group_name}")
    if not resource_group_name:
        console.print("AZURE_RESOURCE_GROUP environment variable is not set.")
        raise typer.Exit(1)
    containerapp_names = util.invoke_az_module(
            "containerapp",
            "list",
            "--resource-group",
            resource_group_name,
            "--query",
            "[?contains(name, 'backend')].name",
    )
    console.print(f"Container app name: {containerapp_names}")
    if len(containerapp_names) == 0:
        console.print("No container app found in the resource group.")
    containerapp_name = containerapp_names[0]
    # hack: use rich.print_json instead of builtins.print to 
    # colorize the output of invoke_az_module
    builtins.print = rich.print_json
    util.invoke_az_module(
        "containerapp",
        "logs",
        "show",
        "--resource-group",
        resource_group_name,
        "--name",
        containerapp_name,
        "--container",
        "main",
        "--type",
        "console",
        "--follow"
     )