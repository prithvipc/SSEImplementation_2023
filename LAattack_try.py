import requests
import json

SEARCH_ENDPOINT = 'http://localhost:5000/search'

# This function simulates the leakage of search patterns
def simulate_search_leakage(keyword):
    response = requests.post(SEARCH_ENDPOINT, data={'keyword': keyword})
    if response.status_code == 200:
        result = response.json()
        return result['result'], result['search_time']
    else:
        print(f"Error with search: {response.status_code}")
        return None, None

def analyze_leakage(num_of_searches=10):
    # Dictionary to hold keyword frequencies
    keyword_to_frequency = {}
    
    for _ in range(num_of_searches):
        keyword = " victor.lamadrid@enron.com"
        
        results, search_time = simulate_search_leakage(keyword)
        if results is not None:
            keyword_to_frequency[keyword] = len(results), search_time
    
    # Sort the keywords by the number of results (frequency) descending
    sorted_keywords = sorted(keyword_to_frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_keywords

#main
def leakage_abuse_attack():
    # First, analyze the leakage to guess the most likely keywords
    sorted_keywords = analyze_leakage()

    for keyword, data in sorted_keywords:
        print(f"Keyword '{keyword}' has {data[0]} results and took {data[1]} ms to search.")

if __name__ == "__main__":
    leakage_abuse_attack()
