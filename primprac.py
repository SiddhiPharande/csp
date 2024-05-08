inf = 999999
N=5
G=[
    [0,19,5,0,3,1],
    [19,0,5,9,5],
    [4,0,9,7,8],
    [0,0,5,0,6],
    [1,3,4,0,0],
]

selected_node = [0,0,0,0,0]

edge_no = 0
selected_node[0] = True
print("Edge : Weight")
while(edge_no <N-1):
    minimum = inf
    a = 0
    b = 0
    for m in range(N):
        if (selected_node[m]):
            for n in range(N):
                if((not selected_node[n]) and G[m][n]):
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a),"-",str(b),"  :  ",str(G[a][b]))
    selected_node[b] = True
    edge_no += 1