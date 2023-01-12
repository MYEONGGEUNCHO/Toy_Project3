import click


'''Nesting Commands 1'''
# @click.group()
# def cli():
#     pass

# @click.command()
# def initdb():
#     click.echo('Initialized the database')

# @click.command()
# def dropdb():
#     click.echo('Dropped the database')
    
# cli.add_command(initdb)
# cli.add_command(dropdb)
    
'''Nesting Commands 2'''
@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')
    


if __name__ == '__main__':
    cli()