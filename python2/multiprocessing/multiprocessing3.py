import multiprocessing
import multiprocessing3_import_worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=multiprocessing4_import_worker.worker)
        jobs.append(p)
        p.start()