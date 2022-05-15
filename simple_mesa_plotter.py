import mesa_reader as mr
import matplotlib.pyplot as plt

h = mr.MesaData('../mesa_work/LOGS/history.data')

plt.xlabel('Star age (yr)')
plt.ylabel('logLuminosity log(L/Lsun)')
plt.plot(h.star_age, h.log_L)
plt.show()
