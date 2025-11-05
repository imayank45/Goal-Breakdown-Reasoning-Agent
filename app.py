from utils.env_loader import load_env
# Load environment variables
load_env()
from chains.full_reasoning_flow import reasoning_flow

def main():

    # goal
    goal = input("Enter your goal: ")

    # Run the reasoning flow
    result = reasoning_flow.invoke({"goal": goal})

    # Print the result
    print("\n=== FINAL OUTPUT ===\n")
    print(result)
    
if __name__ == "__main__":
    main()