import os

output_dir = "output_responses"
final_output = "final_combined_output.txt"

with open(final_output, "w", encoding="utf-8") as final_file:
    for i in range(1, 14):  # Adjust range as needed
        response_filename = os.path.join(output_dir, f"response_{i}.txt")
        if os.path.exists(response_filename):
            with open(response_filename, "r", encoding="utf-8") as response_file:
                final_file.write(response_file.read())
                final_file.write("\n\n")  # Add space between chunks
        else:
            print(f"{response_filename} not found. Skipping...")

print(f"All responses combined into {final_output}.")
