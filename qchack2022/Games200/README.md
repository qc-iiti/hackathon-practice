# CHSH Game – Quantum Advantage using PennyLane

## Team Members
- Shubham Sharma (Team Lead)
- Vibha Patel
- Faaz Mohammed

---

## About
This project implements the **CHSH game**, a classic example showing how quantum mechanics can outperform classical strategies.

Alice and Bob receive random bits, measure a shared quantum state, and try to satisfy a winning condition without communicating. Classically they can win at most **75%** of the time, while quantum strategies can reach about **85.36%**.

This code reproduces both results using **PennyLane**.

---

## What’s Implemented
- Preparation of a two-qubit entangled state  
  |ψ⟩ = α|00⟩ + β|11⟩
- CHSH measurement strategy using rotated measurement bases
- Computation of the average winning probability
- Optimization of measurement angles using gradient descent

---

## Key Idea (Measurement Trick)
Quantum devices measure only in the computational basis.  
To measure in a rotated basis, the qubit is rotated **before** measurement.

Measuring in a basis rotated by `θ`  
= applying `RY(-2θ)` and measuring normally.

This allows Alice and Bob to implement the optimal CHSH strategy.

---

## Optimization Details
- Optimizer: Gradient Descent  
- Step size: `0.1`  
- Steps: `100`  

This setup is stable, fast, and consistently meets the required tolerance.
