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
    def __init__(self, network):
        self._network = network


    def validate_journey(self, route):

        for i in range(len(route) - 1):
            if route[i + 1] not in self._network.reachable_from(route[i]):
                return False
        return True


    def calculate_journey_time(self, route):
        if not self.validate_journey(route):
            raise JourneyError("Error: unable to calculate cost for invalid journey")

        cost = 0
        for i in range(len(route) - 1):
            cost += self._network.link_cost(route[i], route[i + 1])

        return cost


    def calculate_shortest_path(self, src, dest):
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


    def get_all_routes(self, src, dest, cost_limit):
        return None