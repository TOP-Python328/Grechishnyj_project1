import data

def calc_sm_cross() -> data.Matrix:
    """Вычисляет и возвращает начальную матрицу стратегии крестика."""
    sm_cross = [[0]*data.size for _ in data.dim_range]
    half, rem = divmod(data.size, 2)
    diag = list(range(1, half+1)) + list(range(half+rem, 0, -1))
    for i in data.dim_range:
        sm_cross[i][i] = diag[i]
        sm_cross[i][-i-1] = diag[i]
    return sm_cross


def calc_sm_zero() -> data.Matrix:
    """Вычисляет и возвращает начальную матрицу стратегии нолика."""

    def triangle_desc(n: int, start: int) -> data.Matrix:
        """Генерирует и возвращает верхне-треугольную по побочной диагонали матрицу, заполняемую параллельно побочной диагонали значениями по убыванию."""
        flat = []
        indexes = range(n)
        for i in indexes:
            flat += [m if m > 0 else 0 for m in range(start-i, -start, -1)][:n]
        matrix = [flat[i*n:(i+1)*n] for i in indexes]
        if n > 2:
            for i in indexes:
                for j in indexes:
                    if i > n-j-1:
                        matrix[i][j] = 0
        return matrix

    def rot90(matrix: data.Matrix) -> data.Matrix:
        """Возвращает "повёрнутую" на 90° матрицу."""
        indexes = range(len(matrix))
        matrix = [[matrix[j][i] for j in indexes] for i in indexes]
        for i in indexes:
            matrix[i] = matrix[i][::-1]
        return matrix

    half, rem = divmod(data.size, 2)
    quarter = triangle_desc(half, half+rem)
    if data.size > 6:
        for i in range(half):
            for j in range(half):
                if i == half-j-1:
                    if i != j:
                        quarter[i][j] -= 1
                if i > half-j:
                    quarter[i][i] = half - i - (rem+1)%2
    m1 = quarter
    m2 = rot90(m1)
    m3 = rot90(m2)
    m4 = rot90(m3)
    top, bot = [], []
    for i in range(half):
        top += [m1[i] + [0]*rem + m2[i]]
        bot += [m4[i] + [0]*rem + m3[i]]
    return top + [[0]*data.size]*rem + bot



    