from lucifer import models


def find_efficient_dungeons(experience, stamina):
    try:
        experience = int(experience)
        current_stamina = int(stamina)
    except ValueError as e:
        return {}
    efficient_dungeons = {}
    for stamina in range(current_stamina, -1, -1):
        applicable_dungeons = models.Dungeon.objects.filter(stamina=stamina)
        for dungeon in applicable_dungeons:
            if dungeon.experience > experience:
                efficient_dungeons[dungeon.dungeon_name] = dungeon.experience
    efficient_dungeons = dict(
        sorted(efficient_dungeons.items(), key=lambda item: item[1], reverse=True))
    return efficient_dungeons
