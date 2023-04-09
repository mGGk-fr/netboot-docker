#!/bin/bash

echo "NetBoot docker image builder"
rm -rf netboot
git clone https://github.com/DragonMinded/netboot.git netboot
docker build -t mggk/netboot .