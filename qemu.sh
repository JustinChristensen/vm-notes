#!/usr/bin/env bash

CPUS=${CPUS:-2}
MEM=${MEM:-2048}

qemu-system-x86_64 \
    -device virtio-net,netdev=net0 \
    -netdev user,id=net0,hostfwd=tcp::5522-:22 \
    -hda ~/VirtualBox\ VMs/Ubuntu/Ubuntu.vdi \
    -m $MEM -smp cpus=$CPUS \
    -nographic -s

