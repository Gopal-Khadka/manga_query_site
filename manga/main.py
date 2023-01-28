from flask import Flask, render_template
from mangas import Manga
import requests


def get_auth_genre(manga):
    value_list = []
    if manga != None:
        for value in manga:
            value_list.append(value.get("name").title())
        final_value = str(value_list).replace("[", "").replace("]", "").replace("'", "")
        return final_value


app = Flask(__name__)


@app.route("/")
def show_example():
    return render_template("index.html")


@app.route("/<content>/<title>")
def show_mangas(content, title):
    content = "manga" if "m" in content[0:3] else "anime"
    api_url = f"https://api.jikan.moe/v4/{content}"
    param = {
        "q": title,
    }
    mangas = requests.get(url=api_url, params=param).json().get("data")
    manga_objects = []
    list = []
    for manga in mangas:
        mal_url = manga.get("url")
        small_image = manga["images"]["jpg"].get("image_url")
        title = manga.get("title")
        title_en = manga.get("title_english", "N/A")
        title_syn = str(manga.get("title_synonyms", "N/A")).replace("[]", "N/A")
        type = manga.get("type")
        if content == "manga":
            chapters = manga.get("chapters")
            volumes = manga.get("volumes")
            authors = get_auth_genre(manga.get("authors"))
            release = manga["published"].get("string")
            list = ["Chapters: ", "Volumes: ", "Authors: "]
        else:
            chapters = manga.get("episodes")
            volumes = manga.get("source")
            authors = manga.get("duration")
            release = manga["aired"].get("string")
            list = ["Episodes: ", "Source: ", "Duration: "]

        status = manga.get("status")
        genre = get_auth_genre(manga.get("genres"))
        plot = manga.get("synopsis", "N/A")
        background = manga.get("background")
        mal_rank = manga.get("rank")
        manga_obj = Manga(
            image=small_image,
            url=mal_url,
            title=title,
            title_en=title_en,
            syn=title_syn,
            type=type,
            chapters=chapters,
            volumes=volumes,
            status=status,
            release=release,
            authors=authors,
            plot=plot,
            genre=genre,
            story=background,
            rank=mal_rank,
        )
        manga_objects.append(manga_obj)
    return render_template("mangas.html", mangas=manga_objects, list=list)


@app.route("/r/<content>")
def show_manga(content):
    content = "manga" if "m" in content[0:3] else "anime"
    api_url = f"https://api.jikan.moe/v4/random/{content}"
    manga = requests.get(url=api_url,).json().get("data")
    manga_objects = []
    list = []
    mal_url = manga.get("url")
    small_image = manga["images"]["jpg"].get("image_url")
    title = manga.get("title")
    title_en = manga.get("title_english", "N/A")
    title_syn = str(manga.get("title_synonyms", "N/A")).replace("[]", "N/A")
    type = manga.get("type")
    if content == "manga":
        chapters = manga.get("chapters")
        volumes = manga.get("volumes")
        authors = get_auth_genre(manga.get("authors"))
        release = manga["published"].get("string")
        list = ["Chapters: ", "Volumes: ", "Authors: "]
    else:
        chapters = manga.get("episodes")
        volumes = manga.get("source")
        authors = manga.get("duration")
        release = manga["aired"].get("string")
        list = ["Episodes: ", "Source: ", "Duration: "]

    status = manga.get("status")
    genre = get_auth_genre(manga.get("genres"))
    plot = manga.get("synopsis", "N/A")
    background = manga.get("background")
    mal_rank = manga.get("rank")
    manga_obj = Manga(
        image=small_image,
        url=mal_url,
        title=title,
        title_en=title_en,
        syn=title_syn,
        type=type,
        chapters=chapters,
        volumes=volumes,
        status=status,
        release=release,
        authors=authors,
        plot=plot,
        genre=genre,
        story=background,
        rank=mal_rank,
    )
    manga_objects.append(manga_obj)
    return render_template("mangas.html", mangas=manga_objects, list=list)


if __name__ == "__main__":
    app.run(debug=True)
