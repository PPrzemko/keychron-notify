import logging

import requests

logging.basicConfig(filename='keychron.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='a')


def send_discord_notification(message, webhook_url):
    data = {"content": message}

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        message = "Discord notification sent successfully!"
        print(message)
        logging.warning(message)
    else:
        message = f"Failed to send Discord notification. Status code: {response.status_code}"
        print(message)
        logging.warning(message)


def check_product_availability(request_url, buy_url, discord_webhook_url):
    response = requests.get(request_url)

    if response.status_code == 200:
        product_data = response.json()
        availability = product_data.get("available", False)
        title = product_data.get("title", "Unknown Product")

        if availability:
            print(f"The product '{title}' is available!")
            message = f"@everyone The product '{title}' is now available! ??\nBuy it here: {buy_url}"
            send_discord_notification(message=message, webhook_url=discord_webhook_url)
        else:
            message = f"The product '{title}' is currently not available."
            logging.info(message)
            print(message)
    else:
        message = f"Failed to fetch data from {request_url}. Status code: {response.status_code}"
        send_discord_notification(message=message, webhook_url=discord_webhook_url)
        print(message)

def main():
    # URLs to check
    url1_request = "https://keychron.de/de/collections/all-products/products/keychron-m6-wireless-mouse.js"
    url1_buy = "https://keychron.de/de/collections/all-products/products/keychron-m6-wireless-mouse"

    # Discord webhook URL
    discord_webhook_url = "https://discord.com/api/webhooks/demo/demo"

    # Check availability for both URLs and send Discord notification if available
    check_product_availability(url1_request, url1_buy, discord_webhook_url)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.exception("main crashed. Error: %s", e)