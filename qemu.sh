#!/usr/bin/env bash

qemu-system-x86_64 \
    -device virtio-net,netdev=net0 \
    -netdev user,id=net0,hostfwd=tcp::5522-:22 \
    -hda ~/VirtualBox\ VMs/Ubuntu/Ubuntu.vdi \
    -m 2048 -smp cpus=2 \
    -nographic -s

