import pandas as pd
import os
import re

def extract_github_url(text):
    # Regular expression to match GitHub URLs (with or without http/https prefix)
    github_url_pattern = r'(https?:\/\/)?(github\.com|[\w\-]+\.github\.io)\/[a-zA-Z0-9\-_]+(?:/[a-zA-Z0-9\-_]+)?'

    # Search for the GitHub URL in the text
    match = re.search(github_url_pattern, text)

    if match:
        # Extract the matched URL
        url = match.group(0)
        # If the URL doesn't start with http or https, add https://
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"
        return url
    else:
        return None

import requests
from bs4 import BeautifulSoup

def extract_github_url_from_githubio(githubio_url):
    try:
        # Fetch the content of the github.io webpage
        response = requests.get(githubio_url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search for all anchor tags (<a>) with href attributes
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Check if the href is a github.com URL
            if re.match(r'https?://github\.com/[a-zA-Z0-9\-_]+/[a-zA-Z0-9\-_]+', href):
                return href

        # If no github.com link is found, return None
        return None

    except requests.RequestException as e:
        print(f"Error fetching {githubio_url}: {e}")
        return
        
def process_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.reset_index()

    for index, row in df.iterrows():
      github_url = extract_github_url(df.at[index,'Abstract'])
      if github_url:
        if "github.io" in github_url:
          github_code = extract_github_url_from_githubio(github_url)
          print("Extracted GitHub URL:", github_url, "GitHub code:", github_code)
        else:
          github_code = github_url
          print("Extracted GitHub URL:", github_url)
        df.at[index, 'github_url'] = github_url
        df.at[index, 'github_code'] = github_code
      else:
        print("No GitHub URL found in the text.")
    return df
    
def process_folder(folder_path):
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      if file.endswith('.csv'):
        file_path = os.path.join(root, file)
        print(f"Processing {file_path}...")
        processed_df = process_csv(file_path)
        output_file_path = os.path.join(root, f"processed_{file}")
        processed_df.to_csv(output_file_path, index=False)
        print(f"Saved processed file to {output_file_path}")

def main():
    root_folder = '.'
    process_folder(root_folder)

if __name__ == "__main__":
    main()

