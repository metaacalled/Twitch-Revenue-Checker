import requests
from datetime import datetime

def calculate_totals(response):
    total_revenue = 0
    total_bits = 0
    total_turbo = 0
    total_prime_subs = 0
    total_ads = 0
    for data in response:
        if 'data' in data and 'revenues' in data['data']:
            revenue_timeseries = data['data']['revenues']['revenueTimeSeries']
            for item in revenue_timeseries:
                total_revenue += item.get('total', 0)
                total_bits += item.get('bits', 0)
                total_turbo += item.get('turbo', 0)
                total_prime_subs += item.get('primeSubscriptions', 0)
                total_ads += item.get('ads', 0)

    return {
        'Total Revenue': total_revenue,
        'Total Bits': total_bits,
        'Total Turbo': total_turbo,
        'Total Prime Subscriptions': total_prime_subs,
        'Total Ads': total_ads
    }

def fetch_data(oauth_token, channel_id):
    url = "https://gql.twitch.tv/gql"
    headers = {
        "Authorization": f"OAuth {oauth_token}"
    }
    data = [
        {
            "operationName": "Channel_Analytics_Revenue",
            "variables": {
                "startAt": "2021-01-01T00:00:00.000Z",
                "endAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "timeZone": "UTC",
                "granularity": "DAY",
                "channelID": channel_id
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "bcf988e9ee3597a7683cc7f682a4b78e76f0b9bf07e921de1a46e8838c410eab"
                }
            }
        },
    ]

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return calculate_totals(response.json())
    else:
        return f"Failed with status code: {response.status_code}"

def format_result(result):
    return {key: f"${value / 100:.2f}" if isinstance(value, int) else value for key, value in result.items()}

def save_results_to_file(identifier, formatted_result, filename="results.txt"):
    with open(filename, "a") as file:
        file.write(f"\nResults for {identifier}:\n")
        for key, value in formatted_result.items():
            file.write(f"{key}: {value}\n")
        
        total_revenue = float(formatted_result['Total Revenue'][1:])
        target_revenue = 50.0
        percentage = (total_revenue / target_revenue) * 100
        file.write(f"Payout Progress: [{'#' * int(percentage // 2)}{'-' * (50 - int(percentage // 2))}] {percentage:.2f}%\n")
        file.write("\n")

def main():
    print("Dumping everything into results.txt.")
    print("Please, wait.")
    with open("oauth_tokens.txt", "r") as file:
        lines = file.readlines()
    
    for line in lines:
        oauth_token, channel_id, identifier = line.strip().split()
        if oauth_token == "oauth_token_here":
            continue
        result = fetch_data(oauth_token, channel_id)
        if isinstance(result, str):  # Handle error message
            with open("results.txt", "a") as file:
                file.write(f"Error fetching data for {identifier}: {result}\n")
        else:
            formatted_result = format_result(result)
            save_results_to_file(identifier, formatted_result)

    current_time = datetime.now().strftime("%I:%M %p")
    with open("results.txt", "a") as file:
        file.write(f"Last Updated: {current_time}\n")
    print("Done!")
    input("Press any key to continue.")

if __name__ == "__main__":
    main()
