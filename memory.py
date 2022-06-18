from dataclasses import dataclass


@dataclass
class Memory:
    def has_space_for(self, pages: int):
        # check if has space for new pages
        return

    def page_in(self, process):
        # fill slots for the process
        pass

    def disk_alloc(self, process):
        # alloc process in disk
        pass
