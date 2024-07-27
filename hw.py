import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    while len(cable_lengths) > 1:
        first_min = heapq.heappop(cable_lengths)
        second_min = heapq.heappop(cable_lengths)

        cost = first_min + second_min
        total_cost += cost
        
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

# Приклад
cable_lengths = [14, 63, 22, 16, 2, 7, 99]
print("Мінімальні витрати на з'єднання:", min_cost_to_connect_cables(cable_lengths))
