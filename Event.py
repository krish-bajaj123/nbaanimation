from Constant import Constant
from Moment_Info import Moment
from Team import Team
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle, Rectangle, Arc

class Event:
    """A class for handling and showing events"""

    def __init__(self, event):
        self.moments = [Moment(moment) for moment in event['moments']]
        self.player_ids_dict = self._create_player_dict(event['home']['players'] + event['visitor']['players'])

    def _create_player_dict(self, players):
        return {player['playerid']: (f"{player['firstname']} {player['lastname']}", player['jersey'])
                for player in players}

    def update_radius(self, i, player_circles, ball_circle, annotations, clock_info):
        moment = self.moments[i]
        for j, (circle, player, annotation) in enumerate(zip(player_circles, moment.players, annotations)):
            circle.center = player.x, player.y
            annotation.set_position(circle.center)
        
        clock_text = f'Quarter {moment.quarter}\n {int(moment.game_clock) % 3600 // 60:02d}:{int(moment.game_clock) % 60:02d}\n {moment.shot_clock:03.1f}'
        clock_info.set_text(clock_text)
        
        ball_circle.center = moment.ball.x, moment.ball.y
        ball_circle.radius = moment.ball.radius / Constant.NORMALIZATION_COEF
        return player_circles, ball_circle

    def show(self):
        fig, ax = plt.subplots()
        ax.set_xlim(Constant.X_MIN, Constant.X_MAX)
        ax.set_ylim(Constant.Y_MIN, Constant.Y_MAX)
        ax.axis('off')
        ax.grid(False)

        start_moment = self.moments[0]

        clock_info = ax.annotate('', xy=[Constant.X_CENTER, Constant.Y_CENTER],
                                 color='black', ha='center', va='center')

        annotations = [ax.annotate(self.player_ids_dict[player.id][1], xy=[0, 0], color='w',
                                   ha='center', va='center', fontweight='bold')
                       for player in start_moment.players]

        self._create_team_table(ax, start_moment)

        player_circles = [plt.Circle((0, 0), Constant.PLAYER_CIRCLE_SIZE, color=player.color)
                          for player in start_moment.players]
        ball_circle = plt.Circle((0, 0), Constant.PLAYER_CIRCLE_SIZE,
                                 color=start_moment.ball.color)
        
        for circle in player_circles + [ball_circle]:
            ax.add_patch(circle)

        anim = animation.FuncAnimation(
            fig, self.update_radius,
            fargs=(player_circles, ball_circle, annotations, clock_info),
            frames=len(self.moments), interval=Constant.INTERVAL)

        court = plt.imread("court.png")
        plt.imshow(court, zorder=0, extent=[Constant.X_MIN, Constant.X_MAX - Constant.DIFF,
                                            Constant.Y_MAX, Constant.Y_MIN])
        plt.show()

    def _create_team_table(self, ax, start_moment):
        sorted_players = sorted(start_moment.players, key=lambda player: player.team.id)
        
        # Assuming the first 5 players are from one team and the next 5 from another
        home_players = sorted_players[:5]
        guest_players = sorted_players[5:]
        
        home_team = home_players[0].team
        guest_team = guest_players[0].team
        
        column_labels = (home_team.name, guest_team.name)
        column_colours = (home_team.color, guest_team.color)
        
        home_player_data = [f"{self.player_ids_dict[player.id][0]} #{self.player_ids_dict[player.id][1]}" for player in home_players]
        guest_player_data = [f"{self.player_ids_dict[player.id][0]} #{self.player_ids_dict[player.id][1]}" for player in guest_players]
        players_data = list(zip(home_player_data, guest_player_data))

        table = plt.table(cellText=players_data,
                          colLabels=column_labels,
                          colColours=column_colours,
                          colWidths=[Constant.COL_WIDTH, Constant.COL_WIDTH],
                          loc='bottom',
                          cellColours=[column_colours for _ in range(5)],
                          fontsize=Constant.FONTSIZE,
                          cellLoc='center')
        table.scale(1, Constant.SCALE)
        
        # Update text color for all cells
        for key, cell in table.get_celld().items():
            cell.get_text().set_color('white')
