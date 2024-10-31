from multiprocessing.pool import AsyncResult
from tqdm import tqdm
import time

class ConcurrentTqdm(tqdm):
    def __init__(self, *args, sequential=False, safe=True, **kwargs):
        self._strategy = 'sequential' if sequential else 'asynchronous'
        self._safe = safe
        super().__init__(*args, **kwargs)
    
    def unsafe(self):
        """Set the class to unsafe mode where exceptions are not checked."""
        self._safe = False
        return self

    # Check if the iterator contains future objects
    def _is_future(self, iterator):
        return all(isinstance(i, AsyncResult) for i in iterator)
    
    def __iter__(self):
        if self._is_future(self.iterable):
            if self._strategy == 'sequential':
                return self._iter_future_sequential_safe() if self._safe else self._iter_future_sequential_unsafe()
            else:
                return self._iter_future_asynchronous_safe() if self._safe else self._iter_future_asynchronous_unsafe()
        return super().__iter__()

    # Safe version of sequential iteration
    def _iter_future_sequential_safe(self):
        with self:
            for future in self.iterable:
                try:
                    result = future.get()
                    if result is not None:
                        yield (True, result)
                except Exception as e:
                    yield (False, e)
                self.update()

    # Unsafe version of sequential iteration
    def _iter_future_sequential_unsafe(self):
        with self:
            for future in self.iterable:
                result = future.get()
                if result is not None:
                    yield result
                self.update()

    # Safe version of asynchronous iteration
    def _iter_future_asynchronous_safe(self):
        futures = list(self.iterable)
        with self:
            while futures:
                for future in futures[:]:
                    if future.ready():
                        try:
                            result = future.get()
                            if result is not None:
                                yield (True, result)
                        except Exception as e:
                            yield (False, e)
                        futures.remove(future)
                        self.update()
                time.sleep(0.1)  # Short sleep to prevent high CPU usage

    # Unsafe version of asynchronous iteration
    def _iter_future_asynchronous_unsafe(self):
        futures = list(self.iterable)
        with self:
            while futures:
                for future in futures[:]:
                    if future.ready():
                        result = future.get()
                        if result is not None:
                            yield result
                        futures.remove(future)
                        self.update()
                time.sleep(0.1)  # Short sleep to prevent high CPU usage

def __dummy_task(x):
    time.sleep(1)
    if x % 2 == 0:
        return x * x
    else:
        raise ValueError(f"Odd number encountered: {x}")

# Example usage
if __name__ == "__main__":
    from multiprocessing import Pool



    # Create a pool of workers
    with Pool(processes=4) as pool:
        tasks = [pool.apply_async(__dummy_task, (i,)) for i in range(10)]

        # Case 1: Asynchronous processing (default) with safety
        print("Using asynchronous strategy with safety")
        for result in ConcurrentTqdm(tasks, total=len(tasks)):
            pass

        for result in ConcurrentTqdm(tasks, total=len(tasks)):
            pass
        # Case 2: Sequential processing without safety
        print("\nUsing sequential strategy without safety")
        tasks = [pool.apply_async(__dummy_task, (i,)) for i in range(10)]
        for result in ConcurrentTqdm(tasks, total=len(tasks), sequential=True).unsafe():
            pass