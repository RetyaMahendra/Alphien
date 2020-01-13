import os

# iperf requirement
try:
    import iperf3
except ImportError:
    print ("install iperf3 package .......")
    os.system("apt install iperf3 -y > /dev/null 2>&1")
    os.system("apt install python3-pip -y  > /dev/null 2>&1")
    os.system("pip3 install iperf3 > /dev/null 2>&1")
finally:
    import iperf3

# client initialization
client = iperf3.Client()
client.duration = 10

# iperf server ip
client.server_hostname = '10.153.66.56'
client.port = 5201

print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
result = client.run()

if result.error:
    print(result.error)
else:
    print(result.sent_Mbps)
