
class NetworkError(Exception):
    """Exception raised for errors in the Network.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class Link(object):
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = int(cost)


class Network(object):
    def __init__(self):
        self._links = []
        self._nodes = []


    def add_link(self, src, dest, cost):
        if src == dest:
            raise NetworkError("Error: adding a circular link")

        link = Link(src, dest, cost)
        if link in self._links:
            raise NetworkError("Error: duplicate link added")
        self._links.append(link)

        if src not in self._nodes:
            self._nodes.append(src)

        if dest not in self._nodes:
            self._nodes.append(dest)


    def reachable_from(self, src):
        reachable_from = []
        for link in self._links:
            if link.src == src:
                reachable_from.append(link.dest)
        return reachable_from


    def size(self):
        return len(self._links)


    def link_cost(self, src, dest):
        for link in self._links:
            if link.src == src and link.dest == dest:
                return link.cost


    def nodes(self):
        return self._nodes


    def links(self):
        return self._links



def load_network(filename):
    with open(filename) as file:
        data = file.readlines()

    network = Network()

    for line in data:
        elements = line.split(',')
        network.add_link(elements[0].strip(), elements[1].strip(), elements[2])


    return network