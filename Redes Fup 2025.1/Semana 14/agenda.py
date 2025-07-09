dict = {'nome': input(),
        'idade': int(input()),
        'peso': float(input()),
        'cidade': input(),
        'telefone': int(input()),
        'apelido': input()
    }

print(f"O contato {dict['nome']} tem {dict['idade']} anos de idade, "
      f"pesa {dict['peso']} Kg, mora em {dict['cidade']}, "
      f"o telefone dele é {dict['telefone']} e seu apelido é {dict['apelido']}.")