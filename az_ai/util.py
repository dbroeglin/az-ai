import io
import json
import logging
from io import StringIO
from subprocess import run

from azure.cli.core import get_default_cli
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def load_dotenv_from_azd():
    """
    Loads environment variables from Azure Developer CLI (azd) or .env file.

    Attempts to load environment variables using the azd CLI first.
    If that fails, falls back to loading from a .env file in the current directory.
    """
    result = run("azd env get-values", capture_output=True, shell=True, text=True)
    if result.returncode == 0:
        logging.info("Found AZD environment. Loading...")
        load_dotenv(stream=StringIO(result.stdout))
    else:
        logging.info("AZD environment not found. Trying to load from .env file...")
        load_dotenv()




def invoke_az_module(*arguments, output="json"):
    with io.StringIO() as out_file:
        cli = get_default_cli()
        arguments = list(arguments)
        arguments.append("--output")
        arguments.append(output)
        logger.debug("Executing command: az '%s'", "' '".join(arguments))
        exit_code = cli.invoke(arguments, out_file=out_file)

        out = out_file.getvalue()
        if exit_code != 0:
            raise Exception(f"Failed to execute ({exit_code}) command: az {arguments}. Output: {out}")
        logger.debug("Command output: '%s'", out)
        return json.loads(str(out))
