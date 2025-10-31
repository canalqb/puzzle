from mnemonic import Mnemonic
from bit import Key
from random import shuffle, seed
import os

# Semente para não repetir combinações
seed(1760457599067)

mnemo = Mnemonic("english")

# Sua lista de números e geração de mnemonic
nums = [
    190744522, 3083120, 1068531200, 1674510742,
    934348968, 3314063, 1184170135, 110327241,
    1217487446, 113319054, 903579360, 98128121
]

# Gerar entropia a partir dos números
entropy_bytes = b""
for n in nums:
    entropy_bytes += n.to_bytes(4, byteorder='big')

entropy_12 = entropy_bytes[:16]
mnemonic_12 = mnemo.to_mnemonic(entropy_12)

print("Mnemonic original (12 palavras):")
print(mnemonic_12)

# Divide em palavras
words = mnemonic_12.split()

# Gerar permutações aleatórias de 12 palavras sem repetir
valid_phrases = set()
tried_phrases = set()
wif_list = []

for _ in range(1000000):  # tenta 10.000 combinações aleatórias
    shuffle(words)
    phrase = ' '.join(words)
    
    if phrase in tried_phrases:
        continue  # já tentamos esta combinação
    tried_phrases.add(phrase)

    try:
        if mnemo.check(phrase):
            entropy_hex = mnemo.to_entropy(phrase).hex()
            priv_int = int(entropy_hex, 16)
            key = Key.from_int(priv_int)
            wif = key.to_wif()
            wif_list.append(wif)
    except:
        pass  # frases inválidas geram erro

# Salvar WIFs em arquivos de 20000
os.makedirs("wifs", exist_ok=True)  # cria pasta "wifs" se não existir

for i in range(0, len(wif_list), 20000):
    batch = wif_list[i:i+20000]
    file_index = (i // 20000) + 1
    filename = f"wifs/wif_puzzle_{file_index}.txt"
    with open(filename, "w") as f:
        f.write("\n".join(batch))

print(f"\nTotal de WIFs salvos: {len(wif_list)} em {len(wif_list)//20000 + 1} arquivos.", end="\r")
