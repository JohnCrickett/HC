from collections import deque

from router.network import Network

class JourneyError(Exception):
    """Exception raised for errors in the Journey(s).

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class RouteCalculator(object):
    """Route calculation class"""

    def __init__(self, network):
        self._network = network


    def validate_journey(self, route):
        """ Validates a journey to ensure it travels along valid links (both existence and direction)

        route -- a list of the nodes along the route in order of traversal
        """
        for i in range(len(route) - 1):
            if route[i + 1] not in self._network.reachable_from(route[i]):
                return False
        return True


    def calculate_journey_time(self, route):
        """ Calculates the time it will take to travel the specified route (journey)

        route -- the list of the nodes along the route in order of traversal
        """
        if not self.validate_journey(route):
            raise JourneyError("Error: unable to calculate cost for an invalid journey")

        cost = 0
        for i in range(len(route) - 1):
            cost += self._network.link_cost(route[i], route[i + 1])

        return cost


    def calculate_shortest_path(self, src, dest):
        """Calculates the shortest path between a src/dest pair of nodes

        src -- the node to start from
        dest -- the target (destination) node
        """
        dist = 0
        current_node = src
        big = 99999999

        dist = {node: big for node in self._network.nodes()}
        previous = {node: None for node in self._network.nodes()}
        dist[src] = 0
        node_queue = self._network.nodes().copy()

        if src not in node_queue:
            raise JourneyError("Error: source node not in network")

        if dest not in node_queue:
            raise JourneyError("Error: destination node not in network")

        if src == dest:
            raise JourneyError("Error: soruce and destination are the same")

        neighbours = {node: set() for node in self._network.nodes()}

        for link in self._network.links():
            neighbours[link.src].add((link.dest, link.cost))

        while node_queue:
            u = min(node_queue, key=lambda node: dist[node])
            node_queue.remove(u)
            if dist[u] == big or u == dest:
                break

            for v, cost in neighbours[u]:
                alternate = dist[u] + cost
                if alternate < dist[v]:
                    dist[v] = alternate
                    previous[v] = u

        path, u = list(), dest

        while previous[u]:
            path.append(u)
            u = previous[u]
        path.append(u)

        return path[::-1] # reverse the path


    def all_routes_within_timelimit(self, src, dest, cost_limit):
        """Get all the routes between a src/dest pair of nodes that hop count is less than or
           equal to the hop limit

        src -- the start node
        dest -- the target (destination) node
        limit -- the maximum number of hops on the route
        """
        # TODO DFS with depth limited to limit
        return None


    def all_routes_within_hoplimit(self, src, dest, cost_limit):
        """Get all the routes between a src/dest pair of nodes that cost less than or
           equal to the limit

        src -- the start node
        dest -- the target (destination) node
        limit -- the maximum cost of the route
        """
        # TODO DFS with path limited to cost
        return None