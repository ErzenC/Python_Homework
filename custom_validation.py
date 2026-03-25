# Create a custom exception InvalidDistanceError
# Then write a function:
# •	Takes distance as input 
# •	Raises an exception if: 
# o	distance <= 0 
# o	distance exceeds 1000 
# •	Otherwise returns "Valid distance"

class InvalidDistanceError(Exception):
    pass

def validimi_distances(distance):
    if distance <=0:
        raise(InvalidDistanceError("Distanca duhet te jete pozitive."))
    elif distance > 1000:
        raise(InvalidDistanceError("Distanca nuk duhet te kaloj 1000."))
    else:
        return "Distance valide"
    
try:
    distance = int(input("Shkruaj distancen: "))
    print(validimi_distances(distance))
except InvalidDistanceError as e:
    print("Error:",e)
    