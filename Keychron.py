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


def check_product_availability(request_url, buy_url, variant_id, discord_webhook_url):
    response = requests.get(request_url)

    if response.status_code == 200:
        product_data = response.json()
        variants = product_data.get("variants", [])


        for variant in variants:
            if variant.get("id") == variant_id:
                availability = variant.get("available", False)
                title = variant.get("title", "Unknown Variant")

                if availability:
                    print(f"The variant '{title}' is available!")
                    message = f"@everyone The variant '{title}' is now available! ??\nBuy it here: {buy_url}"
                    send_discord_notification(message=message, webhook_url=discord_webhook_url)
                else:
                    message = f"The variant '{title}' is currently not available."
                    logging.info(message)
                    print(message)
                break  # Stop iterating once the variant is found
        else:
            message = f"Variant with ID {variant_id} not found in the response."
            logging.warning(message)
            print(message)
    else:
        message = f"Failed to fetch data from {request_url}. Status code: {response.status_code}"
        send_discord_notification(message=message, webhook_url=discord_webhook_url)
        print(message)


def main():
    # URLs to check
    url1_request = "https://keychron.de/de/products/keychron-q6-pro-qmk-via-wireless-custom-mechanical-keyboard-iso-layout-collection.js"
    url1_buy = "https://keychron.de/de/products/keychron-q6-pro-qmk-via-wireless-custom-mechanical-keyboard-iso-layout-collection?variant=41417271705737"
    url1_variant = 41417271705737

    # Discord webhook URL
    discord_webhook_url = "https://discord.com/api/webhooks/demo/demo"

    # Check availability for both URLs and send Discord notification if available
    check_product_availability(url1_request, url1_buy, url1_variant, discord_webhook_url)


def main2():
    pass


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.exception("main crashed. Error: %s", e)
