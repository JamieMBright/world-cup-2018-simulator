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

# Example Output
```
               GROUP A
          RUS  1 - 0  SAU
          RUS  1 - 1  EGY
          RUS  4 - 4  URU
          SAU  1 - 0  EGY
          SAU  1 - 2  URU
          EGY  0 - 1  URU

 Group A    Form      GF       GD       Pts   
==============================================
 Uruguay   DWW      7        2        7       

 Russia    WDD      6        1        5       

 Saudi     LWL      2        -1       3       
 Arabia                                       

 Egypt     DLL      1        -2       1       


               GROUP B
          POR  1 - 0  SPA
          POR  4 - 1  MOR
          POR  3 - 1  IRA
          SPA  1 - 0  MOR
          SPA  1 - 2  IRA
          MOR  2 - 1  IRA

 Group B    Form      GF       GD       Pts   
==============================================
 Portugal  WWW      8        6        9       

 Spain     LWL      2        -1       3       

 Iran      LWL      4        -2       3       

 Morocco   LLW      3        -3       3       


               GROUP C
          FRA  1 - 1  AUS
          FRA  0 - 1  PER
          FRA  1 - 1  DEN
          AUS  0 - 1  PER
          AUS  1 - 1  DEN
          PER  1 - 0  DEN

 Group C    Form      GF       GD       Pts   
==============================================
 Peru      WWW      3        3        9       

 Denmark   DDL      2        -1       2       

 Australi  DLD      2        -1       2       
 a                                            

 France    DLD      2        -1       2       


               GROUP D
          ARG  2 - 1  ICE
          ARG  1 - 1  CRO
          ARG  1 - 3  NIG
          ICE  0 - 1  CRO
          ICE  3 - 2  NIG
          CRO  0 - 0  NIG

 Group D    Form      GF       GD       Pts   
==============================================
 Croatia   DWD      2        1        5       

 Nigeria   WLD      5        1        4       

 Argentin  WDL      4        -1       4       
 a                                            

 Iceland   LLW      4        -1       3       


               GROUP E
          BRA  1 - 0  SWI
          BRA  3 - 2  COS
          BRA  2 - 1  SER
          SWI  1 - 1  COS
          SWI  3 - 2  SER
          COS  0 - 1  SER

 Group E    Form      GF       GD       Pts   
==============================================
 Brazil    WWW      6        3        9       

 Switzerl  LDW      4        0        4       
 and                                          

 Serbia    LLW      4        -1       3       

 Costa     LDL      3        -2       1       
 Rica                                         


               GROUP F
          GER  1 - 0  MEX
          GER  2 - 1  SWE
          GER  2 - 1  SOU
          MEX  1 - 2  SWE
          MEX  1 - 2  SOU
          SWE  0 - 1  SOU

 Group F    Form      GF       GD       Pts   
==============================================
 Germany   WWW      5        3        9       

 South     LWW      4        1        6       
 Korea                                        

 Sweden    LWL      3        -1       3       

 Mexico    LLL      2        -3       0       


               GROUP G
          BEL  2 - 1  PAN
          BEL  2 - 3  TUN
          BEL  1 - 0  ENG
          PAN  1 - 0  TUN
          PAN  0 - 1  ENG
          TUN  1 - 2  ENG

 Group G    Form      GF       GD       Pts   
==============================================
 Belgium   WLW      5        1        6       

 England   LWW      3        1        6       

 Tunisia   WLL      4        -1       3       

 Panama    LWL      2        -1       3       


               GROUP H
          POL  0 - 0  SEN
          POL  0 - 0  COL
          POL  1 - 3  JAP
          SEN  1 - 0  COL
          SEN  1 - 2  JAP
          COL  0 - 0  JAP

 Group H    Form      GF       GD       Pts   
==============================================
 Japan     WWD      5        3        7       

 Senegal   DWL      2        0        4       

 Colombia  DLD      0        -1       2       

 Poland    DDL      1        -2       2       


            Round of 16
          URU  0 - 1  SPA
          PER  2 - 3  NIG
          POR  1 - 0  RUS
          CRO  1 - 0  DEN
          BRA  1 - 0  SOU
          BEL  1 - 0  SEN
          GER  3 - 2  SWI
          JAP  2 - 1  ENG

          Quarter-finals
          SPA  2 - 3  NIG
          BRA  1 - 2  BEL
          POR  0 - 1  CRO
          GER  1 - 0  JAP

            Semi-finals
          NIG  0 - 1  BEL
          CRO  0 - 1  GER

               Final
          BEL  1 - 0  GER

  Belgium are World Cup 2018 Champions!
```
