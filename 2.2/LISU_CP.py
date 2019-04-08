from threading import Thread
from LISU_JD import LISUJD
from LISU_SP import LISUSP
from LISU_WD import LISUWD
  
if __name__ == '__main__':
    Thread(target = LISUJD).start()
    Thread(target = LISUSP).start()
    #Thread(target = LISUWD).start()

    #Thread(target = LISUJD).join()
    #Thread(target = LISUSP).join()
    #Thread(target = LISUWD).join()
