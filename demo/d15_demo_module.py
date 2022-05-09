# import d12_print_pattern_demo
# import d12_print_pattern_demo as d12_module
# import d15.d15_module
# import d15.d15_module as demo_module
# from d12_print_pattern_demo import inBangCuuChuong, inNguoc, inXuoi

# d12_print_pattern_demo.inBangCuuChuong(3)
# inBangCuuChuong(5)
# print('Biến __name__ trong file này là: {}'.format(__name__))

# II> DEMO IMPORT SỬ DỤNG THƯ VIỆN MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np


x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
