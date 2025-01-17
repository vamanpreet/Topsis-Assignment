import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, result_file):
    try:
        # Load the input file
        data = pd.read_csv(input_file)
        
        if data.shape[1] < 3:
            raise ValueError("Input file must contain at least three columns.")
        
        # Validate weights and impacts
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
        if len(weights) != data.shape[1] - 1 or len(impacts) != data.shape[1] - 1:
            raise ValueError("Number of weights and impacts must match the number of criteria.")
        if not all(i in ['+', '-'] for i in impacts):
            raise ValueError("Impacts must be either '+' or '-'.")

        # Extract data for TOPSIS
        names = data.iloc[:, 0]
        values = data.iloc[:, 1:].values.astype(float)

        # Normalize the matrix
        norm_matrix = values / np.sqrt((values ** 2).sum(axis = 0))

        # Weighted normalized matrix
        weighted_matrix = norm_matrix * weights

        # Determine Ideal and Negative-Ideal Solutions
        ideal_solution = []
        negative_ideal_solution = []
        for i, impact in enumerate(impacts):
            if impact == '+':
                ideal_solution.append(weighted_matrix[:, i].max())
                negative_ideal_solution.append(weighted_matrix[:, i].min())
            else:
                ideal_solution.append(weighted_matrix[:, i].min())
                negative_ideal_solution.append(weighted_matrix[:, i].max())
        
        ideal_solution = np.array(ideal_solution)
        negative_ideal_solution = np.array(negative_ideal_solution)

        # Calculate separation measures
        separation_ideal = np.sqrt(((weighted_matrix - ideal_solution) ** 2).sum(axis = 1))
        separation_negative = np.sqrt(((weighted_matrix - negative_ideal_solution) ** 2).sum(axis = 1))

        # Calculate TOPSIS Score
        scores = separation_negative / (separation_ideal + separation_negative)

        # Add scores and rankings to the data
        data['Topsis Score'] = scores
        data['Rank'] = scores.argsort()[::-1].argsort() + 1

        # Save results to file
        data.to_csv(result_file, index=False)
        print(f"Results saved to {result_file}")
    
    except FileNotFoundError:
        print("Error: Input file not found.")
    
    except ValueError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")



if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    else:
        _, input_file, weights, impacts, result_file = sys.argv
        topsis(input_file, weights, impacts, result_file)
