from pairgame import PairGame

class Chess(PairGame):
    def Play(self):
        player1_profession = self.m_players[0].GetProfession()
        player2_profession = self.m_players[1].GetProfession()
        print(f"{player1_profession} and {player2_profession} are playing Chess.")
