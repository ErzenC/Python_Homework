# 6. File Handling with Validation
# Write a script that:
# •	Reads a file 
# •	Calculates: 
# o	total number of words 
# o	number of non-empty lines 
# •	Handles: 
# o	missing file errors 
# o	empty file scenario
def analyze_file(filename):#Funksioni per analizimin e file, duke marre parasysh gabimet e mundshme
    try:#Përpjekja për të hapur dhe analizuar file
        with open(filename, "r", encoding="utf-8") as file: #"r" per lexim dhe "utf-8" per te siguruar mbeshtetje per karaktere te ndryshme
            lines = file.readlines()#Leximi i rreshtave te file dhe ruajtja ne nje liste

        if len(lines) == 0:# Kontrolli nese file eshte bosh
            print("The file is empty.")
            return

        total_words = 0
        non_empty_lines = 0

        for line in lines: #Iterimi i rreshtave te file per te numruar fjale dhe rreshta te paster
            if line.strip() != "":# Kontrolli nese rreshti eshte i paster (nuk permban vetem hapesira)
                non_empty_lines += 1
                total_words += len(line.split())

        print("Numri total i fjaleve:", total_words)
        print("Numri i rreshtave te paster:", non_empty_lines)

    except FileNotFoundError: #Trajtimi i gabimit nese file nuk gjendet
        print("Error: File not found.")

analyze_file("sample.txt") #Kthimi i rezultatit te analizimit te file "sample.txt", nese file nuk ekziston do te shfaqet mesazhi i gabimit

#OUTPUT:
# Numri total i fjaleve: 30
# Numri i rreshtave te paster: 3