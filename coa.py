import time

NUM_INSTRUCTIONS = 8
STAGES = ["Fetch", "Decode", "Execute"]
NUM_STAGES = len(STAGES)

def simulate_non_pipelined():
    print("\n--- Non-Pipelined Execution ---")
    total_cycles = 0

    for i in range(NUM_INSTRUCTIONS):
        print(f"\nInstruction {i+1}:")
        for stage in STAGES:
            total_cycles += 1
            print(f"Cycle {total_cycles}: {stage}")
            time.sleep(0.1)

    cpi = total_cycles / NUM_INSTRUCTIONS
    print(f"\nTotal cycles (Non-Pipelined): {total_cycles}")
    print(f"CPI (Non-Pipelined): {cpi:.2f}")
    return total_cycles, cpi

def simulate_pipelined():
    print("\n--- Pipelined Execution ---")
    total_cycles = NUM_INSTRUCTIONS + NUM_STAGES - 1
    pipeline = [["" for _ in range(total_cycles)] for _ in range(NUM_INSTRUCTIONS)]

    for i in range(NUM_INSTRUCTIONS):
        for j in range(NUM_STAGES):
            pipeline[i][i + j] = STAGES[j]

    print("\nPipeline Timing Diagram:")
    for i in range(NUM_INSTRUCTIONS):
        print(f"Instr {i+1}: ", end="")
        for cycle in range(total_cycles):
            print(f"{pipeline[i][cycle]:8}", end="")
        print()

    cpi = total_cycles / NUM_INSTRUCTIONS
    print(f"\nTotal cycles (Pipelined): {total_cycles}")
    print(f"CPI (Pipelined): {cpi:.2f}")
    return total_cycles, cpi

def simulate_data_hazard():
    print("\n--- Pipelined Execution with Data Hazard ---")

    total_cycles = NUM_INSTRUCTIONS + NUM_STAGES
    print("Data Hazard detected! 1 cycle stall added.")

    print(f"Total cycles (With Hazard): {total_cycles}")
    cpi = total_cycles / NUM_INSTRUCTIONS
    print(f"CPI (With Hazard): {cpi:.2f}")
    return total_cycles, cpi

non_pipe_cycles, non_pipe_cpi = simulate_non_pipelined()
pipe_cycles, pipe_cpi = simulate_pipelined()
hazard_cycles, hazard_cpi = simulate_data_hazard()

speedup = non_pipe_cycles / pipe_cycles

print("\n===================================")
print("       Performance Summary         ")
print("===================================")
print(f"Non-Pipelined: {non_pipe_cycles} cycles, CPI={non_pipe_cpi:.2f}")
print(f"Pipelined:     {pipe_cycles} cycles, CPI={pipe_cpi:.2f}")
print(f"With Hazard:   {hazard_cycles} cycles, CPI={hazard_cpi:.2f}")
print(f"\nPipeline Speedup: {speedup:.2f}x faster than Non-Pipelined CPU")
print("===================================\n")
