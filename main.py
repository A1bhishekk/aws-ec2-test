import requests

def extract_patch_and_save(raw_url: str, output_file: str) -> str:
    """
    Extract patch content from a GitHub raw URL and save it to a file.

    Parameters:
        raw_url (str): The raw URL of the GitHub patch file.
        output_file (str): The path to the output file where the patch content will be saved.

    Returns:
        str: The extracted raw content of the patch.
    """
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        print(response.status_code)

        # Extract the raw content
        raw_content = response.text

        return raw_content

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# Example GitHub raw URL
github_raw_url = "https://github.com/torvalds/linux/raw/95a69adab9acfc3981c504737a2b6578e4d846ef/tools/hv/hv_kvp_daemon.c"

# Specify the output file path
output_file_path = "patch_file.txt"

# Call the function to extract and save the patch
raw_content=extract_patch_and_save(github_raw_url, output_file_path)
 # Save the raw content to a text file
with open(output_file_path, 'w') as f:
            f.write(raw_content)
print("Patch extracted and saved to file.")
