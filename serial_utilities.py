import sys, glob
import serial

def serial_ports():
    """
    Regresa una lista de los puertos serie disponibles en el sistema
    """
    if sys.platform.startswith('win'):
        print('Windows')
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # Esto excluye la terminal actual "/dev/tty"
        print('Linux')
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        print('Darwin')
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Plataforma no soportada...')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result