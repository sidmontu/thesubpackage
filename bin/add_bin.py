import typer

from thesubpackage.add import add

def _main(op0:int, op1: int):

    result = add(op0, op1)
    print("Result = %d" % (result))

if __name__ == "__main__":
    typer.run(_main)

    
