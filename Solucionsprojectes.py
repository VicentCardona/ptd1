import math

# --- PART 1: PROJECTE DE MATEMÀTIQUES (SISTEMES D'EQUACIONS) ---

def calcular_determinant_2x2(matriu):
    """Calcula el determinant d'una matriu 2x2."""
    # ad - bc
    return matriu[0][0] * matriu[1][1] - matriu[0][1] * matriu[1][0]

def calcular_determinant_3x3(matriu):
    """Calcula el determinant d'una matriu 3x3 per la regla de Sarrus."""
    det = (matriu[0][0] * matriu[1][1] * matriu[2][2] +
           matriu[0][1] * matriu[1][2] * matriu[2][0] +
           matriu[0][2] * matriu[1][0] * matriu[2][1] -
           matriu[0][2] * matriu[1][1] * matriu[2][0] -
           matriu[0][1] * matriu[1][0] * matriu[2][2] -
           matriu[0][0] * matriu[1][2] * matriu[2][1])
    return det

def projecte_matematiques():
    """Funció principal per al projecte de resolució de sistemes d'equacions."""
    print("\n--- Projecte 1: Resolució de Sistemes d'Equacions ---")
    
    # Demanem els coeficients per a un sistema 3x3
    print("Introdueix els coeficients per a un sistema 3x3 (ax + by + cz = d):")
    
    # Matriu de coeficients (A) i vector de termes independents (B)
    A = []
    B = []
    
    for i in range(3):
        while True:
            try:
                fila_str = input(f"Introdueix els 3 coeficients (a, b, c) i el terme independent (d) de l'equació {i+1}, separats per espais: ")
                valors = [float(x) for x in fila_str.split()]
                if len(valors) != 4:
                    print("Error: Necessites introduir exactament 4 números.")
                    continue
                A.append(valors[0:3])
                B.append(valors[3])
                break
            except ValueError:
                print("Error: Si us plau, introdueix només números.")

    # Calculem el determinant principal
    det_A = calcular_determinant_3x3(A)
    
    if det_A == 0:
        print("\nEl determinant principal és 0. El sistema no té una solució única.")
        return

    # Matriu per a Dx
    Ax = [fila[:] for fila in A]
    for i in range(3):
        Ax[i][0] = B[i]
    det_Ax = calcular_determinant_3x3(Ax)

    # Matriu per a Dy
    Ay = [fila[:] for fila in A]
    for i in range(3):
        Ay[i][1] = B[i]
    det_Ay = calcular_determinant_3x3(Ay)
    
    # Matriu per a Dz
    Az = [fila[:] for fila in A]
    for i in range(3):
        Az[i][2] = B[i]
    det_Az = calcular_determinant_3x3(Az)

    # Calculem les solucions
    x = det_Ax / det_A
    y = det_Ay / det_A
    z = det_Az / det_A

    print("\n--- Solució ---")
    print(f"El valor de x és: {x:.2f}")
    print(f"El valor de y és: {y:.2f}")
    print(f"El valor de z és: {z:.2f}")


# --- PART 2: PROJECTE DE FÍSICA (LLANÇAMENT DE PROJECTILS) ---

def projecte_fisica():
    """Funció principal per al simulador de llançament de projectils."""
    print("\n--- Projecte 2: Simulador de Llançament de Projectils ---")
    
    GRAVETAT = 9.81
    
    try:
        velocitat_inicial = float(input("Introdueix la velocitat inicial (m/s): "))
        angle_graus = float(input("Introdueix l'angle de llançament (graus): "))
    except ValueError:
        print("Error: valors no vàlids.")
        return

    # Convertim l'angle a radians per als càlculs
    angle_radians = math.radians(angle_graus)

    # Descomponem la velocitat en eixos X i Y
    vx = velocitat_inicial * math.cos(angle_radians)
    vy_inicial = velocitat_inicial * math.sin(angle_radians)

    # Variables per a la simulació
    temps = 0.0
    pos_x = 0.0
    pos_y = 0.0
    interval_temps = 0.1 # Simulem cada 0.1 segons

    print("\n--- Inici de la Simulació ---")
    print("Temps (s) | Posició X (m) | Posició Y (m)")
    print("-----------------------------------------")

    while pos_y >= 0:
        print(f"{temps:9.1f} | {pos_x:13.2f} | {pos_y:13.2f}")
        
        temps += interval_temps
        
        # Càlcul de les noves posicions
        pos_x = vx * temps
        pos_y = (vy_inicial * temps) - (0.5 * GRAVETAT * temps**2)

    print("-----------------------------------------")
    print("\n--- Resultats Finals ---")
    print(f"El temps de vol ha estat de: {temps - interval_temps:.2f} segons.")
    print(f"L'abast màxim ha estat de: {pos_x:.2f} metres.")


