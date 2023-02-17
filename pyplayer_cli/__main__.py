#!/usr/bin/env python
"""Command-line interface."""
import click
from rich import traceback
import requests
import webbrowser


@click.command()
@click.version_option(version="1.1.0", message=click.style("pyplayer-cli Version: 1.1.0"))
@click.argument('type_arg')
@click.argument('name')
def main(type_arg, name) -> None:
    if(type_arg == 'movie'):
        movie(name)
    elif(type_arg == 'tv'):
        tv('breaking bad', 1, 3)

def movie(name):
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=87d5585a5497b373679e8bdc7d6f0d22&query={name}\"")
    request = response.json()
    result_list = request.get("results")
    id_list = []
    
    for i in range(len(result_list)):
        result_first = result_list[i]
        print(f"[{str(i)}]\t{str(result_first.get('original_title'))}")
        id_list.append(str(result_first.get('id')))
    
    play = int(input("\nSelect a movie [type number]: "))
    print(id_list[play])
    webbrowser.open(f"https://vidsrc.me/embed/{str(id_list[play])}")


def tv(name, season, episode):
    pass

if __name__ == "__main__":
    traceback.install()
    main(prog_name="pyplayer-cli")  # pragma: no cover