scale = float(input("리히터규모를입력하시오: "))
if scale >= 8.0:
    print("대부분의구조물이파괴됩니다. ")
elif scale >= 7.0:
    print("지표면에균열이발생합니다.")
elif scale >= 4.0:
    print("빈약한건물에큰피해가있습니다. ")
elif scale >= 2.0:
    print("물건들이흔들리거나떨어집니다.")
else:
    print("지진계에의해서만탐지가능합니다. ")
