def is_palindrome_recursive(word, low_index, high_index):
    # Caso base: se os índices se cruzarem
    if low_index >= high_index:
        # Se a palavra estiver vazia, não é um palíndromo
        return word != ""

    # Se os caracteres correspondentes não forem iguais, não é um palíndromo
    if word[low_index] != word[high_index]:
        return False

    # Verifica recursivamente o próximo par de caracteres
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
