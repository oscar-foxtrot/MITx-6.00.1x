class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    
    def __str__(self):
        return self.incantation + ' ' + self.name + '\n' + self.getDescription()
       
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
