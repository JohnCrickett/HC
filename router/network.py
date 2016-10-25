
class NetworkError(Exception):
    """Exception raised for errors in the Network.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class Link(object):
    """Simple POD type for a Link in a Network (Graph)

    Attributes:
        src -- the a end (start) of the link
        dest -- the z end (end) of a link
        cost -- the cost of traversing the link
    """
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = int(cost)


class Network(object):
    """A representation of a network (Graph)

    """
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
        """
        Determine which nodes are reachable from this node and return a list of reachable nodes

        src -- the source node to check reachabilty from
        """
        reachable_from = []
        for link in self._links:
            if link.src == src:
                reachable_from.append(link.dest)
        return reachable_from


    def size(self):
        """ Returns the number of links in the network"""
        return len(self._links)


    def link_cost(self, src, dest):
        """
        Returns the cost of traversing the link from src to desk

        raises NetworkError if the src or dest are not found in the network
        """
        for link in self._links:
            if link.src == src and link.dest == dest:
                return link.cost
        raise NetworkError("Error: src or dest not found in network")


    def nodes(self):
        """Returns the list of nodes in the network"""
        return self._nodes


    def links(self):
        """Returns the list of links in the network"""
        return self._links



def load_network(filename):
    """
    Loads a network from a CSV formatted file

    filename -- the name of the file to load the network from

    returns a net Network object built using the file contents
    """
    with open(filename) as file:
        data = file.readlines()

    network = Network()

    for line in data:
        elements = line.split(',')
        network.add_link(elements[0].strip(), elements[1].strip(), elements[2])


    return network