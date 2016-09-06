# pgh-next-rgbus

This is a simple application intended to pull the next arrival time of Pittsburgh Port Authority bus and display the number of minutes remaining on an RGB matrix.
Perfect for the busy professional who needs to know exactly when they need to get out the door!!

This application is based on the great work over at Adafruit and is compatible with the HUB75-based RGB matrices that they sell.

Built with Nathaniel Fruchter's awesome https://github.com/nhfruchter/pgh-bustime.

## Start on boot

1. Install upstart with `sudo apt-get install upstart`
2. Copy the file `pgh-next-rgbus.conf.example` over to `/etc/init/pgh-next-rgbus.conf`
3. Customize the file with your API key, stop ID, direction, etc
4. Enable with `sudo start pgh-next-rgbus`
5. Reboot or power cycle to test -- sign should start up on boot!
