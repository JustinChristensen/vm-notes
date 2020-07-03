import os

sys.path.insert(0, "./scripts/gdb")

from linux.tasks import task_lists, get_task_by_pid
from linux.utils import CachedType

task_type = CachedType("struct task_struct")

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

    def invoke(self, task):
        if (task.type == task_type.get_type().pointer()):
            task = task.dereference()

        if not task["mm"]:
            gdb.write("no mm")
            return False

        mm = task["mm"].dereference()

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
            size = vma["vm_end"] - vma["vm_start"]
            total += size
            gdb.write("  start: {}, end: {}, size: {}\n".format(vma["vm_start"], vma["vm_end"], size))
            vma = vma["vm_next"]

        gdb.write("grand total: {}\n".format(total))

        return True

VmDetails()
