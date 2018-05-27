# Welcome to the World Cup Simulator

This world cup simulator makes some simple assumptions about the FIFA world ranking total points to calculate the probabilities of an outcome between two teams meeting.

The rankings and points are taken from here, and are provided in the appropriate csv for the 2018 world cup in Russia.
http://www.fifa.com/fifa-world-ranking/ranking-table/men/index.html

Put simply, the chances of a team to win is calculated using the largest gap between FIFA points (1080 gap between Germany and Saudi Arabia), and my perception of what Saudi's chances are.

I decided that, should Germany play Saudi Arabia 100 times, Saudi would win once, and draw twice. Furthermore, I decided that two teams meeting with no difference in rankings at a neutral venue would have an equal chance of winning. From 100 games, there would be 30 draws, and 35 wins each. Using a linear expression, the win conditions from equal ranking delta to extreme ranking delta is then derived.
When draws are not allowed, the equal outcome would be 50:50, and the heavily skewed would be 1.5:98.5.
A similar approach is then employed for the goals scored. For teams with equal delta, it is assumed the most likely outcome is 2 goals to either side, and a draw potential of up to 4-4. For the Germany vs Saudia Arabia extreme, it is assumed that the most likely draw would be a 0-0, Germany would win by up to 5, and for Saudi to win, it would be a 1-0 upset. Similar linear patterns are then derived and applied. 
This logic is then simulated with all the actual fixtures from a world cup format.

The "reporting" flag can be set to True in order to see a nice print out of all the games and scores, including group tables. Set to False to just return the Team class instance of the champions.

The usage is as simple as `world_cup_simulator(reporting=True)`.

Have fun!
Jamie
