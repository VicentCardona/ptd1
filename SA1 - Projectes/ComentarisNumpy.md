# Funcions per a Operacions amb Matrius (amb NumPy)

Aquest script realitza les mateixes operacions matricials que la versió de Python pur, però aprofitant la potència i simplicitat de la llibreria NumPy.

### `sumar_matrius(A, B)`
Suma dues matrius A i B utilitzant NumPy.
- **Lògica**: NumPy sobrecarrega l'operador `+` per a `arrays`, de manera que realitza una suma element a element de forma automàtica.

### `multiplicar_matrius(A, B)`
Multiplica dues matrius A i B utilitzant NumPy.
- **Lògica**: Fa servir la funció `np.dot()`, que implementa la multiplicació matricial estàndard de manera altament optimitzada.

### `transposada_matriu(A)`
Calcula la transposada d'una matriu A utilitzant NumPy.
- **Lògica**: Accedeix a l'atribut `.T` de l'array de NumPy, que retorna la vista transposada de la matriu sense càlculs manuals.

### `determinant_matriu(A)`
Calcula el determinant d'una matriu quadrada A.
- **Lògica**: Crida la funció `np.linalg.det()`, del mòdul d'àlgebra lineal (`linalg`) de NumPy. Funciona per a matrius quadrades de qualsevol dimensió.

### `inversa_matriu(A)`
Calcula la inversa d'una matriu quadrada A.
- **Lògica**: Després de validar que el determinant no sigui zero, utilitza la funció `np.linalg.inv()` per trobar la matriu inversa de forma eficient.