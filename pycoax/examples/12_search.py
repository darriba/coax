#!/usr/bin/env python

from common import create_serial, create_interface

from coax import read_address_counter_hi, read_address_counter_lo, read_status, load_address_counter_hi, load_address_counter_lo, write_data, load_mask, search_forward, search_backward

with create_serial() as serial:
    interface = create_interface(serial)

    load_address_counter_hi(interface, 0)
    load_address_counter_lo(interface, 80)

    write_data(interface, bytes.fromhex('a7 84 8b 8b 8e 33 00 96 8e 91 8b 83 19'))

    load_address_counter_hi(interface, 0)
    load_address_counter_lo(interface, 81)

    load_mask(interface, 0xff)

    search_forward(interface, 0x83)

    status = read_status(interface)

    print(status)

    while status.busy:
        status = read_status(interface)

        print(status)

    hi = read_address_counter_hi(interface)
    lo = read_address_counter_lo(interface)

    print(f'hi = {hi}, lo = {lo}')

    search_backward(interface, 0x84)

    status = read_status(interface)

    print(status)

    while status.busy:
        status = read_status(interface)

        print(status)

    hi = read_address_counter_hi(interface)
    lo = read_address_counter_lo(interface)

    print(f'hi = {hi}, lo = {lo}')

    load_mask(interface, 0xf0)

    search_forward(interface, 0x30)

    status = read_status(interface)

    print(status)

    while status.busy:
        status = read_status(interface)

        print(status)

    hi = read_address_counter_hi(interface)
    lo = read_address_counter_lo(interface)

    print(f'hi = {hi}, lo = {lo}')
