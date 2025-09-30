export const degreesOfSeparation = (familyTree, personA, personB) => {
  const graph = {};

  // Build graph
  for (let parent in familyTree) {
    const children = familyTree[parent];
    if (!graph[parent]) graph[parent] = [];

    // Connect parent to children
    for (let child of children) {
      if (!graph[child]) graph[child] = [];
      graph[parent].push(child);
      graph[child].push(parent);
    }

    // Connect siblings to each other
    for (let i = 0; i < children.length; i++) {
      for (let j = i + 1; j < children.length; j++) {
        graph[children[i]].push(children[j]);
        graph[children[j]].push(children[i]);
      }
    }
  }

  // BFS initialization
  let queue = [{ name: personA, distance: 0 }];
  let visited = new Set();
  visited.add(personA);

  while (queue.length > 0) {
    let current = queue.shift();
    let { name, distance } = current;

    if (name === personB) return distance;

    for (let neighbor of graph[name]) {
      if (!visited.has(neighbor)) {
        queue.push({ name: neighbor, distance: distance + 1 });
        visited.add(neighbor);
      }
    }
  }

  return -1; // No connection
};