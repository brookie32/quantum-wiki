---
title: "SpinControl: Control Software for Prototyping and Benchmarking of Spin-Qubit Devices and Measurement Protocols"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.23316"
summary: "arXiv:2610.23316v1 Announce Type: new Abstract: Quantum computers require software to control the states of the qubits. As the actions on qubits grow in complexity with circuit execution, calibration,"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.23316v1 Announce Type: new Abstract: Quantum computers require software to control the states of the qubits. As the actions on qubits grow in complexity with circuit execution, calibration, and benchmarking, the complexity of the control software grows in tandem. Spin-qubit quantum computers are at a stage where experimentalists need low-level access for tuning and calibration, and quantum algorithm researchers want high-level circuit-level access. In this article, we present the software design of SpinControl. SpinControl integrates three architectural metrics: 1) customizability, to allow prototyping devices and measurement protocols, is achieved by separating data and behaviour; 2) modularity and extensibility are achieved by separating functionalities into different components; and 3) robustness, to reliably execute quantum circuits on many qubits, is achieved by CI pipelines and input validation. SpinControl allows different types of measurements while customizing the instruments used, the pulse or circuit program executed, and the data processing. It allows building standardized experiments from measurement and analysis building blocks and executing these for calibration in a custom and conditional order. SpinControl implements these functionalities alongside robust configuration and data management, a connection to the cloud, and calibration scheduling. Pulse and circuit compilation, virtual gate matrices, as well as spin-qubit-specific GUIs integrated by SpinControl, make heavy use of software packages developed by Delft University of Technology: pulse lib, core-tools (both open source), and QConstruct

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.23316) | 2026-10-19
