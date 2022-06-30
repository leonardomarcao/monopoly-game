# Monopoly game

![Monopoly](https://img.shields.io/badge/Monopoly-v1.0-green.svg?style=flat-square)
![Open Source Love](https://img.shields.io/badge/Open%20Source-Love-blue.svg?style=flat-square)

## Summary

* [Game](#game)
  * [Rules](#rules)
  * [Player](#players)
* [Usage](#usage-how-its-work)
* [Output](#output)


## Game
### Rules
- the player rolls a 6-sided equiprobable die that determines how many spaces on the board the player will face
- when he lands on a property that has an owner, he must pay the owner the rental value of the property
- when completing a turn on the board, the player gains 100 balance
- only players can buy property if it has no owner and the player has the money from the sale
- when buying a property or player loses the balance value and gains the right to that property
- the player with a negative balance loses the game, and no longer plays. loses its properties and therefore can be purchased by any other player
- end when a terminal player with a positive balance, at any time of the match -> winner
- If the game takes a long time, as is usual in games of this nature, the game ends on the thousandth round with the victory of the player with the most bankroll. The tiebreaker is the turn order of the players in this
match.

### Players
- opening balance: 300
- profiles:
  - The player is impulsive;
    - The impulsive gambler buys any property he lands on.
  - Player two is demanding;
    - The player requires any property as long as the rental purchase amount is 50.
  - Player three is cautious;
    - The cautious player buys any property as long as he has a reserve of 80 balance left after the purchase is made.
  - Player four is random;
    - The player randomizes the property he lands on with a 50% probability
- Property
  - cost of sale
  - rental value
  - there is property already if purchased
  - follows an order on the board

## Usage (How it's work?)

To play the game, you only need to run the following command:

```
    python3 main.py
```

Ps: no need to install any package, just run the command.

## Output:

- An execution of the proposed program must run 300 simulations, printing in the console the data referring to the executions. find the following information in the data:
- How many matches end by time out (1000 rounds);
- How many laps on average does a match take;
- What are the victories for the behavior of the players;
- Which behavior wins the most.

### Output example:

```
'The mean of duration of lap is: 11.45'
'The number of games that reached max lap is: 0'
("The profile of player reccurent is: ('wary player', [{'type of winner': "
 "'impulsive player', 'percent': 1.99}, {'type of winner': 'select player', "
 "'percent': 2.66}, {'type of winner': 'wary player', 'percent': 80.73}, "
 "{'type of winner': 'random player', 'percent': 14.62}])")
```