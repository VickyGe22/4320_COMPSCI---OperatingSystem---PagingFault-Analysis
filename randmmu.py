from mmu import MMU
import random


class RandMMU(MMU):
    def __init__(self, frames):
        self.frames = frames
        self.page_table = {}
        self.memory_list = []
        self.debug = False
        self.disk_reads = 0
        self.disk_writes = 0
        self.page_faults = 0
        self.position = 0

    def set_debug(self):
        self.debug = True

    def reset_debug(self):
        self.debug = False

    def _debug_print(self, msg):
        if self.debug:
            print(msg)

    def __lt__(self, other):
        return self.frames > other.frames

    def __eq__(self, other):
        return self.frames == other.frames

    def read_memory(self, page_number):

        if page_number in self.memory_list:
            self._debug_print(f"Page {page_number} is already in memory. Reordering the memory list.")
        else:
            self.page_faults += 1
            self.disk_reads += 1
            self._debug_print(f"Page {page_number} is not in memory. Page fault occurred. Total page faults: {self.page_faults}.")
            if len(self.memory_list) >= self.frames:
                removed_page = random.choice(self.memory_list)
                self.position = self.memory_list.index(removed_page)
                modify_bit = self.page_table[removed_page]
                if modify_bit == 1:
                    self.disk_writes += 1
                    self._debug_print(f"Page {removed_page} had a modify bit set. Writing to disk. Total disk writes: {self.disk_writes}.")
                self.memory_list.remove(removed_page)
                self._debug_print(f"Removed page {removed_page} from cache")
                self.memory_list.insert(self.position, page_number)
                self._debug_print(f"Adding page {page_number} to memory.")
            else:
                self.memory_list.append(page_number)
                self._debug_print(f"Adding page {page_number} to memory.")
            self.page_table[page_number] = 0
            
    
    def write_memory(self, page_number):

        if page_number in self.memory_list:
            self._debug_print(f"Page {page_number} is already in memory. Reordering the memory list.")
        else:
            self.page_faults += 1
            self.disk_reads += 1
            self._debug_print(f"Page {page_number} is not in memory. Page fault occurred. Total page faults: {self.page_faults}.")
            if len(self.memory_list) >= self.frames:
                removed_page = random.choice(self.memory_list)
                self.position = self.memory_list.index(removed_page)
                modify_bit = self.page_table[removed_page]
                if modify_bit == 1:
                    self.disk_writes += 1
                    self._debug_print(f"Page {removed_page} had a modify bit set. Writing to disk. Total disk writes: {self.disk_writes}.")
                self.memory_list.remove(removed_page)
                self._debug_print(f"Removed page {removed_page} from cache")
                self.memory_list.insert(self.position, page_number)
                self._debug_print(f"Adding page {page_number} to memory.")
            else:
                self.memory_list.append(page_number)
                self._debug_print(f"Adding page {page_number} to memory.")
        self.page_table[page_number] = 1



    def get_total_disk_reads(self):
        return self.disk_reads

    def get_total_disk_writes(self):
        return self.disk_writes

    def get_total_page_faults(self):
        return self.page_faults
