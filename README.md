# 🔋 CPU Heat Recovery Simulation (Inspired by F1 MGU-H)

This project simulates how a computer CPU could recover waste heat as usable energy — inspired by the **MGU-H** system used in Formula 1 hybrid power units.

Just as the MGU-H converts turbocharger heat into electrical energy in F1 cars, this model explores whether similar energy recovery could work in CPU systems using **thermoelectric generators**.

---

## 🎯 Project Goals

- Simulate heat generation based on CPU load
- Model thermoelectric energy recovery at various efficiency levels
- Visualize how CPU load, heat, and recovered energy evolve over time
- Demonstrate how emerging technology might enable energy recycling in computing

---

## ⚙️ How It Works

At each time step:
- CPU load (%) determines heat output (Watts)
- A configurable **conversion efficiency** simulates thermoelectric recovery
- Recovered energy is calculated and plotted over time

---

## 📊 Key Features

- CPU Load, Heat Output, and Energy Recovery plotted over time
- Supports 5%, 10%, and 20% thermoelectric efficiency simulations
- Total energy recovered displayed for each run
- Modular code: `main.py`, `config.py`, `recovery_sim.py`, `visualizer.py`

---

## 📌 Sample Output

> Example: 60-second simulation with 10% efficiency  
> ✅ Total Energy Recovered: **382.43 Joules**

![Sample Plot](link-to-your-plot-if-hosted)

---

## 🧪 Try It Yourself

```bash
git clone https://github.com/your-username/cpu-heat-recovery-sim.git
cd cpu-heat-recovery-sim
python main.py
