import matplotlib.pyplot
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

matplotlib.use("TkAgg")

qc = QuantumCircuit(1)
qc.h(0)

state = Statevector(qc)

fig = plot_bloch_multivector(
    state,
    title="Superposition on Bloch Sphere"
)

qc2 = QuantumCircuit(1)
qc2.x(0)

state2 = Statevector(qc2)

fig2 = plot_bloch_multivector(
    state2,
    title="Pauli Matrix on Bloch Sphere"
)

qc3 = QuantumCircuit(1)

state3 = Statevector(qc3)

fig3 = plot_bloch_multivector(
    state3, 
    title="Basic state"
)

matplotlib.pyplot.show()