import MT25QL01GBBB_20231023 as MT25QL01GBBB

Flash = MT25QL01GBBB.flash()

# テスト1: アドレス 0x03761000 から最初の256バイトを読み出し
print("=== テスト1: 0x03761000 から256バイト読み出し ===")
test_data = Flash.READ_DATA_BYTES_SMF(0x03761000, 256)
print(f"読み出し結果 (先頭32バイト): {test_data[:32]}")
print(f"16進数表示: {' '.join(f'{b:02x}' for b in test_data[:32])}")

# テスト2: アドレス 0x00000000 から最初の256バイトを読み出し（フラッシュ開始位置）
print("\n=== テスト2: 0x00000000 から256バイト読み出し ===")
test_data2 = Flash.READ_DATA_BYTES_SMF(0x00000000, 256)
print(f"読み出し結果 (先頭32バイト): {test_data2[:32]}")
print(f"16進数表示: {' '.join(f'{b:02x}' for b in test_data2[:32])}")

# テスト3: JPEGマジックナンバーを探す（アドレス範囲をスキャン）
print("\n=== テスト3: JPEGマジックナンバー(FF D8 FF)を探索 ===")
search_addresses = [0x00000000, 0x01000000, 0x02000000, 0x03000000, 0x03700000, 0x03750000, 0x03761000]
for addr in search_addresses:
    try:
        data = Flash.READ_DATA_BYTES_SMF(addr, 16)
        print(f"アドレス {hex(addr)}: {' '.join(f'{b:02x}' for b in data)}")
    except Exception as e:
        print(f"アドレス {hex(addr)}: エラー - {e}")

print("\n=== テスト完了 ===")
