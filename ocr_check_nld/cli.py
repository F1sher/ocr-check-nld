from os.path import basename
import click
from ocr_check_nld import Check


@click.command()
@click.argument("check_path")
@click.argument("check_lang")
def cli(check_path, check_lang):
    check = Check(check_path, check_lang)
    total = check.get_total()
    print("Total of \"{:s}\" is {:.2f}".format(basename(check_path), total))

    
if __name__ == "__main__":
    cli()
