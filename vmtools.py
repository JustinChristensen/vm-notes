import os

sys.path.insert(0, "./scripts/gdb")

from linux.tasks import task_lists, get_task_by_pid
from linux.utils import CachedType, container_of

task_type = CachedType("struct task_struct")
mm_type = CachedType("struct mm_struct")

def mm_lists():
    mm_ptr_type = mm_type.get_type().pointer()
    init_mm = gdb.parse_and_eval("init_mm").address
    mm = init_mm

    while True:
        yield mm
        mm = container_of(mm['mmlist']['next'], mm_ptr_type, "mmlist")
        if mm == init_mm:
            return

class VmPsFunc(gdb.Function):
    """Dump VM details about tasks"""

    def __init__(self):
        super(VmPsFunc, self).__init__("vm_ps")

    def invoke(self):
        task_fmt = "{pid!s:<5} {comm:<32} {mmap_base!s:<20} {task_size!s:<20}\n"

        gdb.write(task_fmt.format(
            pid="pid", comm="name",
            mmap_base="mmap_base", task_size="task_size"
        ))

        for task in task_lists():
            if task["mm"]:
                mm = task["mm"].dereference()

                gdb.write(task_fmt.format(
                    pid=task["pid"], comm=task["comm"].string(),
                    mmap_base=mm["mmap_base"], task_size=mm["task_size"]
                ))

        return True

VmPsFunc()

class VmDetails(gdb.Function):
    """Dump VM details for a specific task"""

    def __init__(self):
        super(VmDetails, self).__init__("vm_details")

    def invoke(self, task, longfmt=False):
        if (task.type == task_type.get_type().pointer()):
            task = task.dereference()

        if not task["mm"]:
            gdb.write("no mm")
            return False

        mm = task["mm"].dereference()

        if not longfmt:
            gdb.write("pid: {pid}\ntask_size: {task_size}\nmmap_base: {mmap_base}\nmmap_end: {mmap_end}\n".format(
                pid=task["pid"],
                task_size=mm["task_size"],
                mmap_base=mm["mmap_base"],
                mmap_end=mm["highest_vm_end"]
            ))

        vma = mm["mmap"]

        if vma:
            gdb.write("{} vmas:\n".format(mm["map_count"]))

        total = 0

        while vma:
            vma = vma.dereference()
            if longfmt:
                gdb.write("{}\n".format(vma))
            else:
                size = vma["vm_end"] - vma["vm_start"]
                total += size
                gdb.write("  start: {}, end: {}, size: {}\n".format(vma["vm_start"], vma["vm_end"], size))
            vma = vma["vm_next"]

        if not longfmt:
            gdb.write("grand total: {}\n".format(total))

        return True

VmDetails()

# Hmm, mm_struct's arent' chained together like tasks are
# class VmMMsFunc(gdb.Function):
#     """Dump MM details about tasks"""
# 
#     def __init__(self):
#         super(VmMMsFunc, self).__init__("vm_mms")
# 
#     def invoke(self, longfmt=False):
#         for mm in mm_lists():
#             if longfmt:
#                 gdb.write("{}".format(mm.dereference()))
#             else:
#                 gdb.write("{} {} ".format(mm["mmap_base"], mm["highest_vm_end"], ))
# 
#                 task = mm["owner"]
#                 if task:
#                     gdb.write("{}".format(task["pid"]))
# 
#                 gdb.write("\n")
# 
# 
#         return True
# 
# VmMMsFunc()

