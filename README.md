# NBA Animation

This is a script for visualization of NBA games from raw SportVU logs.

1. Clone this repo:

  ```bash
  $ git clone https://github.com/krish-bajaj123/nbaanimation
  ```

2. Choose any NBA game from ```data/2016.NBA.Raw.SportVU.Game.Logs``` directory.

3. Generate an animation for the play by running the following script:

  ```bash
  $ python3 main.py --path=0021500491.json --event=2
  ```

  ```
  required arguments:
    --path PATH    a path to json file to read the events from

  optional arguments:
    --event EVENT  an index of the event to create the animation to
                   (the indexing start with zero, if you index goes beyond out
                   the total number of events (plays), it will show you the last
                   one of the game)
    -h, --help     show the help message and exit
  ```
