import MT25QL01GBBB_20231023 as MT25QL01GBBB

Flash = MT25QL01GBBB.flash()

keydata = input("input dump start address or shortcut key\n")

CORN_MSN_TMBHEAD_DATA_ADDRESS = 0x123400


if keydata == 'a':
    readAddress = CORN_MSN_TMBHEAD_DATA_ADDRESS

# データ読み込み
data = Flash.READ_DATA_BYTES2_SMF(readAddress, 4096)

# ヘッダーの表示
print(f"Dumping data starting from address: {hex(readAddress)}")
print("      ", end="")
for i in range(16):
    print(f"{hex(i)[2:].zfill(2)} ", end="")
print("  | ASCII Characters |")

# データの表示
for j in range(16):
    print(f"{hex(j)[2:].zfill(3)}:", end=" ")

    # 16進数データの表示
    for i in range(16):
        print(f"{hex(data[i + j * 16])[2:].zfill(2)} ", end="")

    # ASCII文字の表示
    ascii_str = ""
    for i in range(16):
        byte = data[i + j * 16]
        if 32 <= byte <= 126:
            ascii_str += chr(byte)
        else:
            ascii_str += "."

    print(f" | {ascii_str}")

print("\nDump completed.")
