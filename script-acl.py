def verificar_tipo_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "El número no corresponde a una lista de acceso"

if __name__ == "__main__":
    numero_acl = int(input("Introduce el número de ACL IPv4: "))
    tipo_acl = verificar_tipo_acl(numero_acl)
    print("Tipo de ACL:", tipo_acl)
