#https://youtu.be/K0_-f2Qp_HI

from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="WATER-BREAK",
            message="Pause, breathe, and hydrate. Your body and brain will thank you. A few sips now = better focus, better energy, better you. Let’s keep it flowing",
            app_icon="notifier\water_tool_icon_175803.ico",
            timeout=5
        )
        time.sleep(2*60*60)