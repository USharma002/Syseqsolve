a = [[1, 2, 1], [2, 1, 2], [2, 2, 1]]
def remove_col(arr, ith, jth = 0):
    newarr = [[j for i,j in enumerate(sub) if i != ith] for sub in arr]
    newarr.pop(jth)
    return newarr

def det(mat):
	if len(mat) == 1:
		return mat[0][0]
	elif len(mat) == 2:
		return mat[0][0] * mat[1][1] - mat[0][1]*mat[1][0]
	else:
		return sum([mat[0][i] * det(remove_col(mat, i)) * (-1)**i for i in range(len(mat))])

def transpose(matrix):
	lst = matrix
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if i<j:
				lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
	return lst

def adjoint(matrix):
	lst = [[(-1)**(j + i) * det(remove_col(matrix, i, j)) for i in range(len(matrix))] for j in range(len(matrix))]
	return transpose(lst)

def inverse(matrix):
	determinant = det(matrix)
	return [[round(i/determinant, 2) for i in j] for j in adjoint(matrix)]

def read_eq(eq):
	eq = eq.replace(' ', '')
	eq = eq.replace('=', ',')
	equations= eq.split(',')
	vdict = {}
	const_mat = []
	for i in range(0, len(equations), 2):
		equations[i] = equations[i].replace('-', '+-')
		equations[i] = equations[i].split('+')
	for i in range(0, len(equations), 2):
		for j in equations[i]:
			if j[-1] not in vdict:
				vdict[j[-1]] = 0.0
	eq_var = {}
	for i in range(0, len(equations), 2):
		ph = vdict.copy()
		for j in equations[i]:
			ph[j[-1]] += 1.0 if j[:-1] == '' else -1 if j[:-1] == '-' else float(j[:-1])
		eq_var[1 + i/2] = ph
	for i in range(1, len(equations), 2):
		const_mat += [[int(equations[i])]]
	return [list(i.values()) for i in eq_var.values()], const_mat, vdict

def mat_mul(m1, m2):
	solution = [[sum(a * b for a, b in zip(m1_row, m2_col)) for m2_col in zip(*m2)] for m1_row in m1] 
	return solution


def solve(eq, rd = 2):
	try:
		var_matrix, constants, vdict = read_eq(eq)[0], read_eq(eq)[1], read_eq(eq)[2]
		sol = mat_mul(inverse(var_matrix), constants)
		return [f'{i} = {round(*j, rd)}' for i, j in zip(vdict.keys(), sol)]
	except:
		print("SOME ERROR OCCURED")