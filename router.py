import argparse

from router.router import RouteCalculator, JourneyError
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
    parser.add_argument('--limit',
                        help='the journey cost limit',
                        )
    args = parser.parse_args()

    # the network is required so we can assume we have filename here
    # and try to load it
    network = load_network(args.network)

    # now lets see what the user wants to do with the netwoek
    # determine a journey time for a specified route
    if args.journeytime != None:
        try:
            rc = RouteCalculator(network)
            time = rc.calculate_journey_time(args.journeytime)
            print("Journey time is: %d" % time)
        except JourneyError as e:
            print(e)



    # calculate the shortest route for a specified src/dest pair
    if args.shortesttime != None:
        try:
            rc = RouteCalculator(network)
            route = rc.calculate_shortest_path(args.shortesttime[0], args.shortesttime[1])
            time = rc.calculate_journey_time(route)
            print("Journey time is: %d" % time)
            print("Route is: " + ', '.join(route))
        except JourneyError as e:
            print(e)


    # get all routes from src to dest that are within limit
    if args.limit != None:
        rc = RouteCalculator(network)
        # TODO


if __name__ == '__main__':
    main()