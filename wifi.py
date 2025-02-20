import subprocess

def get_all_wifi_passwords():
    wifi_profiles = {}

    # Get the list of WiFi profiles
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

    # Extract WiFi profile names
    profiles = [i.split(":")[1][1:-1] for i in profiles_data if "All User Profile" in i]

    for profile in profiles:
        # Get the WiFi profile details
        profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')

        # Extract the password from the profile details
        password = None
        for line in profile_info:
            if "Key Content" in line:
                password = line.split(":")[1][1:-1]
                break

        wifi_profiles[profile] = password

    return wifi_profiles

# Fetch and display all WiFi passwords
wifi_passwords = get_all_wifi_passwords()
for wifi, password in wifi_passwords.items():
    print(f"WiFi: {wifi}, Password: {password}")# Write your code here :-)
