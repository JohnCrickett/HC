import argparse

from router.router import RouteCalculator
from router.network import Network, load_network

def main():
    parser = argparse.ArgumentParser(description='Routing.')

    parser.add_argument('--network',
                        help='the name of the network file to route over',
                        required=True
                        )
    parser.add_argument('--journeytime',
                        nargs="+",
                        help='the journey to validate / cost',
                        )

    parser.add_argument('--shortesttime',
                        nargs="+",
                        help='the journey to calculate / cost',
                        )

    args = parser.parse_args()

    network = load_network(args.network)

    if args.journeytime != None:
        rc = RouteCalculator(network)
        time = rc.calculate_journey_time(args.journeytime)
        print("Journey time is: %d" % time)

    if args.shortesttime != None:
        rc = RouteCalculator(network)
        route = rc.calculate_shortest_path(args.shortesttime[0], args.shortesttime[1])
        time = rc.calculate_journey_time(route)
        print("Journey time is: %d" % time)
        print("Route is: " + ', '.join(route))

if __name__ == '__main__':
    main()