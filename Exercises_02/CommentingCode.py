# Continuous loop until [ctrl][c]
        while True:
            # Read the first byte, if no byte, loop
            byte1 = Serial_Port1.read(1)
            if len(byte1) <1:
                break
            # Check for UBX header = xB5 and X62, Unicode = µb
            if byte1 == b"\xb5":
                byte2 = Serial_Port1.read(1)
                if len(byte2) < 1:
                    break
                if byte2 == b"\x62":
                    # Get the UBX class
                    byte3 = Serial_Port1.read(1)
                    # Get the UBX message
                    byte4 = Serial_Port1.read(1)
                    # Get the UBX payload length
                    byte5and6 = Serial_Port1.read(2)
                    # Calculate the length of the payload
                    length_of_payload = int.from_bytes(byte5and6, "little", signed=False)
                    # Read the buffer for the payload length
                    ubx_payload = Serial_Port1.read(length_of_payload)
                    # Last two bytes are 2*CRC, save them for later use
                    ubx_crc_a = Serial_Port1.read(1)
                    ubx_crc_b = Serial_Port1.read(1)
                    # Calculate CRC using CLASS + MESSAGE + LENGTH + PAYLOAD
                    payload_for_crc = byte3 + byte4 + byte5and6 + ubx_payload
                    # If the CRC is good, proceed
                    if ubx_crc(payload_for_crc,ubx_crc_a, ubx_crc_b):
                        # Log the ubx bytes
                        payload_for_save = byte1 + byte2 + payload_for_crc + ubx_crc_a + ubx_crc_b
                        with open (ubx_log_file, 'ab') as file:
                            file.write(payload_for_save)