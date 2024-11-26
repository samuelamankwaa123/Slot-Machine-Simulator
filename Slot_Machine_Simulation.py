import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define game parameters
symbols = ['Cherry', 'Lemon', 'Bar', 'Jackpot']
probabilities = [0.3, 0.4, 0.2, 0.1]  # Must sum to 1
payouts = {'Cherry': 10, 'Lemon': 5, 'Bar': 20, 'Jackpot': 50}

# Function to simulate one spin of the slot machine
def spin_slot_machine():
    return np.random.choice(symbols, size=3, p=probabilities)

# Function to simulate multiple rounds
def simulate_game_rounds(num_rounds, bet_amount):
    results = []
    total_payout = 0

    for _ in range(num_rounds):
        outcome = spin_slot_machine()
        if len(set(outcome)) == 1:  # Check if all three symbols match
            payout = bet_amount * payouts[outcome[0]]
        else:
            payout = 0
        total_payout += payout
        results.append({
            'Outcome': "-".join(outcome),
            'Payout': payout,
            'Win': payout > 0
        })

    return pd.DataFrame(results), total_payout

# Simulation parameters
num_rounds = 10000  # Number of spins
bet_amount = 1      # Fixed bet amount per spin

# Run the simulation
results_df, total_payout = simulate_game_rounds(num_rounds, bet_amount)

# Calculate total bets and RTP
total_bets = num_rounds * bet_amount
RTP = (total_payout / total_bets) * 100
print(f"Total Bets: {total_bets}")
print(f"Total Payout: {total_payout}")
print(f"Return to Player (RTP): {RTP:.2f}%")

# Analyze results
win_percentage = results_df['Win'].mean() * 100
print(f"Win Percentage: {win_percentage:.2f}%")

# Group by outcomes for frequency analysis
outcome_frequencies = results_df['Outcome'].value_counts()

# Visualization: Payout Distribution
plt.figure(figsize=(10, 6))
results_df['Payout'].plot(kind='hist', bins=50, alpha=0.7, color='skyblue', edgecolor='black')
plt.title("Payout Distribution", fontsize=16)
plt.xlabel("Payout Amount", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualization: Outcome Frequencies
plt.figure(figsize=(12, 6))
outcome_frequencies.plot(kind='bar', color='orange', alpha=0.7, edgecolor='black')
plt.title("Outcome Frequencies", fontsize=16)
plt.xlabel("Outcome", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
