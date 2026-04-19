import inspect

def funksiya(imzo):
    """Berilgan funksiyaning parametrlar ro'yxatini qaytaring"""
    return inspect.signature(imzo).parameters.keys()

# Misol:
def misol_funksiya(a, b, c):
    return a + b + c

print(funksiya(misol_funksiya))
