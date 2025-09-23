import numpy as np

# --- Funcions per a Operacions amb Matrius (amb NumPy) ---

def sumar_matrius(A, B):
    """Suma dues matrius A i B utilitzant NumPy."""
    if A.shape != B.shape:
        return "Error: Les matrius han de tenir les mateixes dimensions."
    
    # Amb NumPy, la suma és tan senzilla com fer servir l'operador '+'
    return A + B

def multiplicar_matrius(A, B):
    """Multiplica dues matrius A i B utilitzant NumPy."""
    if A.shape[1] != B.shape[0]:
        return "Error: El nombre de columnes de la primera matriu ha de ser igual al de files de la segona."
    
    # Fem servir la funció np.dot() (o l'operador '@') per a la multiplicació matricial.
    return np.dot(A, B)

def transposada_matriu(A):
    """Calcula la transposada d'una matriu A utilitzant NumPy."""
    # NumPy ens dona una drecera molt còmoda: l'atribut .T
    return A.T

def determinant_matriu(A):
    """Calcula el determinant d'una matriu quadrada A."""
    if A.shape[0] != A.shape[1]:
        return "Error: La matriu ha de ser quadrada per calcular el determinant."
    
    # La funció det() del mòdul d'àlgebra lineal (linalg) de NumPy fa el càlcul.
    return np.linalg.det(A)

def inversa_matriu(A):
    """Calcula la inversa d'una matriu quadrada A."""
    # Primer, verifiquem que sigui quadrada
    if A.shape[0] != A.shape[1]:
        return "Error: La matriu ha de ser quadrada per tenir inversa."
    
    # Després, que el determinant no sigui zero
    if np.linalg.det(A) == 0:
        return "Error: La matriu no és invertible (el seu determinant és zero)."
        
    # La funció inv() de linalg calcula la matriu inversa.
    return np.linalg.inv(A)

# --- Exemple d'Ús ---

print("### CALCULADORA DE MATRIUS AMB NUMPY ###\n")

# Definim les nostres matrius com a 'arrays' de NumPy
# Aquesta és la conversió clau: de llistes de llistes a arrays de NumPy.
matriu1 = np.array([[1, 2, 3], 
                    [4, 5, 6]])

matriu2 = np.array([[7, 8], 
                    [9, 1], 
                    [2, 3]])
           
matriu_quadrada = np.array([[3, 1], 
                            [4, 2]])

print("--- Multiplicació (amb NumPy) ---")
resultat_mult = multiplicar_matrius(matriu1, matriu2)
print(f"Resultat de multiplicar matriu1 * matriu2:\n{resultat_mult}\n")

print("--- Transposada (amb NumPy) ---")
transposada = transposada_matriu(matriu_quadrada)
print(f"Transposada de matriu_quadrada:\n{transposada}\n")

print("--- Determinant i Inversa (amb NumPy) ---")
print(f"Matriu quadrada:\n{matriu_quadrada}")
det = determinant_matriu(matriu_quadrada)
inv = inversa_matriu(matriu_quadrada)
print(f"Determinant: {det:.2f}") # Formategem a 2 decimals
print(f"Inversa:\n{inv}\n")