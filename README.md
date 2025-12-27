# Quantum Chemistry: Universality of Givens Rotations (QHack 2022)

## Overview
This repository contains a solution to the **Quantum Chemistry – Universality of Givens Rotations** coding challenge from **QHack 2022**.

Givens rotations are particle-conserving unitaries widely used in quantum chemistry. In this challenge, the goal is to compute the rotation angles required to prepare a specific six-qubit quantum state using a sequence of Givens rotations, starting from a given ground state.

---

## Problem Statement
Given a six-qubit quantum state of the form:

|ψ⟩ = a|110000⟩ + b|001100⟩ + c|000011⟩ + d|100100⟩

starting from the ground state |110000⟩, determine the three Givens rotation angles  
**θ₁, θ₂, θ₃** required to prepare |ψ⟩ using the circuit described in the challenge.

### Constraints
- The coefficients `a, b, c, d` are **real and normalized**
- `a > 0`
- The angles θ₁, θ₂, θ₃ must lie in the interval **[−π, π)**
- Angles must be returned **in the order they appear in the circuit**

---

## Approach
The solution analytically computes the required angles using trigonometric relationships derived from the amplitudes of the target state:

- θ₂ = −2 · arctan(c / b)
- θ₃ = −2 · arctan(d / a)
- θ₁ = 2 · arcsin(c / sin(θ₂ / 2))

These angles uniquely parametrize the sequence of Givens rotations needed to generate the desired state.

---

## File Description
- `qchem300.py`  
  Implements the `givens_rotations` function and follows the exact input/output format required by the QHack evaluation system.

---

## Function Specification
```python
givens_rotations(a, b, c, d)
```
---
## BY:
-Anushri Maheshwari
-Faaz Mohammed
-Vibha Patel
