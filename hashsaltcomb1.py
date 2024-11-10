#hashsaltcomb1.py                                                                                                        
# Function to generate hash:salt combinations and save to output file hashh1.txt
def generate_hash_salt_file(hashfile, salts_file, output_file):
    try:
        # Open the hash file and salts file
        with open(hashfile, 'r') as f_hashes, open(salts_file, 'r') as f_salts, open(output_file, 'w') as f_output:
            # Read all lines from the hash and salts files
            hashes = f_hashes.readlines()
            salts = f_salts.readlines()

            # Debugging: Print the number of hashes and salts
            print(f"Found {len(hashes)} hashes and {len(salts)} salts.")
            
            # Ensure each hash and salt are processed properly
            for sha1_hash in hashes:
                sha1_hash = sha1_hash.strip()  # Remove leading/trailing whitespaces/newlines
                print(f"Processing hash: {sha1_hash}")  # Debugging statement

                for salt in salts:
                    salt = salt.strip()  # Remove leading/trailing whitespaces/newlines
                    print(f"Processing salt: {salt}")  # Debugging statement
                    # Write the combination in the correct format "hash:salt"
                    f_output.write(f"{sha1_hash}:{salt}\n")

            print(f"Hash:salt combinations have been saved to {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to execute the script
if __name__ == "__main__":
    # Define file paths
    hashfile = 'hash_file.txt'  # File containing SHA-1 hashes, one per line
    salts_file = 'salts.txt'   # File containing salts, one per line
    output_file = 'hashh1.txt' # Output file for hash:salt combinations

    # Generate the hash:salt combinations and save to the output file
    generate_hash_salt_file(hashfile, salts_file, output_file)

