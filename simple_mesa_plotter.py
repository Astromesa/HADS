import mesa_reader as mr
import matplotlib.pyplot as plt

h = mr.MesaData('../mesa_work/LOGS/history.data')

plt.xlabel('Star age (yr)')
plt.ylabel('logLuminosity log(L/Lsun)')
plt.plot(h.star_age, h.log_L)
print("preshow")
plt.show()
print("postshow")
plt.savefig('plot1.jpg', dpi=300)
plt.close()


