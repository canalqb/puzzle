from mnemonic import Mnemonic

# Inicializa o objeto Mnemonic para inglês
mnemo = Mnemonic("english")

# Carrega o arquivo de texto
file_path = "documento.txt"  # Substitua pelo caminho do seu arquivo
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Quebra o texto em palavras e normaliza
words_in_text = text.lower().replace("\n", " ").split()
words_in_text = [word.strip(".,!?;:()[]{}\"'") for word in words_in_text]

# Lista BIP39
bip39_words = set(mnemo.wordlist)

# Filtra palavras que pertencem ao BIP39
words_in_bip39 = [word for word in words_in_text if word in bip39_words]

# Remove duplicatas e organiza
words_in_bip39 = sorted(set(words_in_bip39))

# Resultado
print("Palavras do documento que estão no BIP39:")
for word in words_in_bip39:
    print(word)
