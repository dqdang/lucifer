from bs4 import BeautifulSoup
import os
import requests
from lucifer import models


def build_database():
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Referer': 'http://www.puzzledragonx.com/en/multiplayer-dungeons.asp',
    }

    response = requests.get(
        'http://www.puzzledragonx.com/en/normal-dungeons.asp', headers=headers, verify=False)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        all_dungeons = soup.find_all("tr")
        for row in all_dungeons:
            dungeon = row.find("td", class_="dungeon")
            if dungeon:
                dungeon_name = dungeon.get_text()

                # First column in table of dungeon info
                stamina_column = dungeon.find_next("td")
                try:
                    stamina = stamina_column.find("span").get_text()
                except Exception as e:
                    stamina = None

                # Fifth column in table of dungeon info
                experience_column = dungeon.find_next("td").find_next(
                    "td").find_next("td").find_next("td")
                try:
                    test_for_valid_experience = int(
                        experience_column.get_text())
                    experience = experience_column.find(
                        "span").get("title").split(" - ")[0]
                except Exception as e:
                    experience = None
                if stamina and experience:
                    dungeon_entry = models.Dungeon(
                        dungeon_type="normal", dungeon_name=dungeon_name, experience=experience, stamina=stamina)
                    dungeon_entry.save()

    response = requests.get(
        'http://www.puzzledragonx.com/en/technical-dungeons.asp', headers=headers, verify=False)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        all_dungeons = soup.find_all("tr")
        for row in all_dungeons:
            dungeon = row.find("td", class_="dungeon")
            if dungeon:
                dungeon_name = dungeon.get_text()

                # First column in table of dungeon info
                stamina_column = dungeon.find_next("td")
                try:
                    stamina = stamina_column.find("span").get_text()
                except Exception as e:
                    stamina = None

                # Fifth column in table of dungeon info
                experience_column = dungeon.find_next("td").find_next(
                    "td").find_next("td").find_next("td")
                try:
                    test_for_valid_experience = int(
                        experience_column.get_text())
                    experience = experience_column.find(
                        "span").get("title").split(" - ")[0]
                except Exception as e:
                    experience = None
                if stamina and experience:
                    dungeon_entry = models.Dungeon(
                        dungeon_type="technical", dungeon_name=dungeon_name, experience=experience, stamina=stamina)
                    dungeon_entry.save()

    response = requests.get(
        'http://www.puzzledragonx.com/en/special-dungeons.asp', headers=headers, verify=False)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        all_dungeons = soup.find_all("tr")
        for row in all_dungeons:
            dungeon = row.find("td", class_="dungeon")
            if dungeon:
                dungeon_name = dungeon.get_text()

                # First column in table of dungeon info
                stamina_column = dungeon.find_next("td")
                try:
                    stamina = stamina_column.find("span").get_text()
                except Exception as e:
                    stamina = None

                # Fifth column in table of dungeon info
                experience_column = dungeon.find_next("td").find_next(
                    "td").find_next("td").find_next("td")
                try:
                    test_for_valid_experience = int(
                        experience_column.get_text())
                    experience = experience_column.find(
                        "span").get("title").split(" - ")[0]
                except Exception as e:
                    experience = None
                if stamina and experience:
                    dungeon_entry = models.Dungeon(
                        dungeon_type="special", dungeon_name=dungeon_name, experience=experience, stamina=stamina)
                    dungeon_entry.save()


def update():
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Referer': 'http://www.puzzledragonx.com/en/multiplayer-dungeons.asp',
    }

    response = requests.get(
        'http://www.puzzledragonx.com/en/normal-dungeons.asp', headers=headers, verify=False)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        all_dungeons = soup.find_all("tr")
        for row in all_dungeons:
            dungeon = row.find("td", class_="dungeon")
            if dungeon:
                dungeon_name = dungeon.get_text()
                if not models.Dungeon.objects.filter(dungeon_name=dungeon_name).exists():
                    # First column in table of dungeon info
                    stamina_column = dungeon.find_next("td")
                    try:
                        stamina = stamina_column.find("span").get_text()
                    except Exception as e:
                        stamina = None

                    # Fifth column in table of dungeon info
                    experience_column = dungeon.find_next("td").find_next(
                        "td").find_next("td").find_next("td")
                    try:
                        test_for_valid_experience = int(
                            experience_column.get_text())
                        experience = experience_column.find(
                            "span").get("title").split(" - ")[0]
                    except Exception as e:
                        experience = None
                    if stamina and experience:
                        dungeon_entry = models.Dungeon(
                            dungeon_type="normal", dungeon_name=dungeon_name, experience=experience, stamina=stamina)
                        dungeon_entry.save()

    response = requests.get(
        'http://www.puzzledragonx.com/en/technical-dungeons.asp', headers=headers, verify=False)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        all_dungeons = soup.find_all("tr")
        for row in all_dungeons:
            dungeon = row.find("td", class_="dungeon")
            if dungeon:
                dungeon_name = dungeon.get_text()
                if not models.Dungeon.objects.filter(dungeon_name=dungeon_name).exists():
                    # First column in table of dungeon info
                    stamina_column = dungeon.find_next("td")
                    try:
                        stamina = stamina_column.find("span").get_text()
                    except Exception as e:
                        stamina = None

                    # Fifth column in table of dungeon info
                    experience_column = dungeon.find_next("td").find_next(
                        "td").find_next("td").find_next("td")
                    try:
                        test_for_valid_experience = int(
                            experience_column.get_text())
                        experience = experience_column.find(
                            "span").get("title").split(" - ")[0]
                    except Exception as e:
                        experience = None
                    if stamina and experience:
                        dungeon_entry = models.Dungeon(
                            dungeon_type="technical", dungeon_name=dungeon_name, experience=experience, stamina=stamina)
                        dungeon_entry.save()

    response = requests.get(
        'http://www.puzzledragonx.com/en/special-dungeons.asp', headers=headers, verify=False)

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        all_dungeons = soup.find_all("tr")
        for row in all_dungeons:
            dungeon = row.find("td", class_="dungeon")
            if dungeon:
                dungeon_name = dungeon.get_text()
                if not models.Dungeon.objects.filter(dungeon_name=dungeon_name).exists():
                    # First column in table of dungeon info
                    stamina_column = dungeon.find_next("td")
                    try:
                        stamina = stamina_column.find("span").get_text()
                    except Exception as e:
                        stamina = None

                    # Fifth column in table of dungeon info
                    experience_column = dungeon.find_next("td").find_next(
                        "td").find_next("td").find_next("td")
                    try:
                        test_for_valid_experience = int(
                            experience_column.get_text())
                        experience = experience_column.find(
                            "span").get("title").split(" - ")[0]
                    except Exception as e:
                        experience = None
                    if stamina and experience:
                        dungeon_entry = models.Dungeon(
                            dungeon_type="special", dungeon_name=dungeon_name, experience=experience, stamina=stamina)
                        dungeon_entry.save()


def main():
    build_database()


if __name__ == "__main__":
    main()
