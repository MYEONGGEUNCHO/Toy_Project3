import click

@click.group()
def main():
    """"""
@main.command()
@click.option('-var1', default=2)
@click.option('-var2', default=1)
def add(var1, var2):
    """덧셈함수
    """
    from batch.celery.tasks.calculator import add
    add(x=var1, y=var2)

@main.command()
@click.option('-var1', default=2)
@click.option('-var2', default=1)
def mul(var1, var2):
    """곱셈함수
    """
    from batch.celery.tasks.calculator import mul
    mul(x=var1, y=var2)



if __name__ == '__main':
    main()