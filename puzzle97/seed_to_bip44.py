from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

# Seus números
nums = [190744522, 3083120, 1068531200, 1674510742, 934348968,
        3314063, 1184170135, 110327241, 1217487446, 113319054,
        903579360, 98128121]

# 1. Converte nums em bytes (32 bits cada)
seed_bytes = b''.join(n.to_bytes(4, 'big') for n in nums)

# 2. Pega os primeiros 32 bytes para gerar a mnemonic (BIP39 256 bits)
entropy_bytes = seed_bytes[:32]

# 3. Gera a mnemonic BIP39 em inglês
mnemonic = Bip39MnemonicGenerator().FromEntropy(entropy_bytes)
print("Mnemonic BIP39 (en):")
print(mnemonic)

# 4. Gera a seed a partir da mnemonic
seed = Bip39SeedGenerator(mnemonic).Generate()

# 5. Cria wallet BIP44 Bitcoin
bip44_wallet = Bip44.FromSeed(seed, Bip44Coins.BITCOIN)

# 6. Deriva os primeiros 12 endereços externos
for i in range(12):
    addr = bip44_wallet.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
    print(f"Index {i}: WIF={addr.PrivateKey().ToWif()}, Address={addr.PublicKey().ToAddress()}")
