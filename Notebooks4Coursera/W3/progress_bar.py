import sys, time, queue
from typing import Any
from IPython.display import clear_output


class ProgressBarHandler:
    
    def __init__(self, end_tick: int, zero_starting: bool = True, bar_length: int = 20) -> None:
        self.end_tick = end_tick
        self.zero_starting = zero_starting
        self.bar_length = bar_length
        
        self.last_time = time.time()
        self.last_tick = 0
        
    def __call__(self, current_tick: int, *args: Any, **kwds: Any) -> Any:
        if self.zero_starting:
            current_tick += 1
            
        if current_tick >= self.end_tick:
            line = ('[{}] {:.2f}% {}/{} '+' '*10).format('█' * self.bar_length, 100, self.end_tick, self.end_tick)
            clear_output(wait=True)
            sys.stdout.write(line)
            sys.stdout.flush()
            print()
            return
            
        current_time = time.time()
        time_per_tick = (current_time - self.last_time) / (current_tick - self.last_tick) if current_tick > self.last_tick else 0
        self.last_time = current_time
        self.last_tick = current_tick       
        
        progress = current_tick / self.end_tick
        progress_bar = '█' * int(progress * self.bar_length) + '.' * (self.bar_length - int(progress * self.bar_length))
        percentage = min(progress * 100, 100)
        etr = (self.end_tick - current_tick) * time_per_tick
                
        line = '[{}] {:.2f}% {}/{} {}'.format(progress_bar, percentage, min(current_tick, self.end_tick), self.end_tick, time.strftime("%H:%M:%S", time.gmtime(etr)))
        clear_output(wait=False)
        sys.stdout.write(line)
        sys.stdout.flush()
        

if __name__ == '__main__':
    bar_handler = ProgressBarHandler(100)
    
    for i in range(100):
        bar_handler(i)
        time.sleep(0.1)