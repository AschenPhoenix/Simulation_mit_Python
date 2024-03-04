# ##################################################################################################################
# ODE-Funktion für einfache DGLs
def ode_func(t, x, m, b, c):
    x1, x1p, x2, x2p, x3, x3p = x[0], x[1], x[2], x[3], x[4], x[5]

    yp = np.zeros(len(x)).tolist()
    yp[0] = x1p
    yp[1] = (-b * () - c * () + ('''Anregungskräfte''')) / m[0]
    yp[2] = x2p
    yp[3] = (-b * () - c * () + ('''Anregungskräfte''')) / m[1]
    yp[4] = x3p
    yp[5] = (-b * () - c * () + ('''Anregungskräfte''')) / m[2]
    return yp

# =======================================================
# ODE Aufruf und plotten
m = [0, 0, 0]
b = 0
c = 0

t = (0,20)
ts = 0.01

anz_variablen = 3
y0 = np.zeros(2*anz_variablen).tolist()
sol = solve_ivp(ode_func, t, y0, method='RK45', max_step=ts, t_eval=np.linspace(0,20,200),  args=(m, b, c))

plt.figure()
for n in range(anz_variablen):
    plt.plot(sol.t, sol.y[2*n], label=f'$x_{n+1}(t)$')
plt.xlabel('Zeit')
plt.ylabel('Weg')
plt.legend(loc='best')
plt.grid()
plt.show()


# ##################################################################################################################