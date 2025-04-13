from collections import deque
import math
import re


def maximalPathQuality(self, values, edges, maxTime):
    """
    :type values: List[int]
    :type edges: List[List[int]]
    :type maxTime: int
    :rtype: int
    """

    adj = [[] for _ in range(len(values))]
    for u, v, t in edges:
        adj[u].append((v, t))
        adj[v].append((u, t))
    result = [0]
    dfs(values, adj, 0, maxTime, 0, [0] * len(adj), set(), result)
    return result[0]


def dfs(values, adj, u, time, total, lookup, lookup2, result):
    lookup[u] += 1
    if lookup[u] == 1:
        total += values[u]
    if not u:
        result[0] = max(result[0], total)
    for v, t in adj[u]:
        if (u, v) in lookup2 or time < t:  # same directed edge won't be visited twice
            continue
        lookup2.add((u, v))
        dfs(values, adj, v, time - t, total, lookup, lookup2, result)
        lookup2.remove((u, v))
    lookup[u] -= 1



def part_1(file_path: str) -> int:
    valve_flow_rates, valve_connections = parse_valves(file_path)
    distances = {}
    for valve_start in ['AA'] + list(valve_flow_rates.keys()):
        for valve_end in valve_flow_rates:
            v_pair = tuple(sorted([valve_start, valve_end]))
            if valve_start != valve_end and v_pair not in distances:
                distance = calc_distance(valve_start, valve_end, valve_connections)
                distances[v_pair] = distance

    visited = []
    dfs_test('AA', valve_flow_rates, visited)

    # valve = 'AA'
    # max_total_pressure = 0
    # for v in valve_flow_rates:
    #     max_total_pressure = max(max_total_pressure, calc_max_total_pressure())
    #
    # while m_rem > 0:
    #     valves = valve_flow_rates.copy()
    #     total_pressure = 0
    #     while valves:
    #         v = valves.pop()
    #         total_pressure += m_rem * valve_flow_rates.pop(valve)
    #     max_total_pressure = max(total_pressure, max_total_pressure)

    valves = set(valve_flow_rates.keys())
    max_total_pressure = calc_max_total_pressure('AA', valves, valve_flow_rates, 30, distances)

    return max_total_pressure


def dfs_test(valve, valve_flow_rates, visited):
    for v in valve_flow_rates:
        if v in visited:
            continue
        visited.append(v)
        dfs_test(v, valve_flow_rates, visited)
        visited.remove(v)
    print(visited)






def calc_max_total_pressure(valve_start, valves, valve_flow_rates, m_rem, distances):
    if m_rem <= 0:
        return

    for valve in valves:

        calc_max_total_pressure(valve, valves - {valve})



    pressure = 0
    max_pressure = 0
    overall_max_pressure = 0
    while valves:
        valve_end = valves.pop()
        v_pair = tuple(sorted([valve_start, valve_end]))
        m_rem -= distances[v_pair] + 1
        if m_rem > 0:
            pressure += m_rem * valve_flow_rates[valve_end]
            max_pressure = calc_max_total_pressure(valve_end, valves, valve_flow_rates, m_rem, distances)
        else:
            max_pressure = max(pressure, max_pressure)
            return max_pressure

    return overall_max_pressure


def part_1_old(file_path: str) -> int:
    valve_flow_rates, valve_connections = parse_valves(file_path)

    valve = 'AA'
    next_valve, distance = find_next_valve(valve, valve_flow_rates, valve_connections, 30)
    next_m = distance
    total_pressure = 0
    print()
    print(next_valve, next_m)
    for m in range(1, 31):
        m_rem = 30 - m
        if m == next_m:
            if valve != 'AA':
                next_m += 1  # Opening the valve
            valve = next_valve
            total_pressure += m_rem * valve_flow_rates.pop(valve)

            next_valve, distance = find_next_valve(valve, valve_flow_rates, valve_connections, m_rem)
            if next_valve is None:
                break

            next_m += distance
            print(next_valve, next_m)

    return total_pressure


def part_2(file_path: str) -> int:
    pass


def parse_valves(file_path: str) -> tuple[dict[str, int], dict[str, list[str]]]:
    valve_flow_rates = {}
    valve_connections = {}
    with open(file_path, 'r') as f:
        for line in f:
            valve = line[6:8]
            flow_rate = int(re.search(r'rate=(\d+)', line).group(1))
            if flow_rate > 0:
                valve_flow_rates[valve] = flow_rate
            valves = re.findall(r'[A-Z]{2}', line.strip().split(';')[1])
            valve_connections[valve] = valves

    return valve_flow_rates, valve_connections


def find_next_valve(valve: str, valve_flow_rates: dict[str, int], valve_connections: dict[str, list[str]], m_rem: int):
    next_valve = None
    distance = 0
    max_weight = 0
    for v, flow_rate in valve_flow_rates.items():
        distance = calc_distance(valve, v, valve_connections)
        if distance < m_rem:
            weight = flow_rate / math.pow(distance, 2)
            # weight = (flow_rate * (m_rem - distance)) / math.pow(distance, 1)
            # weight = flow_rate * (m_rem - distance)
            if weight > max_weight:
                max_weight = weight
                next_valve = v

    return next_valve, distance


def calc_distance(valve_start: str, valve_end: str, valve_connections: dict[str, list[str]]) -> int:
    distance = 0
    visited = set()
    bfs = deque()
    bfs.append((valve_start, 0))
    while bfs:
        valve, distance = bfs.popleft()
        distance += 1
        if valve_end in valve_connections[valve]:
            return distance
        for v in valve_connections[valve]:
            if v not in visited:
                visited.add(v)
                bfs.append((v, distance))

    return distance
