# Garage Remote Raspi

## Install intructions

Deploy the `garage-remote-raspi.service` file
<code>

    sudo cp garage-remote-raspi.service /etc/systemd/system

    sudo systemctl daemon-reload

    sudo systemctl start garage-remote-raspi.service
</code>


To check the status of the service:
<code>

    sudo systemctl status garage-remote-raspi.service
</code>


To stop the service:
<code>

    sudo systemctl stop garage-remote-raspi.service
</code>

To enable the service on every reboot:
<code>

    sudo systemctl enable garage-remote-raspi.service
</code>


To disable the service on every reboot
<code>

    sudo systemctl disable garage-remote-raspi.service
</code>