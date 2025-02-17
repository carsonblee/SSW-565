class PairGame:
    def __init__(self):
        self.m_players = [None, None]

    def SetPlayerOne(self, player):
        self.m_players[0] = player

    def SetPlayerTwo(self, player):
        self.m_players[1] = player

    def GetNumberOfPlayers(self):
        return len([player for player in self.m_players if player is not None])

    def Play(self):
        pass