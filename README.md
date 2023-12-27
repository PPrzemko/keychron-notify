# Keychron Product Availability Checker
This script checks the availability of a specific product variant on the Keychron website and sends a Discord notification if the variant becomes available. The script is designed to be run by a cron job (crontab) at a frequency determined by the user.

## Usage
### 1. Clone the Repository:
`git clone https://github.com/your-username/your-repository.git
cd your-repository`
### 2. Install Dependencies:
`pip install -r requirements.txt`
### 3. Configure Crontab:
Edit your crontab file using the crontab -e command and add the following line to run the script at your desired frequency. For example, to run the script every hour:
`0 * * * * /path/to/python3 /path/to/your-repository/availability_checker.py`

Make sure to replace /path/to/python3 and /path/to/your-repository with the actual paths on your system.

### 4. Configure Script:
Open availability_checker.py and modify the function call:

url1_request: URL to check the product availability.
url1_buy: URL to purchase the product (include the variant parameter).
url1_variant: Variant ID of the product.
discord_webhook_url: Discord webhook URL to receive notifications.
### 5. Run the Script Manually:
You can also run the script manually to check the availability without waiting for the cron job.

`python availability_checker.py
`

## Script Details
The script logs information to a file named keychron.log.
Discord notifications are sent using a webhook when the specified product variant becomes available.
If an error occurs during execution, details are logged, and a notification is sent to Discord.
Feel free to modify and extend the script to check availability for additional products or improve notification messages.

## Disclaimer
This script is provided as-is, and the maintainers are not responsible for any issues or misuse. Use it responsibly and ensure compliance with Keychron's terms of service.





