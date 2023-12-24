'''
* Interface for Memory Management Unit.
* The memory management unit should maintain the concept of a page table.
* As pages are read and written to, this changes the pages loaded into the
* the limited number of frames. The MMU keeps records, which will be used
* to analyse the performance of different replacement strategies implemented
* for the MMU.
*
'''
class MMU:
    def read_memory(self, page_number):
        self.page_table[page_number] = 0

    def write_memory(self, page_number):
        self.page_table[page_number] = 1

    def set_debug(self):
        self.debug = True

    def reset_debug(self):
        self.debug = False

    def get_total_disk_reads(self):
        return self.disk_reads

    def get_total_disk_writes(self):
        return self.disk_writes

    def get_total_page_faults(self):
        return self.page_faults
