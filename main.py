import random
from recovery_sim import simulate_step
from config import TOTAL_TIME, TIME_STEP

def run_simulation(efficiency):
    results = []
    for t in range(0, TOTAL_TIME, TIME_STEP):
        cpu_load = random.uniform(20, 100)
        data = simulate_step(cpu_load, efficiency)
        data["time"] = t
        results.append(data)
    return results


from visualizer import plot_simulation

if __name__ == "__main__":
    # Try different efficiencies
    for eff in [0.05, 0.10, 0.20]:
        print(f"\n🔧 Simulating with {eff*100:.0f}% Efficiency:")
        sim_results = run_simulation(eff)
        plot_simulation(sim_results)
        total_energy = sum([r["energy_recovered"] for r in sim_results])
        print(f"Total Energy Recovered: {total_energy:.2f} Joules")
