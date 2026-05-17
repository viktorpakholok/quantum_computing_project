from qiskit import QuantumCircuit

def make_circuit(n: int, initial_number: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    for qubit in range(n):
        if (initial_number >> qubit) & 1:
            qc.x(qubit)
    return qc
