from Game import Game
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process arguments about an NBA game.')
    parser.add_argument('--path', type=str,
                        help='a path to json file to read the events from',
                        required=True)
    parser.add_argument('--event', type=int, default=0,
                        help="an index of the event to create the animation for")

    args = parser.parse_args()

    game = Game(path_to_json=args.path, event_index=args.event)
    game.read_json()
    game.start()

if __name__ == "__main__":
    main()
#fun
