import click
from click_shell import shell
from library import Garden


@click.option(
    '--use-save',
    default=True,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@shell(prompt='>> ', intro='Launching cli application...')
def main(use_save):
    global garden
    garden = Garden()

    if use_save:
        garden.get_data_from_file('savings.json')


@main.command(help='Create new garden.', name='new_model')
def new_model():
    garden.get_data_from_file('data.json')


@main.command(help='To the next day.', name='next_day')
def next_day():
    garden.next_day()
    garden.set_data_in_file('savings.json')


@main.command(help='Show information about garden.', name='show')
def show():
    garden.show()
    garden.set_data_in_file('savings.json')


@main.command(help='Add garden bed.', name='add_bed')
def add_bed():
    garden.add_garden_bed()
    garden.set_data_in_file('savings.json')


@main.command(help='Plant a tree.', name='plant_tree')
@click.argument('name', type=str)
def plant_tree(name):
    garden.plant_tree(name)
    garden.set_data_in_file('savings.json')


@main.command(help='Plant a cultivated plant.', name='plant_cult')
@click.argument('name')
@click.argument('bed', type=int)
def plant_cult(name, bed):
    garden.plant_cultivated_plant(name, bed-1)
    garden.set_data_in_file('savings.json')


@main.command(help='Weed a garden bed.', name='weed')
@click.argument('bed', type=int)
def weeding(bed):
    garden.weeding(bed-1)
    garden.set_data_in_file('savings.json')


@main.command(help='Water a garden bed.', name='water')
@click.argument('bed', type=int)
def watering(bed):
    garden.watering(bed-1)
    garden.set_data_in_file('savings.json')


@main.command(help='Fertilize a plant.', name='fertilize')
@click.argument('bed', type=int)
def fertilizing(bed):
    garden.fertilize(bed-1)
    garden.set_data_in_file('savings.json')


@main.command(help='Kill pests on a plant.', name='kill_pest')
@click.argument('type_name')
@click.argument('bed', type=int)
def kill_pest(type_name, bed):
    garden.kill_pest(type_name, bed-1)
    garden.set_data_in_file('savings.json')


@main.command(help='Take harvest from a plant.', name='harvest')
@click.argument('type_name')
@click.argument('bed', type=int)
def harvesting(type_name, bed):
    garden.harvesting(type_name, bed-1)
    garden.set_data_in_file('savings.json')


@main.command(help='Treat a plant.', name='treat')
@click.argument('type_name')
@click.argument('bed', type=int)
def treatment(type_name, bed):
    garden.treatment(type_name, bed-1)
    garden.set_data_in_file('savings.json')


if __name__ == '__main__':
    main()
