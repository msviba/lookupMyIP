import requests
import re
import time

providers = [
    # Each provider has: [URL, regex (or None if not needed), resolved IP (initially None), duration (initially None)]
    ["https://api.ipify.org?format=text", None, None, None],
    ["https://ipv4.mojeip.cz/index2.php?ipv4_raw=1&format=text", None, None, None],
    ["https://ipinfo.io/what-is-my-ip", r"(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)", None, None],
    ["https://www.myexternalip.com/raw", None, None, None],
    ["https://checkip.amazonaws.com/", None, None, None],
    ["https://api64.ipify.org?format=text", None, None, None],
    ["https://api.myip.com", r'"ip":"([^"]+)"', None, None],
    ["https://ifconfig.co/ip", None, None, None],
    ["https://icanhazip.com", None, None, None],
    ["https://myexternalip.com/raw", None, None, None],
    ["https://www.trackip.net/ip", None, None, None],
]

def fetch_ip(provider):
    url, regex, _, _ = provider
    try:
        start_time = time.time()
        response = requests.get(url)
        duration = time.time() - start_time
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        if regex:
            # Use regex to extract IP from the response text
            match = re.search(regex, response.text)
            return match.group(1) if match else None, duration
        else:
            # Return the response text directly if no regex is needed
            return response.text.strip(), duration
    except requests.RequestException as e:
        print(f"Error retrieving public IP from {url}: {e}")
        return None, None

if __name__ == "__main__":
    for provider in providers:
        ip, duration = fetch_ip(provider)
        provider[2] = ip  # Update the resolved IP in the provider list
        provider[3] = duration  # Update the duration in the provider list

    print("Resolved IP addresses and durations:")
    for provider in providers:
        ip, duration = provider[2], provider[3]
        print(f"IP: {ip}, URL: {provider[0]}, Duration: {duration:.2f} seconds")
