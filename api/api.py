# Lab 6: Using RESTCONF to Connect to a Cisco Device

## Objective:

# In this lab, we'll explore how to use RESTCONF, a modern API protocol for networking devices, to retrieve interface details from a Cisco device. Instead of traditional methods like SSH or Telnet, RESTCONF allows us to use standard HTTP methods to interact with the device.

# ## Prerequisites:

# 1. A Python environment with the `requests` library installed. If not installed, you can add it with pip:

#     ```bash
#     pip install requests
#     ```

# 2. Familiarity with REST APIs and RESTCONF.

# ## Steps:

# ### 1. Set Up Your Python Environment:

# Install necessary libraries if you haven't done so already:

# ```bash
# pip install requests
# ```

# ### 2. Write the Python Script:

# You'll be using the provided script as a base. This script connects to the device using RESTCONF and retrieves interface details.

# ```python
import requests

# Disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# Device details
# HOST = 'sandbox-iosxe-recomm-1.cisco.com'
# USER = 'developer'
# PASS = 'lastorangerestoreball8876'
HOST = '192.168.1.110'
USER = 'cisco'
PASS = 'cisco'

def main():
    """Retrieve Interface details from the device via RESTCONF."""
    
    # Construct the URL
    url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"
    
    # Headers for the GET request
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }
    
    # Make the GET request
    response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
    
    # Print the returned JSON data
    print(response.text)

if __name__ == '__main__':
    main()
#```

### 3. Save and Execute the Script:

#After saving your Python script, run it. The output will provide interface details in JSON format, retrieved using RESTCONF from your Cisco device.

## Conclusion:

#This lab demonstrated how RESTCONF can be a powerful tool for network automation, providing a more modern and flexible approach compared to traditional CLI methods. As the networking world moves more towards automation and programmability, understanding and using APIs like RESTCONF becomes increasingly essential.