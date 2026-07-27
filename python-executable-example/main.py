import click
import psutil

@click.command()
@click.option('--threshold', type=int, default=80, help='Threshold for disk usage percentage')
def disk_usage(threshold):

    click.secho("-- Disk Check --", fg="yellow", bold=True)

    # Disk space information
    disk_use = psutil.disk_usage('/')
    hr = round(disk_use.free / (1024 ** 3), 2)
    # Display free disk space, added confirm just for reference
    if click.confirm(f"Do you want to see the free disk space?"):
        click.secho(f"Free disk space: {hr} GB", fg="blue", bold=True)

    # Check if disk usage exceeds the threshold
    if click.confirm(f"Do you want to see the disk usage information?"):
        if disk_use.percent > threshold:
            click.secho(f"Warning: Disk usage is above {threshold}%!", fg="red", bold=True)
        else:
            click.secho(f"{disk_use.percent}% used of total", fg="green", bold=True)

def main():
    disk_usage()

if __name__ == '__main__':
    main()