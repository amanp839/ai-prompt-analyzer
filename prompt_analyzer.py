def analyze_prompt(prompt):
    score = 0
    suggestions = []

    # Check clarity
    if len(prompt.split()) >= 5:
        score += 1
    else:
        suggestions.append("Add more detail to make the prompt clearer.")

    # Check context
    context_words = ["context", "background", "for", "about", "because"]

    if any(word in prompt.lower() for word in context_words):
        score += 1
    else:
        suggestions.append("Add some context or background information.")

    # Check specificity
    specific_words = ["specific", "exactly", "step-by-step", "example", "format"]

    if any(word in prompt.lower() for word in specific_words):
        score += 1
    else:
        suggestions.append("Make the expected result more specific.")

    # Check output instructions
    output_words = ["list", "table", "explain", "summarize", "create", "format"]

    if any(word in prompt.lower() for word in output_words):
        score += 1
    else:
        suggestions.append("Specify the format or type of output you want.")

    percentage = int((score / 4) * 100)

    print("\n--- AI Prompt Analyzer ---")
    print(f"Prompt Quality Score: {percentage}%")

    if percentage == 100:
        print("Excellent prompt! 🎯")
    elif percentage >= 75:
        print("Good prompt! 👍")
    elif percentage >= 50:
        print("Your prompt can be improved. 💡")
    else:
        print("Your prompt needs more detail. 📝")

    if suggestions:
        print("\nSuggestions:")

        for suggestion in suggestions:
            print(f"- {suggestion}")


print("🤖 AI Prompt Analyzer")
print("---------------------")

user_prompt = input("Enter your prompt: ")

analyze_prompt(user_prompt)
