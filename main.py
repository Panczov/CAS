from pymavlink import mavutil
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


connection ='tcp:127.0.0.1:5763'
t = np.array([])
h = np.array([])
i = 0

try:

    vehicle = mavutil.mavlink_connection(connection)

    while True:

        msg = vehicle.recv_msg()
        if msg is not None and msg.get_type() == 'GLOBAL_POSITION_INT':  # Sprawdzenie istnienia wiadomości

            altitude = (msg.relative_alt / 1000.0)
            print(f'Altitude: {altitude} meters, ')
            h = np.append(h,altitude)
            t = np.append(t, 1+i)
            i += 1
            # Wedle liczenia czasu to mniej więcej co sekunde (nie wiem jak dokładnie) dostawałęm informację o
            # Altitude naszego samolociku stąd uznałem że chyba najmądrzej tak to będzie po prostu napisać.
            # Jak da się dokładniej to mogę poprawić
        if(vehicle.time_since('HEARTBEAT')) > 2.5:
            # Dałem 2.5 sekundy... nie wiem wyczułem że tak bęzdzie optymalnie
            # Nie za bardzo to zmienia działanie programu i program sam z siebie nie wyłącza się bo sprawdzałem
            # Natomiast dla bezpieczeństwa można tę wartość zwiększyć do 5, to nic w niczym nie zmienia
            print("Connection terminated")

            fig, ax = plt.subplots()

            ax.plot(t, h)
            ax.set_xlabel("Time")
            ax.set_ylabel("Altitude")
            print(t, h)

            plt.show()
            break
            # Tutaj raczej wiadomo o co chodzi
except Exception:
    print("Mavutil connection not established")






