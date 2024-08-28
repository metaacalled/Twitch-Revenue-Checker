# Twitch Revenue Data Fetcher

This Python script fetches revenue data from Twitch for multiple channels and saves the results to a file. It's designed to provide an easy way to monitor various revenue metrics over time for different Twitch channels.

## Features

- Fetches data for multiple Twitch channels.
- Calculates totals for revenue, bits, turbo subscriptions, prime subscriptions, and ads.
- Saves the formatted results, including a progress bar indicating revenue towards a target, to a text file (`results.txt`).

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/metaacalled/twitch-revenue-checker.git
    cd twitch-revenue-checker
    ```

2. **Install the required dependencies**:
    ```bash
    pip install requests
    ```

## Usage

1. **Prepare `oauth_tokens.txt`**:
    - Create a file named `oauth_tokens.txt` in the same directory as the script.
    - Each line should contain an OAuth token, a channel ID, and an identifier, separated by spaces:
      ```
      oauth_token_here channel_id_here identifier_here
      ```
    - Example:
      ```
      abcd1234efgh5678ijkl9012mnop3456 qwerty1234567890 ChannelOne
      xyz9876abcd5432ijkl1098mnop7654 asdfgh0987654321 ChannelTwo
      ```

2. **Run the script**:
    ```bash
    python main.py
    ```

3. **Check the results**:
    - The results will be saved in `results.txt` in the same directory.
    - The file will contain:
      - The total revenue, bits, turbo subscriptions, prime subscriptions, and ads for each channel.
      - A text-based progress bar showing how close the total revenue is to a $50.00 target.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
