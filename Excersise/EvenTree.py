# Ex - 3


def find_edges(count):
    root = max(count)

    count_even = 0

    for cnt in count:
        if cnt % 2 == 0:
            count_even += 1

    if root % 2 == 0:
        count_even -= 1

    return count_even


def count_nodes(edge_list, n, m):
    count = [1 for i in range(0, n)]

    for i in range(m - 1, -1, -1):
        count[edge_list[i][1] - 1] += count[edge_list[i][0] - 1]

    print (find_edges(count))
    return find_edges(count)


if __name__ == '__main__':
    # n,m= map(int, raw_input())
    n, m = 10, 9
    edge_list = [(2,1),(3, 1),(4,3),(5,2),(6,1),(7,2),(8,6),(9, 8),(10, 8)]
    s = count_nodes(edge_list,n,m)
    find_edges(s)

