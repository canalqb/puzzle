from bip_utils import Bip44, Bip44Coins, Bip44Changes

nums = [190744522, 3083120, 1068531200, 1674510742, 934348968,
        3314063, 1184170135, 110327241, 1217487446, 113319054,
        903579360, 98128121]

# Converte nums em seed bytes
seed_bytes = b''.join(n.to_bytes(4, 'big') for n in nums)

# Cria wallet BIP44 para Bitcoin
bip44_wallet = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)

# Gera 12 carteiras principais (indices 0-11)
base_addresses = []
for i in range(12):
    addr = bip44_wallet.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
    base_addresses.append(addr)
    print(f"Base {i}: WIF = {addr.PrivateKey().ToWif()}, Address = {addr.PublicKey().ToAddress()}")

print("\nDerivando 1000 endereços para cada base...\n")

# Para cada base, gera 1000 derivados (indices 0-999)
for base_idx, base_addr in enumerate(base_addresses):
    print(f"\nBase {base_idx} derivando 1000 endereços:")
    for i in range(1000):
        derived_addr = bip44_wallet.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
        wif = derived_addr.PrivateKey().ToWif()
        btc_address = derived_addr.PublicKey().ToAddress()
        print(f"Index {i}: WIF={wif}, Address={btc_address}")
