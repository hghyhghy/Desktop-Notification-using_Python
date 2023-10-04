# import time


# importing plyer module to use notifications

import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink water",
            message="Water helps your body to Keep a normal temperature. Lubricate and cushion joints. Protect your spinal cord and other sensitive tissues. Get rid of wastes through urination, perspiration, and bowel movements",
            app_icon="C:\Users\sarka\Desktop\HTMLCSS\MYFIRSTHTML",
            timeout=5,
        )
        time.sleep(60 * 60)
