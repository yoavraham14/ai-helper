import json

def query_man_pages():
    try:
        # Load the man pages data
        with open('man_pages.json', 'r') as file:
            man_data = json.load(file)
        
        print("Welcome to the local MAN page assistant!")
        print("Type 'exit' to quit.\n")
        
        while True:
            # Prompt for input
            cmd = input("Enter a command to search (e.g., 'ln'): ").strip()
            
            if cmd.lower() == "exit":
                print("Exiting the assistant. Goodbye!")
                break
            
            # Fetch the command details
            if cmd in man_data:
                print(f"\nMAN Page for '{cmd}':\n")
                print(man_data[cmd][:1000])  # Print a snippet for readability
                print("\n... (truncated for display)\n")
            else:
                print(f"No data found for command '{cmd}'.")
    
    except Exception as e:
        print(f"Error: {e}")

query_man_pages()

