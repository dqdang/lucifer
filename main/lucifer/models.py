from django.db import models

class Dungeon(models.Model):
    dungeon_type = models.CharField(max_length=16)
    dungeon_name = models.CharField(max_length=200)
    experience = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
    def __str__(self):
        return self.dungeon_type + ", " + self.dungeon_name + ", " + str(self.stamina) + ", " + str(self.experience)
