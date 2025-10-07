# find articulations and bridges

def tarjan_algorithm(n: int, graphs: dict) -> tuple[list[int], list[list[int]]]:
    times = 0
    nums = [-1] * n
    lows = [-1] * n
    articulations = []
    bridges = []

    def dfs(u, parent):
        global times
        times += 1
        nums[times] = lows[times] = times
        for v in graphs[u]:
            if nums[v] == -1: # descedant
                dfs(v, u)
                lows[u] = min(lows[u], lows[v])
                if nums[u] <= lows[v]:
                    articulations.append(u)
                if nums[u] < lows[v]:
                    bridges.append([u, v])
            elif v != parent: # ancestor
                lows[u] = min(lows[u], nums[v])
                
    dfs(0 -1)

    return articulations, bridges


