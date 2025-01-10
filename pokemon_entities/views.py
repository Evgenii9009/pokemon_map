import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    map_pokemons = PokemonEntity.objects.filter(disappeared_at__gt=localtime(), appeared_at__lt=localtime())
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in map_pokemons:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    pokemons_on_page = []
    page_pokemons = Pokemon.objects.all()
    for pokemon in page_pokemons:
        pokemons_on_page.append({'img_url': pokemon.image.url, 'pokemon_id': pokemon.id, 'title_ru': pokemon.title}) if pokemon.image else pokemons_on_page.append({'img_url': "", 'pokemon_id': pokemon.id, 'title_ru': pokemon.title})


    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        needed_pokemon = Pokemon.objects.get(id=pokemon_id)
    except:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    pokemon_on_page = {'img_url': needed_pokemon.image.url, 
                       'title_ru': needed_pokemon.title, 
                       'title_en': needed_pokemon.title_en, 
                       'title_jp': needed_pokemon.title_jp,
                       'description': needed_pokemon.description}
    if needed_pokemon.previous_evolution:
        pokemon_on_page["previous_evolution"] = {"pokemon_id": needed_pokemon.previous_evolution.id,
                                                 "img_url": needed_pokemon.previous_evolution.image.url,
                                                 "title_ru": needed_pokemon.previous_evolution.title}
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    map_pokemons = PokemonEntity.objects.filter(pokemon=pokemon_id)
    for pokemon_entity in map_pokemons:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_on_page
    })
