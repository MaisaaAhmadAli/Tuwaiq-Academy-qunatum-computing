# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:46:59 2023

@author: cooc2
"""

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

def xor_gate():
    # Create a quantum circuit with two qubits and one classical bit
    qc = QuantumCircuit(2, 1)

    print("XOR gate")

    # Loop over all possible input combinations
    for input_state in range(4):
        # Set the input state
        qc.x(0) if input_state >= 2 else None
        qc.x(1) if input_state % 2 == 1 else None

        # Apply the XOR gate
        qc.cx(0, 1)  # Controlled-X gate (CNOT)
        qc.measure(1, 0)  # Measure the second qubit and store the result in the classical bit

        # Simulate the circuit
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(qc, simulator, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)

        # Print the measurement outcome
        print(f"Input {input_state:02b}: {counts}")

        # Reset the circuit
        qc.reset([0, 1])

def or_gate():
    qc = QuantumCircuit(3, 1)
    print ("OR gate")

    # Loop over all possible input combinations
    for input_state in range(4):
        # Set the input state
        qc.x(0) if input_state >= 2 else None
        qc.x(1) if input_state % 2 == 1 else None
        

        qc.cx(1,2)
        qc.x(1)
        qc.ccx(0,1,2)
        qc.measure(2, 0)  

        # Simulate the circuit
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(qc, simulator)
        result = job.result()
        counts = result.get_counts(qc)

        # Print the measurement outcome
        print(f"Input {input_state:02b}: {counts}")

        # Reset the circuit
        qc.reset(qc.qubits)

def and_gate():
    qc = QuantumCircuit(3, 1)
    print ("AND gate")

    # Loop over all possible input combinations
    for input_state in range(4):
        # Set the input state
        qc.x(0) if input_state >= 2 else None
        qc.x(1) if input_state % 2 == 1 else None

        # Apply the AND gate
        qc.ccx(0, 1, 2)  # Controlled-Controlled-X gate (Toffoli)
        qc.measure(2, 0)  # Measure the third qubit and store the result in the classical bit

        # Simulate the circuit
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(qc, simulator, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)

        # Print the measurement outcome
        print(f"Input {input_state:02b}: {counts}")

        # Reset the circuit
        qc.reset(qc.qubits)
        
def xand_gate():
    qc = QuantumCircuit(3, 1)
    print ("NAND gate")

    # Loop over all possible input combinations
    for input_state in range(4):
        # Set the input state
        qc.x(0) if input_state >= 2 else None
        qc.x(1) if input_state % 2 == 1 else None

        # Apply the AND gate
        qc.ccx(0, 1, 2)  # Controlled-Controlled-X gate (Toffoli)
        qc.x(2)
        qc.measure(2, 0)  # Measure the third qubit and store the result in the classical bit

        # Simulate the circuit
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(qc, simulator, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)

        # Print the measurement outcome
        print(f"Input {input_state:02b}: {counts}")

        # Reset the circuit
        qc.reset(qc.qubits)
xand_gate()
and_gate()       
or_gate()
xor_gate()