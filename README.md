# pgh-next-rgbus

This is a simple Python application intended to pull the next arrival times of Pittsburgh Regional Transit
(formerly Pittsburgh Port Authority) buses at a particular stop, and display the number of minutes remaining until arrival on an RGB matrix.
Perfect for the busy professional who needs to know exactly when they need to get out the door!!

<img src="https://camo.githubusercontent.com/c3f47758159d79b33a57932bb550ed11c63b5d238827894b14e97c359db10f45/68747470733a2f2f756331653834303665653838663535373932353232643938313830312e646c2e64726f70626f7875736572636f6e74656e742e636f6d2f63642f302f696e6c696e652f4272363541574a66563432696f3069783465742d50522d656a6971464151706d474834414a44727234733336636d7379557a5f35442d5f5f79623274754c786a6b467859662d307334324131716e4d583958515359357243366d575578516333715a694f514d5379556f5a386d48715f3276632d6143515930714b33476a32433042386f35686d47695271774579416b6d52587034536d47526b516869352d7374625879476448763132764f6d772f66696c6523" alt="An image of a working installation of pgh-next-rgbus, running in a lovely wooden box with an LED RGB display that says &quot;74 20 min&quot;" data-canonical-src="https://uc1e8406ee88f55792522d981801.dl.dropboxusercontent.com/cd/0/inline/Br65AWJfV42io0ix4et-PR-ejiqFAQpmGH4AJDrr4s36cmsyUz_5D-__yb2tuLxjkFxYf-0s42A1qnMX9XQSY5rC6mWUxQc3qZiOQMSyUoZ8mHq_2vc-aCQY0qK3Gj2C0B8o5hmGiRqwEyAkmRXp4SmGRkQhi5-stbXyGdHv12vOmw/file#" style="width: 600px;">

This application is based on the great work over at Adafruit and is compatible with the HUB75-based
RGB matrices that they sell. This project uses a prebuilt version of the `rgbmatrix.so` library with
additional Python support for the `DrawText` method. See [my pull request](https://github.com/adafruit/rpi-rgb-led-matrix/pull/11)
to the Adafruit repo for more information.

This app was built with Nathaniel Fruchter's awesome [pgh-bustime](https://github.com/nhfruchter/pgh-bustime) interface
to the Port Authority's Bustime API. To use the API, you'll need to request an API key from
[their site](http://truetime.portauthority.org/bustime/home.jsp).

This app has only been tested on a Raspberry Pi 3 with a 32x16 RGB matrix. Let me know if you get it working
on another platform!

## Installation

* Clone this repo into a directory of your choice, e.g. `/home/pi/src/`
* Clone the repo that contains the `rgbmatrix` library into the same directory as you cloned this repo:

```
cd /home/pi/src
git clone https://github.com/hzeller/rpi-rgb-led-matrix
```

* Install the required packages:

```
pip3 install -r requirements.txt
```

## Start on boot

1. Install upstart with `sudo apt-get install upstart`
2. Copy the file `pgh-next-rgbus.conf.example` over to `/etc/init/pgh-next-rgbus.conf`
3. Customize the file with your API key, stop ID, direction, etc
4. Enable with `sudo start pgh-next-rgbus`
5. Reboot or power cycle to test -- sign should start up on boot!
