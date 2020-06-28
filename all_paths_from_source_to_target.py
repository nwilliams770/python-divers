class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        edges = self._generate_edges(graph)
        start_node = 0
        end_node = len(graph) - 1
        print("edges", edges)
        paths = self._dfs(edges, end_node, start_node, [], [])

        return paths


    def _dfs(self, edges, target, node, path, paths):
        if node == target:

            path.append(node)
            paths.append(path)
        else:
            path.append(node)
            next_in_path = edges[node]


            if len(next_in_path) > 0:
                for el in next_in_path:
                    node = el
                    self._dfs(edges, target, node, path.copy(), paths)

        return paths

    def _generate_edges(self, l):
        edges = {}
        for i, el in enumerate(l):
            edges[i] = el

        return edges