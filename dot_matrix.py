
st1 = "AGCTAGGA"
st2 = "GACTAGGC"

print(np.zeros((5,5)))
#zeros
def k_zeros(x):
	return([0 for x in range(x)])
print(k_zeros(6))

col = [i for i in st1]
rows = [i for i in st2]
mtrx = []
for y in range(len(st2)):
	for x in range(len(st1)):
		mtrx.append([col[x], rows[y]]) #can have as tuple if paren added
print(mtrx[:8], "\n")
# print(mtrx[::8], "\n")
# print(mtrx[::9], "\n")
# print(mtrx[::-9], "\n")
mtrx2 = [mtrx[i:i + 8] for i in range(0, 64, 8)]
mtrx3 = [1 if mtrx[i][0] == mtrx[i][1] else 0 for i in range(len(mtrx))]
mtrx4 = [mtrx3[i:i+8] for i in range(0, 64, 8)]
# print([i for i in range(0, 64, 8)])
for i in range(len(mtrx2)):
	print(mtrx2[i])

for i in range(len(mtrx4)):
	print(mtrx4[i])

print(f"Length of one side(X) in Dot Matrix: {len(st1)}")
print(f"Length of the Dot Matrix: {len(mtrx)}")
