import heapq

tickets = []
heapq.heappush(tickets, (3, "Regular"))
heapq.heappush(tickets, (1, "VIP"))

priority, person = heapq.heappop(tickets)

print("Processing", person)