class Player:
    playerList = []
    def __init__(self, context):
        self.memberID = context.author.id
        self.memberDisplayName = context.author.display_name
        self.level = 1
        self.strength = 1
        self.maxHP = 10
        self.currentHP = 10
        Player.playerList.append(self)

    def __str__(self):
        return f"{self.memberDisplayName}\n - Level {self.level}\n - HP : {self.currentHP}/{self.maxHP}\n - Strength : {self.strength}"