import MT25QL01GBBB_20231023 as MT25QL01GBBB

Flash = MT25QL01GBBB.flash()

# 小さいテストで確認
print("=== チャンク読み込みテスト ===")
TEST_ADDRESS = 0x03761000

# チャンク1: 0x03761000 から 256バイト
chunk1 = Flash.READ_DATA_BYTES_SMF(TEST_ADDRESS, 256)
print(f"チャンク1 (256バイト, {hex(TEST_ADDRESS)}):")
print(f"  先頭32バイト: {' '.join(f'{b:02x}' for b in chunk1[:32])}")
print(f"  チャンク長: {len(chunk1)}")

# チャンク2: 0x03761100 から 256バイト
chunk2 = Flash.READ_DATA_BYTES_SMF(TEST_ADDRESS + 256, 256)
print(f"\nチャンク2 (256バイト, {hex(TEST_ADDRESS + 256)}):")
print(f"  先頭32バイト: {' '.join(f'{b:02x}' for b in chunk2[:32])}")
print(f"  チャンク長: {len(chunk2)}")

# 両チャンク連結
combined = chunk1 + chunk2
print(f"\n連結後 (512バイト): 先頭32バイト {' '.join(f'{b:02x}' for b in combined[:32])}")

# 一度に読み出し
all_at_once = Flash.READ_DATA_BYTES_SMF(TEST_ADDRESS, 512)
print(f"\n一度に読み出し (512バイト): 先頭32バイト {' '.join(f'{b:02x}' for b in all_at_once[:32])}")

# 比較
print(f"\nチャンク分割 == 一度に読み出し: {combined == all_at_once}")
if combined != all_at_once:
    print(f"チャンク分割の長さ: {len(combined)}")
    print(f"一度に読み出しの長さ: {len(all_at_once)}")
    # 最初の違いを探す
    for i in range(min(len(combined), len(all_at_once))):
        if combined[i] != all_at_once[i]:
            print(f"最初の違い: 位置 {i}, チャンク分割={combined[i]:02x}, 一度に読み出し={all_at_once[i]:02x}")
            break
