#coding = utf-8

def serchGraph(graph, start, end):
    results = []
    generatePath(graph, [start], end, results)
    results.sort(key=lambda x:len(x))
    return results

def generatePath(graph, path, end, results):
    state = path[-1]
    if state == end:
        results.append(path)
    else:
        for arc in graph[state]:
            if arc not in path:
                generatePath(graph, path+[arc], end, results)

if __name__ == "__main__":
    Graph = {"A":["B", "C", "D"],
             "B":["E"],
             "C":["D", "F"],
             "D":["B", "E", "G"],
             "E":[],
             "F":["D", "G"],
             "G":["E"]}
    r = serchGraph(Graph, "A", "D")
    print("**********************")
    print("  PATH   A   to    D")
    print("**********************")
    for i in r:
        print(i)