#taking a predefined tree
        graph={0:[1,2],1:[0,3,4],2:[0,5,6],3:[1,7],4:[1,7],5:[2,7],6:[2,7],7:[3,4,5,6]}
        visited=[0,0,0,0,0,0,0,0]
        def dfs(a):
            visited[a]=1
                print(a)
                    for i in graph[a]:
                            if visited[i]==0:
                                        dfs(i)
                                        dfs(0)

