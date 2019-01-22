from os.path import basename, isfile
import click
from ocr_check_nld import Check


@click.command()
@click.argument("check_path")
@click.argument("check_lang")
def cli(check_path, check_lang):
    if not isfile(check_path):
        print("The file \"{:s}\" does not exist!".format(check_path))
        return
        
    check = Check(check_path, check_lang)
    total = check.get_total()
    print("Total of \"{:s}\" is {:.2f}".format(basename(check_path), total))

    
if __name__ == "__main__":
    cli()
