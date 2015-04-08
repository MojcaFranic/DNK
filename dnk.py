file = open("dnk.txt", "r")
dna_suspect = file.read()

male = "TGCAGGAACTTC"
female = "TGAAGGACCTTC"

caucasian = "AAAACCTCA"
african = "CGACTACAG"
asian = "CGCGGGCCG"

eye_blue = "TTGTGGTGGC"
eye_green = "GGGAGGTGGC"
eye_brown = "AAGTAGTGAC"

hair_black = "CCAGCAATCGC"
hair_brown = "GCCAGTGCCG"
hair_red = "TTAGCTATCGC"

face_square = "GCCACGG"
face_round = "ACCACAA"
face_oval = "AGGCCTCA"

#all suspects are male caucasians

if dna_suspect.find(hair_red) and dna_suspect.find(eye_brown) and dna_suspect.find(face_round):
    print("Ziga ate the ice-cream!")

elif dna_suspect.find(hair_black) and dna_suspect.find(eye_blue) and dna_suspect.find(face_oval):
    print("Matej ate the ice-cream!")

elif dna_suspect.find(hair_brown) and dna_suspect.find(eye_green) and dna_suspect.find(face_square):
    print("Miha ate the ice-cream!")

else:
    print("Ninjas don't eat ice-cream!")

print("One minute on your lips, forever on your hips...")

file.close()