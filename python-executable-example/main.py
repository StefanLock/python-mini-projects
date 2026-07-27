import click
import psutil

@click.command()
def disk_usage():

    click.secho("-- Disk Check --", fg="green", bold=True)

    disk_use = psutil.disk_usage('/')
    hr = round(disk_use.free / (1024 ** 3), 2)
    click.echo(f"{hr}GB free disk space, \n{disk_use.percent}% used of total")

def main():
    disk_usage()

if __name__ == '__main__':
    main()