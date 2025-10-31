from mnemonic import Mnemonic
from bit import Key

word_list = [
    "adult","all","angle","animal","appear","away","base","between","bird","black",
    "blue","book","border","bottom","brown","cable","can","color","column","common",
    "cover","cream","depth","edge","electric","emotion","empty","exact","face","first",
    "focus","frame","front","general","globe","green","hand","hold","human","inner",
    "inside","kitchen","large","left","light","man","more","morning","move","neutral",
    "next","number","observe","obvious","only","open","order","other","page","palm",
    "panel","people","person","photo","pink","plastic","plate","position","possible",
    "power","raven","right","scene","script","short","side","similar","skin","small",
    "smile","space","stick","stone","surprise","table","text","that","there","thumb",
    "tone","top","travel","typical","urban","vehicle","voice","warm","weather","wide",
    "woman","wood","world","yellow"
]

mnemo = Mnemonic("english")
n = len(word_list)
length = 12  # número de palavras na frase
indices = [0] * length

target_address = "1CfntEjWHwCc7moXnMHUX8QuBJaakAnv8U"

def increment(indices, base):
    for i in reversed(range(len(indices))):
        if indices[i] + 1 < base:
            indices[i] += 1
            for j in range(i+1, len(indices)):
                indices[j] = 0
            return True
    return False

count = 0
while True:
    phrase_words = [word_list[i] for i in indices]
    mnemonic_phrase = " ".join(phrase_words)
    
    if mnemo.check(mnemonic_phrase):
        entropy_bytes = mnemo.to_entropy(mnemonic_phrase)
        entropy_hex = entropy_bytes.hex()
        inteiro = int(entropy_hex, 16)
        try:
            key = Key.from_int(inteiro)
            wif = key.to_wif()
            address = key.address

            if address == target_address:
                filename = f"{address}.txt"
                with open(filename, "w") as f:
                    f.write(f"WIF: {wif}\n")
                    f.write(f"Mnemonic: {mnemonic_phrase}\n")
                    f.write(f"Entropy (hex): {entropy_hex}\n")
                    f.write(f"Integer: {inteiro}\n")
            
            # Mostra apenas as 3 primeiras palavras
            first_three = " ".join(mnemonic_phrase.split()[:3])
            print(f"{first_three} - {entropy_hex} - {inteiro} - {wif} - {address}", end="\r")
            count += 1
        except Exception as e:
            pass
    
    if not increment(indices, n):
        break

print(f"Total de frases válidas encontradas: {count}")
