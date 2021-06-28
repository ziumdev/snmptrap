from multiprocessing import Process
import trapReceiver
receiverProcess = Process(target=trapReceiver.run)

if __name__ == '__main__':
    receiverProcess.start()
    # receiverProcess.join()