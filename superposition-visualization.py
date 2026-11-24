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

matplotlib.pyplot.show()