import serial
import time

def read_moisture_data():
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        time.sleep(2)  # Wait for the connection to establish

        while True:
            if ser.in_waiting > 0:
                moisture_level = ser.readline().decode('utf-8').strip()
                print(f"Moisture Level: {moisture_level}")

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Serial connection closed")

if __name__ == "__main__":
    while True:
        read_moisture_data()
        time.sleep(10)  # Wait for a while before attempting to reconnect
