# Sample with Waveshare EPD (Electronic Paper Display) from Jetson Nano

This project is a sample project for the use of Jetson Nano and Waveshare's electronic paper after the completion of [Getting Started with AI on Jetson Nano](https://courses.nvidia.com/courses/course-v1:DLI+S-RX-02+V2/course).

[![Sample with Waveshare e-paper from Jetson Nano](https://img.youtube.com/vi/yWHuR-A8EII/maxresdefault.jpg)](https://youtube.com/shorts/yWHuR-A8EII)

## Hardware Connection

Wire JetsonNano and EPD with reference to [Hardware Connection](https://www.waveshare.com/wiki/1.54inch_e-Paper_Module_Manual#Hardware_Connection_3).

## Environment Building

The following is common to [Getting Started with AI on Jetson Nano](https://courses.nvidia.com/courses/course-v1:DLI+S-RX-02+V2/course) up to the following.

- Getting Started with AI on Jetson Nano
- Setting up your Jetson Nano
- Headless Device Mode
- Setup Steps 1-6

## Run Docker

It may be necessary to run docker with `--privileged` when using e-paper.

For example, run as follows.

```bash
sudo docker run \
  --privileged \
  --runtime nvidia -it \
  --rm \
  --network host \
  --volume ~/nvdli-data:/nvdli-nano/data \
  --device /dev/video0 \
  nvcr.io/nvidia/dli/dli-nano-ai:v2.0.2-r32.7.1
```

## Download EPD Library

Clone the EPD library under accessible data.

```bash
cd /nvdli-nano/data/
git clone --depth 1 https://github.com/waveshare/e-Paper.git
```

## Install Libraries

Install a set of libraries. pillow may need to be reinstalled.

```bash
apt update
apt install -y python3-pip python3-pil python3-numpy
pip3 uninstall -y pillow
pip3 install pillow Jetson.GPIO spidev
```

## Deploy the socket receiving application

Deploy socket_listener.py to `~/nvdli-data`.
The location is tied to `/nvdli-nano/data` in docker.

This program listens to the socket and draws Open/Close to EPD when it receives data. To make the demo easier to read, the text is enlarged and extends off the screen. Reduce font size if necessary.

## Launch the socket receiving application

Launch the socket receiving application

```bash
python3 socket_listener.py
Server started!
```

## Open notebook

Open the notebook in your browser and enter the password. The procedure is the same as for [Getting Started with AI on Jetson Nano](https://courses.nvidia.com/courses/course-v1:DLI+S-RX-02+V2/course).

## Upload opening/closing project

Upload `open_close_hand.ipynb` to `/classification/` and open it.

## Start opening/closing project

Open and execute a hand opening/closing project. Start it in the same way as [Getting Started with AI on Jetson Nano](https://courses.nvidia.com/courses/course-v1:DLI+S-RX-02+V2/course).

## Collect Data, Train, Test

As with [Getting Started with AI on Jetson Nano](https://courses.nvidia.com/courses/course-v1:DLI+S-RX-02+V2/course), collect data, train, and test.If all goes well, the e-paper will be updated by triggering the opening and closing of the hand.

Even though we made use of the partial drawing mode, the EPD module functions at a slower. We made attempts to apply queues and sockets to improve this, but saw that updates to the drawings took several seconds to complete.
