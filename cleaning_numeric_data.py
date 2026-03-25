#vlerat e dhena nga detyra:

values = ["50", "75", "NaN", "100", "error", "25"]

# Write code to:
# •	Convert valid numeric values to integers 
# •	Skip invalid values 
# •	Return the cleaned list

def pastrimi(data):
    vlerat_e_pastra = []
    for v in data:
        try:
            number = int(v)#Konvertimi i vlerave qe do te ruhen ne integer
            vlerat_e_pastra.append(number)
        except ValueError:
            continue
    return vlerat_e_pastra
print("Vlerat e pastruara:", pastrimi(values))

#OUTPUT: Vlerat e pastruara: [50, 75, 100, 25]


