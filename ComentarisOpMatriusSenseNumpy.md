# Funcions per a Operacions amb Matrius (Python Pur)

### `sumar_matrius(A, B)`
Suma dues matrius representades com a llistes de llistes.
- **Validació**: Comprova que les dimensions de les matrius siguin iguals.
- **Lògica**: Crea una matriu `resultat` buida i la recorre amb dos bucles `for` per sumar els elements `A[i][j]` i `B[i][j]`.

### `multiplicar_matrius(A, B)`
Multiplica dues matrius. El nombre de columnes d'A ha de ser igual al de files de B.
- **Validació**: Comprova que el nombre de columnes d'A sigui igual al nombre de files de B.
- **Lògica**: Utilitza tres bucles `for` niuats. Els bucles `i` i `j` seleccionen la cel·la del resultat, mentre que el bucle `k` calcula el producte escalar de la fila `i` d'A i la columna `j` de B.

### `transposada_matriu(A)`
Calcula la transposada d'una matriu.
- **Lògica**: Crea una matriu `resultat` amb les dimensions intercanviades. Després, assigna l'element `A[j][i]` a la posició `resultat[i][j]` per intercanviar files per columnes.

---
## Funcions Simplificades per a Matrius 2x2

**NOTA**: Calcular determinants i inverses per a matrius de qualsevol mida (NxN) és algorítmicament molt més complex. Aquestes funcions són exemples didàctics només per al cas 2x2.

### `determinant_2x2(A)`
Calcula el determinant d'una matriu 2x2.
- **Validació**: Assegura que la matriu sigui de 2x2.
- **Fórmula**: Aplica la fórmula `ad - bc`.

### `inversa_2x2(A)`
Calcula la inversa d'una matriu 2x2.
- **Validació**: Comprova que el determinant no sigui zero.
- **Fórmula**: Aplica la fórmula de la inversa per a matrius 2x2: `(1/det) * [[d, -b], [-c, a]]`.