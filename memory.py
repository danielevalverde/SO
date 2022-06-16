from dataclasses import dataclass


@dataclass
class Memory:

    def has_space_for(pages):
        # check if has space for new pages
        pass

    def page_in(process):
        # fill slots for the process
        pass

    def disk_alloc(process):
        # alloc process in disk
        pass
