import numpy as np
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

qc = QuantumCircuit(3)
qc.x(0)
qc.x(1)
qc.x(2)

def my_qft(circuit: QuantumCircuit):

    qubits_num = circuit.num_qubits
    for qubit_target in range(qubits_num):
        circuit.h(qubit_target)

        for qubit_control in range(qubit_target+1, qubits_num):
            circuit.cp(2*np.pi*(np.power(2, qubit_target))*np.power(2, qubits_num-1-qubit_control) / np.power(2, qubits_num), qubit_control, qubit_target)

    for inverse in range(qubits_num//2):
        circuit.swap(inverse, qubits_num-1-inverse)

my_qft(qc)

# qc_measured = qc.measure_all(inplace=False)
# from qiskit.primitives import StatevectorSampler
# sampler = StatevectorSampler()
# job = sampler.run([qc_measured], shots=10000)
# result = job.result()
# print(f" > Counts: {result[0].data['meas'].get_counts()}")

from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
state = Statevector(qc)
print(state)
fig = plot_bloch_multivector(state)
plt.show()
