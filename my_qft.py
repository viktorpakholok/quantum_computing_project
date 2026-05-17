import numpy as np
from qiskit import QuantumCircuit


def qft(circuit: QuantumCircuit):

    qubits_num = circuit.num_qubits
    for qubit_target in range(qubits_num):
        circuit.h(qubit_target)

        for qubit_control in range(qubit_target+1, qubits_num):
            k = qubit_control - qubit_target
            circuit.cp(2 * np.pi /(2 ** k), qubit_control, qubit_target)

    for inverse in range(qubits_num//2):
        circuit.swap(inverse, qubits_num-1-inverse)


def aqft(circuit: QuantumCircuit, precision: int):

    qubits_num = circuit.num_qubits
    for qubit_target in range(qubits_num):
        circuit.h(qubit_target)

        for qubit_control in range(qubit_target+1, min(qubits_num, qubit_target+precision+1)):
            k = qubit_control - qubit_target
            circuit.cp(2 * np.pi / (2 ** k), qubit_control, qubit_target)

    for inverse in range(qubits_num//2):
        circuit.swap(inverse, qubits_num-1-inverse)

# qc_measured = qc.measure_all(inplace=False)
# from qiskit.primitives import StatevectorSampler
# sampler = StatevectorSampler()
# job = sampler.run([qc_measured], shots=10000)
# result = job.result()
# print(f" > Counts: {result[0].data['meas'].get_counts()}")

if __name__ == "__main__":
     
    from qiskit.quantum_info import Statevector
    from qiskit.visualization import plot_bloch_multivector
    import matplotlib.pyplot as plt

    qc = QuantumCircuit(3)
    qc.x(0)
    qc.x(1)
    qc.x(2)

    qft(qc)

    state = Statevector(qc)
    print(state)
    fig = plot_bloch_multivector(state)
    plt.show()
