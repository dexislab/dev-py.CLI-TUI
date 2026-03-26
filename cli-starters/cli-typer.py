import typer

app = typer.Typer()

def build_hello_msg(n: int):
    return f"Hello:   {n.title()} AGAIN " + "yuy!!!"

@app.command()
def hello(name):
    print(build_hello_msg(name))

@app.command()
def goodbye(name: str, surname: str | None = None, formal: bool = True):
    if formal:
        print(f"Goodbye Ms. {name} {surname}. Have a good day.")
    else:
        print(f"Bye {name} ({surname})!")


if __name__ == "__main__":
    app()
