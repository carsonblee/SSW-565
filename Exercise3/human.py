class Human:
    def __init__(self, profession):
        self._SetProfession(profession)
    
    def _SetProfession(self, profession):     
        self._profession = profession

    def GetProfession(self):
        return self._profession

    