# --- PART 3: PROJECTE D'AVENTURA DE TEXT ---

def cova(inventari):
    """Escena de la cova."""
    print("\nEstàs a l'entrada d'una cova fosca i humida.")
    print("Sents el so d'aigua gotejant a dins.")
    print("A terra veus una LLANTERNA.")
    
    while True:
        accio = input("Què vols fer? (agafar llanterna / tornar al bosc) > ").lower()
        if "agafar" in accio and "llanterna" in accio:
            print("Has agafat la llanterna. Ara pots veure millor a la foscor.")
            inventari.append("llanterna")
            # Un cop agafada, no es pot tornar a agafar
            tornar_al_bosc(inventari) 
            break
        elif "tornar" in accio:
            tornar_al_bosc(inventari)
            break
        else:
            print("No entenc aquesta acció.")

def castell(inventari):
    """Escena del castell."""
    print("\nArribes a un castell imponent amb una gran porta de fusta.")
    if "llanterna" in inventari:
        print("La porta està oberta. Gràcies a la teva llanterna, veus un passadís fosc a dins.")
        print("Decideixes entrar... i guanyes l'aventura! Felicitats!")
    else:
        print("La porta està entreoberta, però dins només veus una foscor impenetrable.")
        print("Necessitaries alguna cosa per fer llum.")
        tornar_al_bosc(inventari)

def tornar_al_bosc(inventari):
    """Funció per gestionar el retorn al bosc."""
    print("\nTornes a la clariana del bosc.")
    bosc(inventari) # Crida a la funció del bosc per continuar el joc

def bosc(inventari):
    """Escena principal del bosc."""
    print("\nEstàs en una clariana al mig d'un bosc.")
    print("Davant teu, veus dos camins:")
    print("1. Un camí que s'endinsa en una COVA.")
    print("2. Un camí que porta cap a un CASTELL llunyà.")
    
    while True:
        eleccio = input("Quin camí tries? (1 o 2) > ")
        if eleccio == "1":
            cova(inventari)
            break
        elif eleccio == "2":
            castell(inventari)
            break
        else:
            print("Tria una opció vàlida (1 o 2).")

def projecte_aventura():
    """Funció principal per a l'aventura de text."""
    print("\n--- Projecte 3: Aventura de Text ---")
    inventari = [] # L'inventari comença buit
    bosc(inventari) # Comencem el joc al bosc

# --- MENÚ PRINCIPAL PER TRIAR EL PROJECTE ---

if __name__ == "__main__":
    while True:
        print("\n===== MENÚ DE SOLUCIONS ALS PROJECTES FINALS =====")
        print("1. Projecte de Matemàtiques (Sistemes d'Equacions)")
        print("2. Projecte de Física (Llançament de Projectils)")
        print("3. Projecte d'Aventura de Text")
        print("4. Sortir")
        
        opcio = input("Tria el projecte que vols executar (1-4): ")
        
        if opcio == '1':
            projecte_matematiques()
        elif opcio == '2':
            projecte_fisica()
        elif opcio == '3':
            projecte_aventura()
        elif opcio == '4':
            print("Fins aviat!")
            break
        else:
            print("Opció no vàlida. Si us plau, tria un número de l'1 al 4.")