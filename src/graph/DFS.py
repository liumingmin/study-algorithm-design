from collections import deque

class DFS(object):
	def __init__(self, graph):
		self.g = graph
		self.parent = [-1] * graph.V
		self.marked = [False] * graph.V
		self.visited = [False] * graph.V

	def dfs(self, u):
		self.marked[u] = True
		self.visitVertex(u)

		for v in self.g.adj[u]:
			if not self.marked[v]:
				self.parent[v] = u
				self.visitEdge(u, v)
				self.dfs(v)
			elif not self.visited[v] or self.g.directed:
				self.visitEdge(u, v)

		self.visited[u] = True

	def visitVertex(self, v):
		pass

	def visitEdge(self, u, v):
		pass

	def hasPathTo(self, v):
		return self.marked[v]

	def getPath(self, v):
		"""Get the path from s to v, inclusive"""
		if not self.marked[v]:
			return None

		path = []
		while v != -1:
			path.append(v)
			v = self.parent[v]

		return tuple(reversed(path))

if __name__ == '__main__':
	from Graph import Graph

	g = Graph(5)
	g.addEdge(0, 4)
	g.addEdge(0, 1)
	g.addEdge(1, 3)

	l = []
	dfs = DFS(g)
	dfs.dfs(0)
	print l
	print dfs.hasPathTo(3), dfs.hasPathTo(2)
	print dfs.getPath(3)
	print dfs.getPath(0)
	print dfs.getPath(2)
