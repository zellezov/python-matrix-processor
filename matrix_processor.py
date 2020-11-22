import math


class NuMaPro:
    def print_menu():
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("0. Exit")

    def print_transpose_menu():
        print("\n1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")

    def add_matrices():
        ax, ay = [int(x) for x in input("Enter size of first matrix:").split()]
        ma = []
        print("Enter first matrix:")
        for i in range(0, ax):
            ma.append([float(x) for x in input().split()])
        bx, by = [int(x) for x in input("Enter size of second matrix:").split()]
        mb = []
        print("Enter second matrix:")
        for i in range(0, bx):
            mb.append([float(x) for x in input().split()])
        if ax != bx or ay != by:
            print("The operation cannot be performed.")
        else:
            mc = []
            for i in range(0, ax):
                row = [x + y for x, y in zip(ma[i], mb[i])]
                mc.append(row)
                print("The result is:")
                print(" ".join([str(x) for x in row]))

    def multiply_matrix():
        ax, ay = [int(x) for x in input("Enter size of matrix:").split()]
        ma = []
        for i in range(0, ax):
            ma.append([int(x) for x in input("Enter matrix:\n").split()])
        mult = int(input("Enter constant:"))
        mc = []
        for i in range(0, ax):
            row = [x * mult for x in ma[i]]
            mc.append(row)
            print("The result is:")
            print(" ".join([str(x) for x in row]))

    def multiply_matrices():
        ax, ay = [int(x) for x in input("Enter size of first matrix:").split()]
        ma = []
        print("Enter first matrix:")
        for i in range(0, ax):
            ma.append([float(x) for x in input().split()])
        bx, by = [int(x) for x in input("Enter size of second matrix:").split()]
        mb = []
        print("Enter second matrix:")
        for i in range(0, bx):
            mb.append([float(x) for x in input().split()])
        if ay != bx:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            if ax != by:
                mm = []
                for ra in range(0, ax):
                    row = []
                    for rb in range(0, by):
                        value = 0
                        for raa in range(0, ay):
                            value += ma[ra][raa] * mb[raa][rb]
                        row.append(value)
                        mm.append(row)
                    print(" ".join([str(round(x)) for x in row]))
            else:
                mm = []
                for ra in range(0, ay):
                    row = []
                    for rb in range(0, bx):
                        value = 0
                        for raa in range(0, ax):
                            value += ma[ra][raa] * mb[raa][rb]
                        row.append(value)
                        mm.append(row)
                    print(" ".join([str(x) for x in row]))

    def transpose_matrix():
        NuMaPro.print_transpose_menu()
        choice = input("Your choice:")
        ax, ay = [int(x) for x in input("Enter matrix size:").split()]
        ma = []
        print("Enter matrix:")
        for i in range(0, ax):
            ma.append([float(x) for x in input().split()])
        print("The result is:")
        mtxt = []
        if choice == "1":
            for ra in range(0, ax):
                row = []
                for rb in range(0, ay):
                    row.append(ma[rb][ra])
                print(" ".join([str(x) for x in row]))
        elif choice == "2":
            for ra in range(0, ay):
                row = []
                for rb in range(0, ax):
                    row.insert(0, ma[rb][ra])
                mtxt.append(row)
            mtxt = mtxt[::-1]
            for row in mtxt:
                print(" ".join([str(x) for x in row]))
        elif choice == "3":
            for row in ma:
                mtxt.append(row[::-1])
            for row in mtxt:
                print(" ".join([str(x) for x in row]))
        elif choice == "4":
            for row in ma:
                mtxt.insert(0, row)
            for row in mtxt:
                print(" ".join([str(x) for x in row]))
                
    def ask_determinant():
        ax, ay = [int(x) for x in input("Enter size of matrix:").split()]
        ma = []
        print("Enter matrix:")
        for i in range(0, ax):
            ma.append([float(x) for x in input().split()])
        det = NuMaPro.calculate_determinant(ax, ay, ma)
        print(f"The result is:\n{round(det, 2)}")
        
    def remove_row_column(row, column, matrix):
        reduced_row = matrix[:row] + matrix[row+1:]
        reduced_matrix = []
        for row in reduced_row:
            reduced_matrix.append(row[:column] + row[column+1:])
        return reduced_matrix    
    
    def calculate_determinant(row, column, matrix):
        if row == 1 and column == 1:
            return matrix[0][0]
        elif row == 2 and column == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        else:
            minor_dets = []
            r = 0
            for c in range(0, column):
                reduced = NuMaPro.remove_row_column(r, c, matrix)
                minor = NuMaPro.calculate_determinant(row - 1, column - 1, reduced)
                cofac = (-1) ** (1 + (c + 1))
                minor_dets.append(matrix[0][c] * minor * cofac)
            return sum(minor_dets)
            
    def calculate_better_determinant(row, column, matrix):
        # print(f"R{row} C{column}")
        if row == 1 and column == 1:
            return matrix[0][0]
        elif row == 2 and column == 2:
            # print("IMHERE")
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        else:
            minor_dets = []
            r = 0
            for c in range(0, column):
                reduced = NuMaPro.remove_row_column(r, c, matrix)
                minor = NuMaPro.calculate_better_determinant(row - 1, column - 1, reduced)
                cofac = (-1) ** (1 + (c + 1))
                minor_dets.append(minor * cofac)
            return sum(minor_dets)
    
    def calculate_cofaces(ax, ay, matrix):
        cofaces = []
        for row in range(0, ax):
            r = []
            for column in range(0, ay):
                reduced = NuMaPro.remove_row_column(row, column, matrix)
                # print(f"REDUCED BY {matrix[row][column]} RESULT {reduced}")
                minor = NuMaPro.calculate_determinant(ax - 1, ay - 1, reduced)
                # minor = (reduced[0][0] * reduced[1][1]) - (reduced[0][1] * reduced[1][0])
                # print(f"SMALL DETERMINANT {minor}")
                cofac = (-1) ** ((row + 1) + (column + 1))
                # print(f"-1 ^ ROW {row + 1} + COLUMN {column + 1} = {cofac}")
                # print(cofac)
                # r.append(matrix[row][column] * minor * cofac)
                r.append(minor * cofac)
                # print(f"COFF {matrix[row][column] * minor * cofac}")
            cofaces.append(r)
        # print(f"FRESHCOF {cofaces}")
        return cofaces
        
    def inverse_matrix():
        ax, ay = [int(x) for x in input("Enter size of matrix:").split()]
        ma = []
        print("Enter matrix:")
        for i in range(0, ax):
            ma.append([float(x) for x in input().split()])
        determinant = NuMaPro.calculate_determinant(ax, ay, ma)
        # print(f"DETERM {determinant}")
        if determinant == 0:
            print("This matrix doesn't have an inverse.")
        else:
            cofaces = NuMaPro.calculate_cofaces(ax, ay, ma)
            # print(f"COFACES {cofaces}")
            transcofaces = []
            for ra in range(0, ax):
                row = []
                for rb in range(0, ay):
                    row.append(cofaces[rb][ra])
                transcofaces.append(row)
            # print(f"TRANSCOFACES {transcofaces}")
            mc = []
            print("The result is:")
            for i in range(0, ax):
                const = 1 / determinant
                # print(f"CONST {const}")
                row = [x * const for x in transcofaces[i]]
                mc.append(row)
                print(" ".join([f"{x:.4f}" for x in row]))

    def run():
        running = True
        while running:
            NuMaPro.print_menu()
            choice = input("Your choice:")
            if choice == "0":
                running = False
            elif choice == "1":
                NuMaPro.add_matrices()
            elif choice == "2":
                NuMaPro.multiply_matrix()
            elif choice == "3":
                NuMaPro.multiply_matrices()
            elif choice == "4":
                NuMaPro.transpose_matrix()
            elif choice == "5":
                NuMaPro.ask_determinant()
            elif choice == "6":
                NuMaPro.inverse_matrix()


NuMaPro.run()

