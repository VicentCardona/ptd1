# --- Funcions per a Operacions amb Matrius (Python Pur) ---

def sumar_matrius(A, B):
    """Suma dues matrius representades com a llistes de llistes."""
    # Validar que les dimensions siguin iguals
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Error: Les matrius han de tenir les mateixes dimensions."

    # Creem una matriu resultat plena de zeros
    resultat = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    # Recorrem cada element per sumar-los
    for i in range(len(A)):
        for j in range(len(A[0])):
            resultat[i][j] = A[i][j] + B[i][j]
            
    return resultat

def multiplicar_matrius(A, B):
    """Multiplica dues matrius. El nombre de columnes d'A ha de ser igual al de files de B."""
    files_A = len(A)
    columnes_A = len(A[0])
    files_B = len(B)
    columnes_B = len(B[0])

    if columnes_A != files_B:
        return "Error: Dimensions incompatibles per a la multiplicació."

    # Creem la matriu resultat amb les dimensions correctes, plena de zeros
    resultat = [[0 for _ in range(columnes_B)] for _ in range(files_A)]

    # El cor de la multiplicació matricial
    for i in range(files_A):
        for j in range(columnes_B):
            for k in range(columnes_A): # o files_B
                resultat[i][j] += A[i][k] * B[k][j]
                
    return resultat

def transposada_matriu(A):
    """Calcula la transposada d'una matriu."""
    files = len(A)
    columnes = len(A[0])
    
    # La transposada tindrà les dimensions invertides
    resultat = [[0 for _ in range(files)] for _ in range(columnes)]
    
    for i in range(columnes):
        for j in range(files):
            resultat[i][j] = A[j][i]
            
    return resultat

# --- Funcions Simplificades per a 2x2 ---
# NOTA: Calcular determinants i inverses per a matrius de qualsevol mida (NxN)
# és molt més complex. Aquests són exemples només per a matrius 2x2.

def determinant_2x2(A):
    """Calcula el determinant d'una matriu 2x2."""
    if len(A) != 2 or len(A[0]) != 2:
        return "Error: Aquesta funció només accepta matrius 2x2."
    
    # Fórmula: ad - bc
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

def inversa_2x2(A):
    """Calcula la inversa d'una matriu 2x2."""
    det = determinant_2x2(A)
    
    if isinstance(det, str): # Si la funció de determinant ha retornat un error
        return det
    if det == 0:
        return "Error: La matriu no té inversa (determinant és zero)."
        
    # Fórmula de la inversa 2x2: (1/det) * [[d, -b], [-c, a]]
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    
    factor = 1 / det
    
    inversa = [
        [factor * d, factor * -b],
        [factor * -c, factor * a]
    ]
    return inversa

# --- Exemple d'Ús ---

# Definim matrius com a llistes de llistes
matriu1 = [[1, 2, 3], 
           [4, 5, 6]]

matriu2 = [[7, 8], 
           [9, 1], 
           [2, 3]]
           
matriu_quadrada = [[3, 1], 
                   [4, 2]]

print("--- Multiplicació (sense NumPy) ---")
print(f"Resultat de multiplicar matriu1 * matriu2:\n{multiplicar_matrius(matriu1, matriu2)}\n")

print("--- Transposada (sense NumPy) ---")
print(f"Transposada de matriu_quadrada:\n{transposada_matriu(matriu_quadrada)}\n")

print("--- Determinant i Inversa per a 2x2 (sense NumPy) ---")
print(f"Matriu quadrada:\n{matriu_quadrada}")
det = determinant_2x2(matriu_quadrada)
inv = inversa_2x2(matriu_quadrada)
print(f"Determinant: {det}")
print(f"Inversa:\n{inv}")