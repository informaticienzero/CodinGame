import copy
import gc
import time

from sys import stderr
from typing import Dict, List, Set, Tuple

gc.disable()
start = time.time()

class Deck:
    """
    A deck is a set of wagons and cards to use them.
    """
    def __init__(self, wagons: int, cards: str) -> None:
        """
        Creates a new deck.

        Required arguments:
        wagons (int) -- The amount of wagons availables.
        cards (str) -- A string of numbers, giving the count of each card.
        """

        self.wagons: int = wagons
        """Number of pawn we have."""
        self.cards: Dict[str, int] = dict(zip(['red', 'yellow', 'green', 'blue', 'white', 'black', 'orange', 'pink', 'engine'], [int(x) for x in cards.split()]))
        """Dictionary keeping the number of cards of each color we have."""


    def __str__(self) -> str:
        """
        A Deck object in printable format.
        """
        return (f'[Deck] Wagons: {self.wagons}\n'
                f'[Deck] Cards: {self.cards}')


    def __repr__(self) -> str:
        """
        Unambiguous representation of a Deck, for debug.
        """
        return f'{self.wagons}, {self.cards}'


    def update(self, route, all_routes, completed_routes, reserved_engines: int) -> int:
        """
        Updates the current deck for a given Route.
        """

        points: int = 0
        if route.is_completable(self):
            if route not in completed_routes:
                required_cards: int = route.length - route.required_engines
                required_color: str = route.color

                if route.color == 'gray':
                    # If gray, then the color with the most cards that is the less used.
                    matching_colors = [color for color in self.cards if self.cards[color] == max(self.cards.values())]
                    min: int = 100
                    for color in matching_colors:
                        occurences = sum(route.length for route in all_routes if route.color == color)
                        if occurences < min:
                            required_color = color
                            min = occurences

                # Maybe we'll need engines to complete the route because there were not enough color cards.
                additional_engines: int = route.length - self.cards[required_color] - route.required_engines
                if additional_engines < 0:
                    additional_engines = 0

                # If we have have as much engines as we have to use everywhere.
                if reserved_engines == self.cards['engine']:
                    additional_engines = 0

                #print(f'[update] Color: {required_color}', file = stderr)
                #print(f'[update] Route: {repr(route)}', file = stderr)
                #print(f'[update] Engines required: {route.required_engines}.', file = stderr)
                #print(f'[update] Additional engines: {additional_engines}.', file = stderr)

                self.cards[required_color] -= required_cards - additional_engines
                if self.cards[required_color] < 0:
                    self.cards[required_color] += required_cards - additional_engines
                    return 0

                self.cards['engine'] -= route.required_engines + additional_engines
                self.wagons -= route.length
                completed_routes.append(route)

                points += route.points

        #print('', file = stderr)
        return points


    def update_for_path(self, path, all_routes, completed_routes, reserved_engines: int) -> int:
        """
        Updates deck for a given Path.
        """

        total: int = 0
        if path.is_completable(self):
            for route in path.routes:
                total += self.update(route, all_routes, completed_routes, reserved_engines)
        return total


class Route:
    """
    A route is a link of a certain color between two cities.
    """
    def __init__(self, route: str) -> None:

        informations: List[str] = route.split()

        self.length: int = int(informations[0])
        """Length of the route, in cases."""
        self.required_engines: int = int(informations[1])
        """Number of engines required to complete the route. 0 if no engine necessary."""
        self.color: str = informations[2].lower()
        """Lowercase color of the route."""
        self.cities: Tuple[str, str] = (informations[3], informations[4])
        """Tuple containing the two cities linked by the route."""
        self.points: int = {
            1: 1,
            2: 2,
            3: 4,
            4: 7,
            6: 15,
            8: 21
        }[self.length]
        """The number of points earned when route is completed."""


    def __str__(self) -> str:
        """
        A Route object in printable format.
        """
        return (f'[Route] {self.cities[0]} - {self.cities[1]} is {self.length} cases long.\n'
                f'[Route] Route requires {self.color} cards with {self.required_engines} engines.\n'
                f'[Route] Route will bring {self.points} points.')


    def __repr__(self) -> str:
        """
        Unambiguous representation of a Route, for debug.
        """
        return  f'{self.length} {self.required_engines} {self.color} {self.cities[0]} {self.cities[1]} {self.points}pts'


    def __eq__(self, other) -> bool:
        """
        Test if two routes are the same based on their cities.
        """
        return sorted(self.cities) == sorted(other.cities)


    def is_completable(self, deck: Deck) -> bool:
        """
        Checks if a route is completable, based on a deck.
        """
        if deck.wagons < self.length:
            # If we don't have enough wagons left, for sure we can't complete this route.
            #print(f'[Route.is_completable] Route not completable because not enough wagons (only {deck.wagons}, needs {self.length}).', file = stderr)
            return False

        if self.required_engines != 0 and deck.cards['engine'] < self.required_engines:
            # If we don't have the required amount of engines, we can't complete this route.
            #print(f'[Route.is_completable] Route not completable because not enough engines.', file = stderr)
            return False

        required_color: str = self.color
        if self.color == 'gray':
            # If gray, then the color with the most cards.
            required_color = next(color for color in deck.cards if deck.cards[color] == max(deck.cards.values()))

        return deck.cards[required_color] >= self.length or deck.cards[required_color] + deck.cards['engine'] >= self.length


