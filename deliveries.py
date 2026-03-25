print("Homework Task 1: Deliveries")

#Delieveries list e dhene nga detyra
deliveries = [
    {"delivery_id": 1, "distance": 12, "status": "completed"},
    {"delivery_id": 2, "distance": -3, "status": "completed"},
    {"delivery_id": 3, "distance": 8, "status": "pending"},
    {"delivery_id": 4, "distance": 20, "status": "completed"}
]

#Funksioni per filtrimin e deliveries, duke shfaqur vetem ato qe kan statusin "completed" dhe distance pozitive
def validimi(data):
    valid_deliveries = []
    for d in data:
        if d["distance"] >= 0 and d["status"] == "completed":
            valid_deliveries.append(d)
    return valid_deliveries

print("Deliveries valide:", validimi(deliveries))
