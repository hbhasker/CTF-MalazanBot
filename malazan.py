import random
import os

from api import gameinfo
from api import Commander
from api import commands
from api.vector2 import Vector2

def contains(area, position):
    start, finish = area
    return position.x >= start.x and position.y >= start.y and position.x <= finish.x and position.y <= finish.y


class MalazanCommander(Commander):
    """
    Hope is to build a neural network based commander that learns with every game and improves its
    play
    """

    def initialize(self):
        """Use this function to setup your bot before the game starts."""
        self.verbose = True    # display the command descriptions next to the bot labels

    def tick(self):
        """ Process all the bots that are done with their orders and available for taking commands."""

        for bot in self.game.bots_available:
            target = random.choice(
                [f.position for f in self.game.flags.values()]
                + [s for s in self.level.flagScoreLocations.values()]
                + [self.level.findRandomFreePositionInBox(self.level.area)]
                )
            commandType  = random.choice([commands.Attack, commands.Charge])
            if target:
                self.issue(commandType, bot, target, description = 'malazan')

    def shutdown(self):
        """Use this function to teardown your bot after the game is over, or perform an
        analysis of the data accumulated during the game."""

        pass

