import click
import os
import robin_stocks.robinhood as rh
from robinhood import controller

@click.group()
@click.option("--username", help="Robinhood username", required=False)
@click.option("--password", help="Robinhood password", required=False)
@click.option("--mfa_code", help="Robinhood MFS Code", required=False)
@click.pass_context
def main(ctx, username: str = "", password: str = "", mfa_code: str = ""):
    '''
    Welcome to Robindata! Your finance smart tool for getting insights from your Robinhood data.
    '''
    ctx.obj = {}
    ctx.obj["password"] = password if password != "" else os.getenv('RH_PASS')
    ctx.obj["username"] = username if username != "" else os.getenv('RH_USER')
    ctx.obj["mfa_code"] = mfa_code if mfa_code != "" else os.getenv('RH_MFA')

@main.command()
@click.pass_context
def login(ctx):
    '''
    This command will execute a Robinhood login.

    :return:
    '''

    login = rh.login(ctx.obj['username'],ctx.obj['password'])

    if login:
        click.echo("Logged In")
    else:
        click.echo("LogIn Failed")

@main.command()
#@click.argument('file', type=click.File('w'), default='./robinhood_transactions.csv', required=False)
@click.pass_context
def export_transactions(ctx):
    '''
    This command will export all your Robinhood transactions to a CSV file.

    iF you do not inform the file path and name, it will generate a file in the current directory called: robinhood_transactions.csv

    :return:
    '''
    login = rh.login(ctx.obj['username'],ctx.obj['password'])
    rc = controller.Controller()
    transactions = rc.get_all_transactions()
    for item in transactions:
        print(item.symbol)

if __name__ == '__main__':
    main()
