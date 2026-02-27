from core.orchestrator import handle_request

if __name__ == "__main__":
    user_input = input("Enter your marketing requirement: ")
    result = handle_request(user_input)
    print("\n===== FINAL OUTPUT =====\n")
    print(result)
