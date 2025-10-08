# find articulations and bridges

def tarjan_algorithm(n: int, graphs: dict) -> tuple[list[int], list[list[int]]]:
    times = 0
    nums = [-1] * n
    lows = [-1] * n
    articulations = []
    bridges = []
    
    def dfs(u, parent):
        nonlocal times
        childrens = 0
        times += 1
        nums[u] = lows[u] = times
        for v in graphs[u]:
            if nums[v] == -1: # descedant
                childrens += 1
                dfs(v, u)
                lows[u] = min(lows[u], lows[v])
                if parent != -1 and nums[u] <= lows[v]:
                    articulations.append(u)
                if nums[u] < lows[v]:
                    bridges.append([u, v])
            elif v != parent: # ancestor
                lows[u] = min(lows[u], nums[v])
        if parent == -1 and childrens >= 2:
            articulations.append(u)

    dfs(0, -1)

    return articulations, bridges

if __name__ == "__main__":
    from collections import defaultdict
    graphs = defaultdict(list)
    # graphs[0].append(1)
    graphs[0].append(3)
    # graphs[1].append(0)
    # graphs[1].append(2)
    # graphs[2].append(1)
    graphs[2].append(3)
    graphs[3].append(0)
    graphs[3].append(2)

    print(tarjan_algorithm(4, graphs))