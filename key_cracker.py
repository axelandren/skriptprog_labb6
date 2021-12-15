import time
import random
import multiprocessing as mp

start_time = time.time()

def main():
    cores = 6
    dx = 4294967295 / cores
    x = round(dx)
    starting_keys = [x * i for i in range(cores)]
    end_keys = [x * (i + 1) for i in range(cores)]
    secret_key = random.randint(0, 4294967295)

    print(f"CPU (process) count is: {cores}")
    print(f"Start keyspace offset: {starting_keys}")
    print(f"End keyspace offset: {end_keys}")
    print(f"Random secret key is: {secret_key}")

    processes = []

    for i in range(cores):
        p = mp.Process(target=worker, args=(i, starting_keys[i], end_keys[i], secret_key))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


def worker(work, cur_key, end_key, secret_key):
    print('Worker:', work, " keyspace start at", cur_key, " and end at ", end_key)
    while cur_key < end_key:
        if cur_key == secret_key:
            print(f"Worker: {work} found secret key: {cur_key}!")
            print(f"It took {round(time.time() - start_time, 2)} second(s) to find the key")
            return
        else:
            cur_key += 1


if __name__ == '__main__':
    main()