class Path:
    """
    A Path is a list of Route to link two cities, with a cost.
    """
    def __init__(self, origin: str, destination: str, cost: int, routes: List[Route], completed_routes: List[Route]) -> None:
        """
        Creates a new Path, link between city origin and city destination, with a cost and a list of Route.
        """
        self.origin: str = origin
        """City where to start from."""
        self.destination: str = destination
        """City where to go to."""
        self.wagons_cost: int = cost
        """Wagons needed to complete this path."""        
        self.routes: List[Route] = Path.eliminate_duplicates(routes)
        """All routes taken by this path."""
        self.completed_routes: List[Route] = completed_routes
        """Completed routes in the Path"""
        self.cities: Set[str] = set([city for cities in [route.cities for route in self.routes] for city in cities])
        """Set of all cities of the Path."""


    @staticmethod
    def eliminate_duplicates(routes: List[Route]) -> List[Route]:
        """
        Removes all duplicates from a list of Route.
        """
        cities_linked: Set[str] = set()
        without_duplicates: List[Route] = []

        for route in routes:
            origin, destination = route.cities
            if origin in cities_linked and destination in cities_linked:
                # Route already present.
                already_present: Route = next(route for route in without_duplicates if origin in route.cities and destination in route.cities)
                if route.length < already_present.length:
                    without_duplicates.remove(already_present)
                    without_duplicates.append(route)
            else:
                without_duplicates.append(route)
                cities_linked.update([origin, destination])

        return without_duplicates


    def is_completable(self, deck: Deck) -> bool:
        """
        Checks if a Path can be completed, based on a deck.
        """
        if deck.wagons < self.wagons_cost or deck.wagons + deck.cards['engine'] < self.wagons_cost:
            #print(f'\t[Path.is_completable] Cannot complete {self} because not enough wagons ({deck.wagons}, needs {self.wagons_cost}).', file = stderr)
            return False

        engines_left: int = deck.cards['engine']
        for color, amount in deck.cards.items():
            if color != 'engine':
                required_cards: int = sum(route.length for route in self.routes if route.color == color and route not in self.completed_routes)
                if required_cards > amount:
                    # If we need more cards than we have.
                    if required_cards <= amount + deck.cards['engine']:
                        deck.cards['engine'] -= required_cards - amount
                    else:
                        # Even with engines, we don't have enough cards to complete all roads.
                        deck.cards['engine'] = engines_left
                        return False

        deck.cards['engine'] = engines_left
        return True


    def score(self, deck: Deck) -> int:
        """
        Gets the score for a Path with a deck associated.
        """
        if not self.is_completable(deck):
            return 0
        return sum(route.points for route in self.routes)


    def __str__(self):
        """
        A Path object in printable format.
        """
        return f'[Path] {self.origin} - {self.destination}'


