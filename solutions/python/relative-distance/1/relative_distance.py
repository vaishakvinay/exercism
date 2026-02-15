from collections import deque


class RelativeDistance:
    def __init__(self, family_tree):
        self.family_tree = family_tree
        self.graph = {}

        for parent, children in family_tree.items():

            if parent not in self.graph:
                self.graph[parent] = []

            for child in children:

                # Parent ↔ Child
                self.graph[parent].append(child)

                if child not in self.graph:
                    self.graph[child] = []

                self.graph[child].append(parent)

            # 🔥 Add sibling connections
            for i in range(len(children)):
                for j in range(i + 1, len(children)):
                    c1 = children[i]
                    c2 = children[j]

                    self.graph[c1].append(c2)
                    self.graph[c2].append(c1)

    def degree_of_separation(self, person_a, person_b):

        # Person checks
        if person_a not in self.graph:
            raise ValueError("Person A not in family tree.")

        if person_b not in self.graph:
            raise ValueError("Person B not in family tree.")

        if person_a == person_b:
            return 0

        # BFS
        queue = deque([(person_a, 0)])
        visited = set()

        while queue:
            current, distance = queue.popleft()

            if current == person_b:
                return distance

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.graph[current]:
                queue.append((neighbor, distance + 1))

        # No connection
        raise ValueError(
            "No connection between person A and person B."
        )

