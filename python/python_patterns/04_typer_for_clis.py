'''
    Problem: create a python app as cli (with sub commands and arguments)
    Solution: use Type module
'''
import typer
from  enum import Enum

app = typer.Typer()
s3 = typer.Typer()
eks = typer.Typer()
app.add_typer(s3, name="s3")
app.add_typer(eks, name="eks")



class Command1ArgValues(Enum):
    option_a = "option_a"
    option_b = "option_b"



# python 04_typer_for_clis.py command1 option_b
# make the param requited and specific values
@app.command()
def command1(arg1: Command1ArgValues):
    print(f"Executing command1 with arg {arg1}")


# python 04_typer_for_clis.py s3 upload /that/to/s3.csv
@s3.command()
def upload(target_path):
    print(f"Uploading data to {target_path}")

if __name__ == "__main__":
    app()