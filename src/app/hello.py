import click

'''Echoing'''
# @click.command()
# def hello():
    ## hello 찍기
    # click.echo('Hello World!')
    ## 유니코드 출력을 지원
    # click.echo(b'\xe2\x98\x83', nl=False)
    # 
    # click.echo('Hello World!', err=True)
    ## ANSI 색상 -  style()함수 이용
    # click.echo(click.style('Hello World!', fg='magenta'))
    # click.echo(click.style('Some more text', bg='red', fg='white'))
    # click.echo(click.style('ATTENTION', blink=True, bold=True))
    ## ANSI 색상 - secho에도  style()함수 이용
    # click.secho('Hello World!', fg='green')
    # click.secho('Some more text', bg='blue', fg='white')
    # click.secho('ATTENTION', blink=True, bold=True)
    
    # pass


''' Adding Parameters '''
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


    
if __name__ == '__main__':
    hello()