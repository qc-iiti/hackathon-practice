# PennyLane 101 – Know Your Devices

This project explores how the same quantum circuit can produce different outputs
depending on the PennyLane device used. The idea is to run an identical RY-rotation
circuit on two devices and compare the results.

---

## Problem Summary

- A simple circuit applies `RY` gates on all qubits.
- It is run once on `default.qubit` (returns a pure state vector) and once on
  `default.mixed` (returns a density matrix).
- The difference between these outputs is measured using the matrix one-norm.

---

## Code Explanation

### Devices
Two devices are created:
- `default.qubit` → gives a pure quantum state  
- `default.mixed` → gives a density matrix  

### Circuits
Both circuits apply the same RY rotations:



qml.RY(params[x][i], wires=i)

The pure circuit returns a state vector, while the mixed circuit returns a
density matrix.

### Comparison
The provided `matrix_norm` function computes the one-norm between:
- the density matrix ρ  
- the projector of the pure state |ψ⟩⟨ψ|

This produces a single number showing how different the two device outputs are.

---

## Output
The program prints the matrix one-norm value for the two states.

