from tinyec.ec import SubGroup, Curve
from tinyec import registry


'''
Here,
    p = galios field-size (is prime and > 3)
    g = generator point
    n = order of the curve (the number of all points on curve)
    h = curve cofactor (the number of non-overlapping subgroups of points, 
        which together hold all curve points)
'''

def custom_curve():
    field = SubGroup(p=17, g=(15, 13), n=18, h=1)
    curve = Curve(a=0, b=7, field=field, name='p1707')
    print(f'curve: {curve}')
    k = 8 # any number
    p = k * curve.g
    print(f"{k} * G = ({p.x}, {p.y})")


def multiplication():
    curve = registry.get_curve('secp192r1')
    print('curve:', curve)

    for k in range(0, 10):
        p = k * curve.g
        print(f"\U0001F449 {k} * G = ({p.x}, {p.y})")

    print(f"Cofactor (h) : {curve.field.h}")
    print(f'Cyclic group order (n) : {curve.field.n}')




if __name__ == '__main__':
    custom_curve()
    multiplication()