import os
import platform
import psutil
import pyaudio
import cv2
import urllib.request


class System_check:
    state: dict = {}

    def __init__(self) -> None:
        pass

    def check(self):
        funcs = [
            self.check_ram,
            self.check_os,
            self.check_system_version,
            self.check_microphone,
            self.check_camera,
            self.check_internet_connection,
        ]

        for i in funcs:
            if i() != True:
                return False

        return True

    def check_ram(self):
        total_ram = psutil.virtual_memory().total / (1024**3)
        self.state["total_ram"] = total_ram
        return total_ram > 4

    def check_os(self):
        system = platform.system()
        self.state["os"] = system
        return system in ["Windows", "Linux"]

    def check_system_version(self):
        system_version = platform.release()
        # print(system_version)
        self.state["os_version"] = system_version
        return bool(system_version)

    def check_microphone(self):
        p = pyaudio.PyAudio()

        try:
            mic_info = p.get_default_input_device_info()
            self.state["mic"] = mic_info
            if mic_info["maxInputChannels"] > 0:
                print("Microphone is available and working.")
                print(f"Microphone Name: {mic_info['name']}")
                print(f"Sample Rate: {int(mic_info['defaultSampleRate'])} Hz")
                return True
            else:
                print("Microphone is not available or not working.")
                return False
        except IOError:
            print("Microphone is not available or not working.")
            return False
        finally:
            p.terminate()

    def check_camera(self):
        try:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Camera is not available or not working.")
                return False
            ret, frame = cap.read()
            if ret:
                self.state["camera"] = ret
                print("Camera is available and working.")
                return True
            else:
                print("Camera is not available or not working.")
                return False
        except Exception as e:
            print(f"Error while checking the camera: {str(e)}")
            return False
        finally:
            if cap.isOpened():
                cap.release()

    def get_state(self):
        return self.state

    def check_internet_connection(self):
        try:
            urllib.request.urlopen("https://www.google.com", timeout=2)
            print("Internet connection is stable.")
            self.state["network"] = "connected"
            return True
        except Exception as e:
            print("No internet connection or connection is unstable.")
            self.state["network"] = "disconnected"
            return False


# obj = Systum_check()
# obj.check()
