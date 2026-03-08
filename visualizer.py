import matplotlib.pyplot as plt

def plot_simulation(results):
    time = [r["time"] for r in results]
    cpu_load = [r["cpu_load"] for r in results]
    heat = [r["heat_generated"] for r in results]
    energy = [r["energy_recovered"] for r in results]

    plt.figure(figsize=(12, 6))

    # Plot 1 - CPU Load
    plt.subplot(3, 1, 1)
    plt.plot(time, cpu_load, color="blue")
    plt.ylabel("CPU Load (%)")
    plt.title("CPU Load Over Time")

    # Plot 2 - Heat Generated
    plt.subplot(3, 1, 2)
    plt.plot(time, heat, color="red")
    plt.ylabel("Heat Generated (Watts)")
    plt.title("Heat Output Over Time")

    # Plot 3 - Energy Recovered
    plt.subplot(3, 1, 3)
    plt.plot(time, energy, color="green")
    plt.ylabel("Energy Recovered (Joules)")
    plt.xlabel("Time (seconds)")
    plt.title("Energy Recovery Over Time")

    plt.tight_layout()
    plt.show()