class Bfs:
    @staticmethod
    def paths(origin: str, destination: str, routes: List[Route], neighbours: Dict[str, Dict[str, int]], completed_routes: List[Route]) -> List[Path]:
        """
        Get all the paths between an origin to a destination. Returns a list of Path.
        If the city of origin or the city of destination is not in the map, returns an empty list.
        """
        if origin not in neighbours or destination not in neighbours:
            return []

        # BFS algorithm.
        paths: List[List[str]] = []
        queue: List[Tuple[str, List[str]]] = [(origin, [origin])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next_city in set(neighbours[vertex]) - set(path):
                if next_city == destination:
                    paths.append(path + [next_city])
                else:
                    queue.append((next_city, path + [next_city]))

        all_routes: List[Path] = []
        for path in paths:
            routes_in_path: List[Route] = []

            for first, second in zip(path, path[1:]):
                # Convert our list of cities into list of routes.
                routes_in_path.extend(filter(lambda x: first in x.cities and second in x.cities, routes))

            # Now we have to filter to keep only one route as link for two cities.
            routes_in_path = Path.eliminate_duplicates(routes_in_path)

            # Calculates the cost by summing the length of each route, unless it is already completed.
            path_cost: int = sum(route.length for route in routes_in_path if route not in completed_routes)
            all_routes.append(Path(origin, destination, path_cost, routes_in_path, completed_routes))

        return sorted(all_routes, key = lambda path: path.wagons_cost)


class GameSimulation:
    """
    Can launch simulations of game.
    """
    def __init__(self, deck: Deck, routes: List[str], tickets: List[str], neighbours: Dict[str, Dict[str, int]], tickets_cities: Set[str], path: Path) -> None:
        self.deck: Deck = copy.deepcopy(deck)
        """The deck used for the simulation."""
        self.routes: List[Route] = routes
        """Routes of the simulation."""
        self.completed_routes: List[Route] = []
        """Routes already done."""
        self.tickets: List[str] = list(tickets)
        """Tickets of the simulation, sorted from greatest to lowest value."""
        self.completed_tickets: List[Path] = []
        """Tickets already completed."""
        self.neighbours: Dict[str, Dict[str, int]] = neighbours
        """For each city, give all it's neighbours."""
        self.tickets_cities: Set[str] = set(tickets_cities)
        """A set of all cities present in the tickets."""
        self.reserved_engines: int = sum(route.required_engines for route in self.routes)
        """Based on all routes, gets the number of engines that will be used."""
        self.path: Path = path


    def simulate_for_path(self, path: Path) -> int:
        """
        Simulate a single path.
        """
        routes: List[Route] = copy.deepcopy(self.routes)
        completed_routes: List[Route] = copy.deepcopy(self.completed_routes)
        deck: Deck = copy.deepcopy(self.deck)

        return deck.update_for_path(path, routes, completed_routes, self.reserved_engines)


    def simulate_game(self, origin: str, destination: str) -> int:
        """
        Simulate the total of points to make for a Path.
        """
        points: int = 0
        points = self.deck.update_for_path(self.path, self.routes, self.completed_routes, self.reserved_engines)
        #print(f'[simulate_game] We got {points} pts for {self.path}.', file = stderr)

        if points != 0:
            tickets: List[str] = (ticket for ticket in self.tickets if ticket not in self.completed_tickets)

            # Now, let's look for all tickets.
            for ticket in tickets:
                infos: List[str] = ticket.split()
                ticket_value: int = int(infos[0])
                ticket_origin: str = infos[1]
                ticket_destination: str = infos[2]

                ticket_paths: List[Path] = Bfs.paths(ticket_origin, ticket_destination, self.routes, self.neighbours, self.completed_routes)
                if ticket_paths:
                    min_path: Path = next((path for path in ticket_paths if path.wagons_cost == 0), None)

                    if min_path:
                        # If we get one that need 0 wagon, it means it was completed when doing previous ticket.
                        points += ticket_value
                        #print(f'[simulate_game](Ticket) Earned {ticket_value} points for completing ticket {min_path}.', file = stderr)
                        self.completed_tickets.append(min_path)

                    else:

                        min_length: int = min(path.wagons_cost for path in ticket_paths)
                        minimal_paths: List[Path] = [path for path in ticket_paths if path.wagons_cost == min_length]
                        max_matched_cities: int = -1

                        for path in minimal_paths:
                            # We have to look, for all those minimal possible paths, which is the best.
                            score: int = self.simulate_for_path(path)
                            matched_cities: int = sum(1 for city in path.cities if city in self.tickets_cities)
                            if matched_cities > max_matched_cities:
                                max_matched_cities = matched_cities
                                min_path = path

                        ticket_points: int = self.deck.update_for_path(min_path, self.routes, self.completed_routes, self.reserved_engines)
                        if ticket_points == 0:
                            # Cannot complete this ticket.
                            #print(f'[simulate_game] {ticket_origin} - {ticket_destination} KO, lost {ticket_value} pts.', file = stderr)
                            points -= ticket_value
                        else:
                            # We add the points earned for all routes + points earned for completing a ticket.
                            #print(f'[simulate_game](Routes + Ticket) {ticket_origin} - {ticket_destination} completed, earned {ticket_points + ticket_value} pts.', file = stderr)
                            points += ticket_points

                            completed: bool = True
                            for route in min_path.routes:
                                if route not in self.completed_routes:
                                    completed = False

                            if completed:
                                points += ticket_value
                                self.completed_tickets.append(min_path)
                else:
                    # Not a single ticket.
                    return -ticket_value

        #print(f'[simulate_game] Total for this simulation: {points} pts.', file = stderr)
        #print(f'[simulate_game] Completed routes: {self.completed_routes}', file = stderr)
        #print('', file = stderr)
        return points


class Game:
    """
    The main class responsible of launching the game.
    """
    def __init__(self, deck: Deck, routes: List[str], tickets: List[str]) -> None:
        """
        Creates an instance of Game.

        Required arguments:
        deck (Deck) -- A deck of cards.
        routes (List[str]) -- All the routes when the game starts. A route likes 'X Y Color City1 City2'.
            X (int) is the length of the route.
            Y (int) is the number of engines required to complete the route.
            Color (str) is the color of the cards to use to complete the route.
        tickets (List[str]) -- All the tickets when the game starts. A ticket likes 'X City1 City2'.
            X (int) is the points earned when the ticket is complete.
        """
        self.deck: Deck = deck
        """The deck for this game."""

        self.routes: List[Route] = list(reversed(sorted([Route(route) for route in routes], key = lambda r: r.length)))
        """All routes when game starts."""
        self.completed_routes: List[Route] = []
        """Routes already done."""

        self.all_connections: Dict[str, Dict[str, int]] = {}
        """For each city, give all it's neighbours."""

        self.tickets: List[str] = list(reversed(sorted(tickets, key = lambda t: int(t.split()[0]))))
        """All tickets when game starts."""
        self.ticket_cities: Set[str] = set([city for cities in [[x[1], x[2]] for x in (x.split() for x in self.tickets)] for city in cities])
        """A set of all cities present in the tickets."""
        self.tickets_done: List[str] = []
        """List of all completed tickets."""

        self.reserved_engines: int = sum(route.required_engines for route in self.routes)
        """Based on all routes, gets the number of engines that will be used."""

        for route in self.routes:
            (start, end) = route.cities

            if start not in self.all_connections:
                self.all_connections[start] = { end: route.length }
            else:
                self.all_connections[start].update({ end: route.length })

            if end not in self.all_connections:
                self.all_connections[end] = { start: route.length }
            else:
                self.all_connections[end].update({ start: route.length })


    def play_game(self, ticket_number: int) -> int:
        """
        Plays the complete party of Ticket to Ride.
        """
        score: int = 0

        if self.tickets:
            ticket: str = self.tickets[ticket_number]
            infos: List[str] = ticket.split()
            value: int = int(infos[0])
            origin: str = infos[1]
            destination: str = infos[2]

            #print(f'[play_game] Ticket: {ticket}.', file = stderr)

            paths: List[Path] = Bfs.paths(origin, destination, self.routes, self.all_connections, self.completed_routes)
            scores: List[int] = []

            for path in paths:
                simulation = GameSimulation(self.deck, self.routes, self.tickets, self.all_connections, self.ticket_cities, path)
                scores.append(simulation.simulate_game(origin, destination))

            if paths:
                score = max(scores)
            else:
                score = -value
                # If we still have wagons left, let's try to do more routes to gain more points.
                if self.deck.wagons > 0:
                    for route in self.routes:
                        score += self.deck.update(route, self.routes, self.completed_routes, self.reserved_engines)
        else:
            score = sum(self.deck.update(route, self.routes, self.completed_routes, self.reserved_engines) for route in self.routes)

        #print(f'\n', file = stderr)
        return score
        

wagons, num_tickets, num_routes = [int(i) for i in input().split()]
# Our deck of cards.
deck = Deck(wagons, input())
# List of all the routes.
routes: List[Route] = []
# List of all tickets.
tickets: List[str] = []

for i in range(num_tickets):
    tickets.append(input())
for i in range(num_routes):
    routes.append(input())
    
if tickets:
    tickets = list(reversed(sorted(tickets, key = lambda t: int(t.split()[0]))))
    
game: Game = Game(deck, routes, tickets)

totals: List[int] = []
if tickets:
    for i in range(len(tickets)):
        totals.append(game.play_game(i))
    print(f'{max(totals)}')
else:
    total: int = game.play_game(0)
    print(f'{total}')
    
end = time.time()
print(f'Program executed in {(end - start):03.03f} seconds.', file = stderr)
