"""
AI453 Probabilistic Graphical Models -- Practical #2: Conditional Independence
SVNIT Surat, Department of Artificial Intelligence

Plain Python 3. No dependencies are required.
"""


# Table 1: P(A, B, C)
P1 = {
	(0, 0, 0): 0.36,
	(0, 0, 1): 0.04,
	(0, 1, 0): 0.01,
	(0, 1, 1): 0.09,
	(1, 0, 0): 0.09,
	(1, 0, 1): 0.01,
	(1, 1, 0): 0.04,
	(1, 1, 1): 0.36,
}

# Table 2: P(R, S, W)
P2 = {
	(0, 0, 0): 0.27,
	(0, 0, 1): 0.03,
	(0, 1, 0): 0.12,
	(0, 1, 1): 0.18,
	(1, 0, 0): 0.08,
	(1, 0, 1): 0.12,
	(1, 1, 0): 0.02,
	(1, 1, 1): 0.18,
}


def prob(table, conditions):
	"""Return the probability of the supplied variable assignments."""
	return sum(
		probability
		for assignment, probability in table.items()
		if all(assignment[position] == value for position, value in conditions.items())
	)


def cond(table, query, given):
	"""Return P(query | given)."""
	return prob(table, {**query, **given}) / prob(table, given)


# Worked example from the handout.
print("P(A=1) =", prob(P1, {0: 1}))


# Table 1
print("T1: P1 total =", sum(P1.values()))
print("T1: P2 total =", sum(P2.values()))

p_a1_c1 = prob(P1, {0: 1, 2: 1})
p_a1 = prob(P1, {0: 1})
p_c1 = prob(P1, {2: 1})
print("T2: P(A=1, C=1) =", p_a1_c1)
print("T2: P(A=1) P(C=1) =", p_a1 * p_c1)
print("T2: Equal?", abs(p_a1_c1 - p_a1 * p_c1) < 1e-9)

p_c1_given_a1 = cond(P1, {2: 1}, {0: 1})
p_c1_given_a0 = cond(P1, {2: 1}, {0: 0})
print("T3: P(C=1 | A=1) =", p_c1_given_a1)
print("T3: P(C=1 | A=0) =", p_c1_given_a0)
print("T3: Difference =", abs(p_c1_given_a1 - p_c1_given_a0))

print("T4: P(C=1 | B=1) =", cond(P1, {2: 1}, {1: 1}))
print("T4: P(C=1 | B=1, A=1) =", cond(P1, {2: 1}, {1: 1, 0: 1}))
print("T4: P(C=1 | B=1, A=0) =", cond(P1, {2: 1}, {1: 1, 0: 0}))

print("T5: P(C=1 | B=0) =", cond(P1, {2: 1}, {1: 0}))
print("T5: P(C=1 | B=0, A=1) =", cond(P1, {2: 1}, {1: 0, 0: 1}))
print("T5: P(C=1 | B=0, A=0) =", cond(P1, {2: 1}, {1: 0, 0: 0}))

# A and C are dependent, but given B, they are conditionally independent.


# Table 2
p_r1_s1 = prob(P2, {0: 1, 1: 1})
p_r1 = prob(P2, {0: 1})
p_s1 = prob(P2, {1: 1})
print("T6: P(R=1, S=1) =", p_r1_s1)
print("T6: P(R=1) P(S=1) =", p_r1 * p_s1)
print("T6: Equal?", abs(p_r1_s1 - p_r1 * p_s1) < 1e-9)

print("T7: P(R=1) =", p_r1)
print("T7: P(R=1 | W=1) =", cond(P2, {0: 1}, {2: 1}))
print("T7: P(R=1 | W=1, S=1) =", cond(P2, {0: 1}, {2: 1, 1: 1}))
print("T7: P(R=1 | W=1, S=0) =", cond(P2, {0: 1}, {2: 1, 1: 0}))

# T5 conditioning on B removes the dependence between A and C.
# T7 conditions on their common effect W, creating dependence between R and S.
# Given wet grass, learning that the sprinkler was on makes rain less likely.
