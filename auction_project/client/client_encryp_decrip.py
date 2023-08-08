import random


class A3_Encryption:

    def __init__(self):
        self.encrypted_data = None
        self.random_key: int = random.randint(1, 65536)

    def start_encryption(self, text, key):
        self.encrypted_data: str = ""

        total_key: int = 0

        for i in key:
            total_key += ord(i)

        for i in text:
            encrypted_bin: int = int(bin(ord(i))[2:]) ^ int(bin(total_key)[2:])

            double_encrypted_bin: int = encrypted_bin ^ int(bin(self.random_key)[2:])

            self.encrypted_data += hex(double_encrypted_bin) + 'X'

        # char to unicode(ASCII) by ord() to bin to int to hex(str)
        self.encrypted_data += hex(int(bin(total_key)[2:])) + 'X' + hex(int(bin(self.random_key)[2:]))
        return self.encrypted_data


class A3_Decryption:
    def __init__(self):
        self.data_list: list = []
        self.key_list: list = []
        self.actual_data: str = ""

    def start_decryption(self, data_encrypted: str):
        self.data_list = data_encrypted.split('X')

        self.key_list = self.data_list[-2:]
        self.data_list = self.data_list[:len(self.data_list) - 2]

        # getting total key and random key
        for i in range(len(self.key_list)):
            self.key_list[i] = int(self.key_list[i], 16)  # hex to int

        for i in range(len(self.data_list)):
            self.data_list[i]: int = int(self.data_list[i], 16) # hex to int
            self.data_list[i]: int = self.data_list[i] ^ self.key_list[1]  # xor double_encrypted_bin and random_key
            self.data_list[i]: int = self.data_list[i] ^ self.key_list[0]  # xor first_encrypted_bin and total_key
            self.data_list[i]: str = "0b" + str(self.data_list[i])  # re-adding Ob to binary value and
            self.data_list[i] = chr(int(self.data_list[i], 2))  # changing it back to int, which is actually ascii value
            self.actual_data += self.data_list[i]
        return self.actual_data


# if __name__ == "__main__":
#     encryption = A3_Encryption()
#     encrypted_data: str = encryption.start_encryption("What's your name?", "hello")  # accepting return value
#
#     print(encrypted_data)
#     decryption = A3_Decryption()
#     decrypted_data: str = decryption.start_decryption(encrypted_data)
#     print(decrypted_data)
