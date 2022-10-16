print("\n\nProgram zamienia jakkolwiek występujący ciąg znaków GvR na Guido van Rossum\n")

zdanie = input("Wpisz dowolne zdanie: ")

# funkcja replace() będzie nam zawsze zamieniać ciąg GvR na Guido van Rossum, nie ważne czy ciąg nawet będzie cześcią słowa, to i tak podmiana zostanie dokonana
podmiana_w_zdaniu = zdanie.replace("GvR", "Guido van Rossum")

print("\nZdanie po podmianie: ",podmiana_w_zdaniu)