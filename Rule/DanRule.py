from Rule.RuleBase import RuleBase


class DanRule(RuleBase):
    """单投注"""

    def __init__(self, game):
        RuleBase.__init__(self, game)
        self.start_count = 4
        pass

    def get_rule_name(self):
        return "单投注"

    def check_count(self):
        current_round = self.game.currentRound
        if current_round is None:
            return

        if current_round.value % 2 == 1:
            self.count += 1
        else:
            self.count = 0

    def get_data(self):
        next_round = self.game.nextStartRound
        game_name = self.game.get_game_name()
        content = ("jxy_parameter=%7B%22fun%22%3A%22lottery%22%2C%22c%22%3A%22quiz%22%2C%22items%22%3A%22{0}" + \
                   "%22%2C%22lssue%22%3A%22{1}" + "%22%2C%22lotteryData%22%3A%5B").format(game_name, next_round.id)
        for i in range(len(RuleBase.ALL_VALUES)):
            if i % 2 == 1:
                content += "%22{0}%22%2C".format(RuleBase.ALL_VALUES[i])
            else:
                content += "%22{0}%22%2C".format(0)
        content = content[0:-3] + "%5D%7D"
        return content
