from threading import Thread
from LISU_JD import LISUJD
from LISU_WD import LISUWD
  
if __name__ == '__main__':
    Thread(target = LISUJD).start()
    Thread(target = LISUWD).start()
