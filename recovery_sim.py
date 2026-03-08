from config import MAX_CPU_LOAD, MAX_HEAT_OUTPUT, THERMOELECTRIC_EFFICIENCY, TIME_STEP

def simulate_step(cpu_load_percent, efficiency=THERMOELECTRIC_EFFICIENCY):
    cpu_load_percent = max(0, min(cpu_load_percent, MAX_CPU_LOAD))
    heat_generated = (cpu_load_percent / 100) * MAX_HEAT_OUTPUT  # Watts
    recoverable_heat = heat_generated * efficiency
    energy_recovered = recoverable_heat * TIME_STEP  # in Joules

    return {
        "cpu_load": cpu_load_percent,
        "heat_generated": heat_generated,
        "energy_recovered": energy_recovered
    }

