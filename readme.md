# lookup my ip

This Python script retrieves your public IP address from multiple online providers. It sends HTTP requests to various services, extracts the IP address from their responses (using optional regular expressions), and measures the time taken for each request. The script outputs the resolved IP addresses along with the duration of each request in seconds.

## Features
- Queries multiple providers to fetch the public IP address.
- Supports regex-based extraction for providers with complex responses.
- Measures and displays the duration of each request.
- Handles errors gracefully if a provider is unavailable or returns an invalid response.

## Install

`pip install requests`

## Usage
Run the script directly using Python:
```bash
python lookup_my_ip.py

