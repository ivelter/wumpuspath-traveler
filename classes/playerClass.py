class Player:
    playerList = []
    def __init__(self, context):
        self.memberID = context.author.id
        self.memberDisplayName = context.author.name
        self.level = 1
        self.strength = 3
        self.maxHP = 10
        self.currentHP = 10
        Player.playerList.append(self)

    def __str__(self):
        return f"{self.memberDisplayName}\n - Level {self.level}\n - HP : {self.currentHP}/{self.maxHP}\n - Strength : {self.strength}"

    def shortSTR(self):
        return self.levelToEmoji() + " " + self.memberDisplayName

    def levelToEmoji(self) -> str:
        """
        Returns an emoji (str) according to the player's level. Useful for embed values.
        """
        if self.level == 1:
            return '🍃'
        elif self.level < 10:
            return '🧒'
        elif self.level < 25:
            return '🧝'
        elif self.level < 50:
            return '🧙'
        elif self.level < 100:
            return '🥷'
        return '👑'

def getPlayerByID(id):
    for p in Player.playerList:
        if p.memberID == id:
            return p
    return null